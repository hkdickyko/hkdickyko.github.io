import ustruct
from time import sleep_ms
import array

_COMMAND_BIT = const(0x80)
_REGISTER_AILT = const(0x04)
_REGISTER_AIHT = const(0x06)
_REGISTER_ENABLE = const(0x00)
_ENABLE_AIEN = const(0x10)
_REGISTER_APERS = const(0x0c)
_REGISTER_CONTROL = const(0x0f)
_REGISTER_ATIME = const(0x01)
_ENABLE_AEN = const(0x02)
_ENABLE_PON = const(0x01)
_REGISTER_STATUS = const(0x13)
_REGISTER_CDATA = const(0x14)
_REGISTER_RDATA = const(0x16)
_REGISTER_GDATA = const(0x18)
_REGISTER_BDATA = const(0x1a)

_CYCLES = (0, 1, 2, 3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60)
_GAINS = (1, 4, 16, 60)

class TCS3472():
        
    def __init__(self, i2c, led):
        self._i2c = i2c
        self._address = 0x29
        self._led = led
        self.gain(1)
        self.integration_time(2.4)
        self._active = False

    def _register8(self, register, value=None):
        register |= _COMMAND_BIT
        if value is None:
            return self._i2c.readfrom_mem(self._address, register, 1)[0]
        data = ustruct.pack('<B', value)
        self._i2c.writeto_mem(self._address, register, data)

    def _register16(self, register, value=None):
        register |= _COMMAND_BIT
        if value is None:
            data = self._i2c.readfrom_mem(self._address, register, 2)
            return ustruct.unpack('<H', data)[0]
        data = ustruct.pack('<H', value)
        self._i2c.writeto_mem(self._address, register, data)
        
    def readStatus(self):
        return self._register8(REG_STATUS)

    def readRawData(self):
        c = self._register16(REG_CDATA)
        r = self._register16(REG_RDATA)
        g = self._register16(REG_GDATA)
        b = self._register16(REG_BDATA)
        data = (r, g, b, c)
        return self.html_hex(data)
    
    def _valid(self):
        return bool(self._register8(_REGISTER_STATUS) & 0x01)

    def read(self, raw=False):
        was_active = self.active()
        self.active(True)
        while not self._valid():
            sleep_ms(int(self._integration_time + 0.9))
        data = tuple(self._register16(register) for register in (
            _REGISTER_RDATA,
            _REGISTER_GDATA,
            _REGISTER_BDATA,
            _REGISTER_CDATA,
        ))
        self.active(was_active)
        if raw:
            return data
        return self.convertRGB(data)    
    
    def active(self, value=None):
        if value is None:
            return self._active
        value = bool(value)
        if self._active == value:
            return
        self._active = value
        enable = self._register8(_REGISTER_ENABLE)
        if value:
            self._register8(_REGISTER_ENABLE, enable | _ENABLE_PON)
            sleep_ms(3)
            self._register8(_REGISTER_ENABLE,
                enable | _ENABLE_PON | _ENABLE_AEN)
        else:
            self._register8(_REGISTER_ENABLE,
                enable & ~(_ENABLE_PON | _ENABLE_AEN))    
    
    def _temperature_and_lux(self, data):
        r, g, b, c = data
        # 基於 6500K 熒光、3000K 熒光 和 60W 白熾燈值範圍很廣。 
        # RGB 值映射到它們的 XYZ 對應值、Y = 照度或勒克斯 
        x = -0.14282 * r + 1.54924 * g + -0.95641 * b
        y = -0.32466 * r + 1.57837 * g + -0.73191 * b
        z = -0.68202 * r + 0.77073 * g +  0.56332 * b
        # 計算色度坐標
        xc = X / (X + Y + Z);
        yc = Y / (X + Y + Z);
        # 使用 McCamy 公式確定 CCT
        n = (xc - 0.3320) / (0.1858 - yc)
        # 計算最終的 CCT
        cct = 449.0 * n**3 + 3525.0 * n**2 + 6823.3 * n + 5520.33
        return cct, y

    def integration_time(self, value=None):
        if value is None:
            return self._integration_time
        value = min(614.4, max(2.4, value))
        cycles = int(value / 2.4)
        self._integration_time = cycles * 2.4
        return self._register8(_REGISTER_ATIME, 256 - cycles)

    def gain(self, value):
        if value is None:
            return _GAINS[self._register8(_REGISTER_CONTROL)]
        if value not in _GAINS:
            raise ValueError("gain must be 1, 4, 16 or 60")
        return self._register8(_REGISTER_CONTROL, _GAINS.index(value))    
    
    def set_leds(self, state=0):
        self._led.value(state)
        
    def convertRGB(self, data):
        r, g, b, c = data
        r = 256 * r / c 
        g = 256 * g / c
        b = 256 * b / c
        return (r, g , b)
        
    def html_rgb(self, data):
        r, g, b, c = data
        red = pow((int((r/c) * 256) / 255), 2.5) * 255
        green = pow((int((g/c) * 256) / 255), 2.5) * 255
        blue = pow((int((b/c) * 256) / 255), 2.5) * 255
        return red, green, blue
    
    def gammaTable(self):
        self._gamma = array.array('B')
        for i in range(256):
            x = i / 255.0;
            value = int(pow(x, 2.5) * 255.0)
            self._gamma.append(value);
            
    def gamma(self, value):
        return self._gamma[int(value)]

    def html_hex(self, data):
        r, g, b = self.html_rgb(data)
        return "{:02x}{:02x}{:02x}".format(int(r), int(g), int(b))
    
    def toHex(self, data):
        r, g, b = data
        return "{:02x}{:02x}{:02x}".format(int(r), int(g), int(b))
    
    def threshold(self, cycles=None, min_value=None, max_value=None):
        if cycles is None and min_value is None and max_value is None:
            min_value = self._register16(_REGISTER_AILT)
            max_value = self._register16(_REGISTER_AILT)
            if self._register8(_REGISTER_ENABLE) & _ENABLE_AIEN:
                cycles = _CYCLES[self._register8(_REGISTER_APERS) & 0x0f]
            else:
                cycles = -1
            return cycles, min_value, max_value
        if min_value is not None:
            self._register16(_REGISTER_AILT, min_value)
        if max_value is not None:
            self._register16(_REGISTER_AIHT, max_value)
        if cycles is not None:
            enable = self._register8(_REGISTER_ENABLE)
            if cycles == -1:
                self._register8(_REGISTER_ENABLE, enable & ~(_ENABLE_AIEN))
            else:
                self._register8(_REGISTER_ENABLE, enable | _ENABLE_AIEN)
                if cycles not in _CYCLES:
                    raise ValueError("invalid persistence cycles")
                self._register8(_REGISTER_APERS, _CYCLES.index(cycles))
                
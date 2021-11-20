---
 category: [積體電路]
 tags: [IoT]
 title: 顏色傳感器
 date: 2021-11-20 12:00:00
---


# 顏色傳感器

TCS3472 器件提供紅色、綠色、藍色 (RGB) 和清晰光感測值的數字返回。 IR 濾光片集成在芯片上並位於顏色感應光電二極管，可最大限度地減少入射光的 IR 光譜分量，並允許準確地進行顏色測量。


[網絡資源 - TCS3472](https://github.com/adafruit/micropython-adafruit-tcs34725)


```python
import struct

ADDR = 0x29

LEVEL = 65.535

class TCS3472:
    def __init__(self, i2c, led):
        self.i2c = i2c
        self.i2c.writeto(ADDR, b'\x80\x03')
        self.i2c.writeto(ADDR, b'\x81\x2b')
        self.led = led

    def scaled(self):
        crgb = self.raw()
        if crgb[0] > 0:
            return tuple(float(x) / crgb[0] for x in crgb[1:])
        return (0,0,0)

    def rgb(self):
        return tuple(int(x * 255) for x in self.scaled())

    def light(self):
        return self.raw()[0]
    
    def brightness(self, level=LEVEL):
        return int((self.light() / level))

    def valid(self):
        self.i2c.writeto(ADDR, b'\x93')
        return self.i2c.readfrom(ADDR, 1)[0] & 1

    def raw(self):
        self.i2c.writeto(ADDR, b'\xb4')
        return struct.unpack("<HHHH", self.i2c.readfrom(ADDR, 8))
        
    def set_leds(self, state):
        self.led.value(state)




from machine import Pin
from machine import I2C
from drivers.tcs3472 import TCS3472
from time import sleep_ms

i2c_bus = I2C(0, sda=Pin(21), scl=Pin(22))
led=Pin(5, Pin.OUT)
t = TCS3472(i2c_bus,led)
t.set_leds(1)
i = 0
while i < 10:
    t.set_leds(1)
    sleep_ms(200)
    r, g, b = t.rgb()
    l = t.light()
    print("#{:02x} {:02x} {:02x} - {}".format(r, g, b, l))
    sleep_ms(300)
    i = i + 1
t.set_leds(0)



```
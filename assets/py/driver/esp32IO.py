import machine
import time
import math

class esp32IO:
    
  def __init__(self,freq=400000):
    self.__freq=freq
    self.__hspi=None
    self.__vspi=None
    self.__i2c=None
    
  def On(self,pinID):
    return machine.Pin(pinID, machine.Pin.OUT)

  def Off(self,pinID):
    return machine.Pin(pinID, machine.Pin.IN)

  def i2cInit(self):
    self.__i2c=machine.I2C(scl=machine.Pin(22),sda=machine.Pin(21),freq=self.__freq)

  def i2cCmd(self,address,data):
    self.__i2c.writeto(address,data)

  def i2cCmdOffset(self,address,data,offset):
    self.__i2c.writeto_mem(address,offset,data)

  def i2cRead(self,address,length):
    return self.__i2c.readfrom(address,length)
      
  def i2cReadOffset(self,address,length,offset):
    return self.__i2c.readfrom_mem(address,offset,length)

  def spi_init(self,pbaudrate=80000000):
    self.__hspi = machine.SPI(1, sck=machine.Pin(14), mosi=machine.Pin(13), miso=machine.Pin(12), baudrate=pbaudrate)
    self.__vspi = machine.SPI(2, sck=machine.Pin(18), mosi=machine.Pin(23), miso=machine.Pin(19), baudrate=pbaudrate)

  def spiRead(self,hspi,length):
    if hspi:
        return self.__hspi.read(length)
    else:
        return self.__vspi.read(length)

  def spiReadOffset(self,hspi,length,offset):
    if hspi:
        return self.__hspi.read(length,offset)
    else:
        return self.__vspi.read(length,offset)

  def spiReadOffset(self,hspi,length,offset=0x00):
    buf = bytearray(length)     
    if hspi:
        return self.__hspi.readinto(buf, offset) 
    else:
        return self.__vspi.readinto(buf, offset)
    return buf

  def spiWrite(self,hspi,data):
    if hspi:
      return self.__hspi.write(data)      
    else:
      return self.__vspi.write(data)      

  def spiWriteRead(self,hspi,data,length):
    buf = bytearray(length)
    if hspi:
      MOSI_buf = data
      self.__hspi.write_readinto(MOSI_buf, MISO_buf)
    else:
      MOSI_buf = data
      self.__vspi.write_readinto(MOSI_buf, MISO_buf)
    return buf
        

class devices:
    
  def __init__(self):
    self.__humidty=0.0
    self.__temperature=0.0
    self.__dewpoint=0.0

  def aht10(self):
    AHT10_ADDRESS=0x38
    CMD_INITIALIZE = bytearray([0xE1, 0x08, 0x00])
    CMD_MEASURE = bytearray([0xAC, 0x33, 0x00])
    AHT10_RESET = bytearray([0xBA])
    AHT_CONST=pow(2,20)
    __espx=esp32IO()
    __espx.i2cInit()
    __espx.i2cCmd(AHT10_ADDRESS,AHT10_RESET)
    time.sleep_ms(75)
    __espx.i2cCmd(AHT10_ADDRESS,CMD_INITIALIZE)
    __espx.i2cCmd(AHT10_ADDRESS,CMD_MEASURE)
    time.sleep_ms(100)
    __buf=__espx.i2cRead(AHT10_ADDRESS, 6)
    __humidty_raw=__buf[1] << 12 | __buf[2] << 4 | __buf[3] >> 4
    __degree_raw=(__buf[3] & 0x0F) << 16 | __buf[4] << 8 | __buf[5]
    self.__humidty=float((__humidty_raw/AHT_CONST)*100)
    self.__temperature=float((__degree_raw/AHT_CONST)*200-50)
    if self.__humidty>0:
        factor = (math.log(self.__humidty, 10) - 2) / 0.4343 + (17.62 * self.__temperature) / (243.12 + self.__temperature)
        self.__dewpoint = float(243.12 * factor / (17.62 - factor))
        return (self.__temperature, self.__humidty, self.__dewpoint)
    else:
        return self.aht10() 
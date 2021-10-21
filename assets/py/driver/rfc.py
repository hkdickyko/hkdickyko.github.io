import ustruct
import array
from utime import ticks_ms
from drivers.mfrc522 import MFRC522

class rfc:
    
  def __init__(self, spi, rst, cs):
    self.key=b'\xff\xff\xff\xff\xff\xff'
    self.rdr = MFRC522(spi, rst, cs)

  def _checkExist(self, value, arr):
    for i in arr:
      if value==i:
        return True
    return False

  def setKey(self, value=""):
    ikey = list(value)
    if len(ikey)!=6:
      return False
    self.key = ustruct.pack('6b', ord(ikey[0]), ord(ikey[1]), ord(ikey[2]), ord(ikey[3]), ord(ikey[4]), ord(ikey[5]))
    return True

  def read(self, block):
    while True:
      (stat, tag_type) = self.rdr.request(self.rdr.REQIDL)
      if stat == self.rdr.OK:
        (stat, raw_uid) = self.rdr.anticoll()
        if stat == self.rdr.OK:
          tagType = "0x%02x" % tag_type
          UID = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
          if self.rdr.select_tag(raw_uid) == self.rdr.OK:
            ms = ticks_ms()
            blockArray = bytearray(16)
            if self.rdr.auth(self.rdr.AUTHENT1A, block, self.key, raw_uid) == self.rdr.OK:
              self.rdr.read(block, into=blockArray)
              self.rdr.stop_crypto1()
              return (0, tagType, UID, block, blockArray) # Data read from card
              break
            else:
              return -1 # Auth err
          self.rdr.stop_crypto1()
        else:
          return -2 # Select failed
   
  def write(self, block, strValue):
    checkArr = array.array('i', [3,7,11,15,19,23,27,31,35,39,43,47,51,55,59,63])
    if self._checkExist(block, checkArr):
      return -5 # "Key Area cannot be written
    if len(strValue)!=16:
      return -4 # Length of Data error
    else:
      char = list(strValue)
      inputbytes = ustruct.pack('16b', ord(char[0]), ord(char[1]), ord(char[2]), ord(char[3]), \
                            ord(char[4]), ord(char[5]), ord(char[6]), ord(char[7]),ord(char[8]), ord(char[9]), \
                            ord(char[10]), ord(char[11]), ord(char[12]), ord(char[13]), ord(char[14]), ord(char[15]))
      while True:
        (stat, tag_type) = self.rdr.request(self.rdr.REQIDL)
        if stat == self.rdr.OK:
          (stat, raw_uid) = self.rdr.anticoll()
          if stat == self.rdr.OK:
            tagType = "0x%02x" % tag_type
            UID = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            if self.rdr.select_tag(raw_uid) == self.rdr.OK:
                if self.rdr.auth(self.rdr.AUTHENT1A, block, self.key, raw_uid) == self.rdr.OK:
                    stat = self.rdr.write(block, inputbytes)
                    self.rdr.stop_crypto1()
                    if stat == self.rdr.OK:
                        return (0, tagType, UID, block) # Data written to card
                    else:
                        return -1 # Failed to write data to card
                else:
                    return -2 # Authentication error
            else:
              return -3 #"Failed to select tag"

  def setKeyA(self, block, key):
    checkArr = array.array('i', [3,7,11,15,19,23,27,31,35,39,43,47,51,55,59,63])
    if not self._checkExist(block, checkArr):
      return -1
    if len(key)!=6:
      return -4 # Length of Data error
    else:          
      ikey = list(key)
      result = self.read(block)
      char = ustruct.unpack('16b',result[4])
      inputbytes = ustruct.pack('16b', ord(ikey[0]), ord(ikey[1]), ord(ikey[2]), ord(ikey[3]), ord(ikey[4]), ord(ikey[5]), \
                                       char[6], char[7], char[8], char[9], \
                                       char[10], char[11], char[12], char[13], char[14], char[15])
      while True:
        (stat, tag_type) = self.rdr.request(self.rdr.REQIDL)
        if stat == self.rdr.OK:
          (stat, raw_uid) = self.rdr.anticoll()
          if stat == self.rdr.OK:
            tagType = "0x%02x" % tag_type
            UID = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            if self.rdr.select_tag(raw_uid) == self.rdr.OK:
                if self.rdr.auth(self.rdr.AUTHENT1A, block, self.key, raw_uid) == self.rdr.OK:
                    stat = self.rdr.write(block, inputbytes)
                    self.rdr.stop_crypto1()
                    if stat == self.rdr.OK:
                        return (0, tagType, UID, block) # Data written to card
                    else:
                        return -1 # Failed to write data to card
                else:
                    return -2 # Authentication error
            else:
              return -3 #"Failed to select tag"

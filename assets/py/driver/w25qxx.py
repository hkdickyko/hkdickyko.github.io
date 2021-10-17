from machine import SPI, Pin
from micropython import const
import gc
import time
 
 
__TYPE = dict(
 W25Q80 = 0XEF13,
 W25Q16 = 0XEF14,
 W25Q32 = 0XEF15,
 W25Q64 = 0XEF16,
 W25Q128 = 0XEF17,
)
 
MEM_SIZE = {
    0XEF13 : 1000000,
    0XEF14 : 2000000,
    0XEF15 : 4000000,
    0XEF16 : 8000000,
    0XEF17 : 16000000,
}
  
W25X_WriteEnable		= const(0x06)
W25X_WriteDisable		= const(0x04)
W25X_ReadStatusReg		= const(0x05)
W25X_WriteStatusReg		= const(0x01) 
W25X_ReadData			= const(0x03) 
W25X_FastReadData		= const(0x0B) 
W25X_FastReadDual		= const(0x3B) 
W25X_PageProgram		= const(0x02) 
W25X_BlockErase			= const(0xD8) 
W25X_SectorErase		= const(0x20) 
W25X_ChipErase			= const(0xC7) 
W25X_PowerDown			= const(0xB9) 
W25X_ReleasePowerDown	= const(0xAB) 
W25X_DeviceID			= const(0xAB) 
W25X_ManufactDeviceID	= const(0x90) 
W25X_JedecDeviceID		= const(0x9F) 
 
class __W25QXX:
    def __init__(self, SPI, CS_PIN):
        self.__SPI = SPI
        self.__CS_PIN = CS_PIN
        self.read(0,1)
        self.TYPE = self.__readID()
#        self.TYPE = 0XEF17		# set for the size of the W25QXX
        self.__MEM = MEM_SIZE[self.TYPE]
        if self.TYPE in list(__TYPE.values()):
            print("W25QXX type is " + list(__TYPE.keys())[list(__TYPE.values()).index(self.TYPE)])
        else: print("unknown device")
         # Write a byte
    def __writeByte(self, b):
        self.__SPI.write(bytearray([b]))
         # Read status register
    def __readSR(self):
        self.__CS_PIN.off()
        self.__SPI.write(bytearray([W25X_ReadStatusReg]))
        ret = list(self.__SPI.read(1))
        self.__CS_PIN.on()
        return ret[0]
         #        
    def __writeSR(self, sr):
        self.__CS_PIN.off()
        self.__SPI.write(bytearray([W25X_WriteStatusReg]))
        self.__SPI.write(bytearray([(sr)]))
        self.__CS_PIN.on()
         # W25qxx write enable	
         # Set Wel Set   
    def __writeEnable(self):
        self.__CS_PIN.off()
        self.__SPI.write(bytearray([W25X_WriteEnable]))
        self.__CS_PIN.on()
         # W25qxx write prohibited	
         # Clear Wel  
    def __writeDisable(self):
        self.__CS_PIN.off()
        self.__SPI.write(bytearray([W25X_WriteDisable]))
        self.__CS_PIN.on()
         # Read the chip ID
    def __readID(self):
        self.__CS_PIN.off()
        self.__SPI.write(bytearray([0x90,0,0,0]))
        tmp = list(self.__SPI.read(2))
        return (tmp[0]<<8)+ tmp[1]
         # Read SPI Flash  
         # Text the data of the specified length starts at the specified address
         # PBuffer: Data Store
         # Ieddr: Start reading address (24bit)
         # NumbyToread: Number of bytes to read (maximum 65535)    
    def read(self, addr, num):
        self.__CS_PIN.off()
        self.__SPI.write(bytearray([W25X_ReadData, (addr>>16)&0xff, (addr>>8)&0xff,addr&0xff]))
        ret = self.__SPI.read(num)
        self.__CS_PIN.on()
        return ret
         # SPI writes less than 256 bytes in one page (0 ~ 65535)
         #       2 2 2    
         # PBuffer: Data Store
         # WriteAddr: Add address (24bit)
         # NumbyToWrite: The number of bytes to be written (maximum 256), the number should not exceed the number of residual bytes of the page !!!
    def __writePage(self, buff, addr, num):
        self.__writeEnable()
        self.__CS_PIN.off()
        self.__SPI.write(bytearray([W25X_PageProgram, (addr>>16)&0xff, (addr>>8)&0xff, addr&0xff]))
        self.__SPI.write(buff[:num])
        self.__CS_PIN.on()
        self.__waitBusy()
         #       s f f 
         # Must ensure that the data written within the address range is 0xFF, otherwise the data written in non-0xFF will fail!
         # Have an automatic page function 
         # Terate the data to the specified length in the specified address, but to make sure the address is not crossing!
         # PBuffer: Data Store
         # WriteAddr: Add address (24bit)
         # NumByTetowrite: Number of bytes to write (maximum 65535)
    # CHECK OK
         # Wait idle
    def __writeNoCheck(self, buff, addr, num):
        pageremain = 256- addr%256
        if(num <= pageremain): pageremain = num
        while True:
            self.__writePage(buff, addr, pageremain)
            if(num == pageremain): break
            else:
                buff = buff[pageremain:]
                gc.collect()
                addr += pageremain
                num -= pageremain
                if num > 256: pageremain = 256
                else: pageremain = num 
         #   s f f  
         #              
         # This function with erase operation!
         # PBuffer: Data Store
         # WriteAddr: Add address (24bit)						
         # NumByTetowrite: Number of bytes to write (maximum 65535)  
    def write(self, buff, addr, num):
        buff_tmp = None
        secpos = addr // 4096
        secoff = addr % 4096
        secremain = 4096 - secoff
        if num <= secremain:
            secremain = num
        while True:
#             print("...")
            buff_tmp = bytearray(self.read(secpos * 4096, 4096))
            if sum (map(lambda x: x^0xFF, buff_tmp[secoff:])): # Need to erase # ration: # Need to erase
                self.__eraseSector(secpos)
                for i in range(0, secremain):
                    buff_tmp[i + secoff] = buff[i]
                self.__writeNoCheck(buff_tmp, secpos * 4096, 4096)
            else:
                self.__writeNoCheck(buff, secpos * 4096, 4096)
            if num == secremain:
                break # End of Write
            else:
                secpos += 1
                secoff = 0
                buff = buff[secremain:]
                addr += secremain
                if num > 4096: secremain = 4096
                else:
                    secremain = num
            gc.collect()
    
         # Erase the entire chip		  
         # Waiting time is long ...
    def eraseChip(self):
        self.__writeEnable()
        self.__waitBusy()
        self.__CS_PIN.off()
        self.__SPI.write(bytearray([W25X_ChipErase]))
        self.__CS_PIN.on()
        self.__waitBusy()
 
         # Erase a sector
         # DST_ADDR: The sector address is set according to the actual capacity
         #    : 150ms
    def __eraseSector(self, addr):
#         print("erase sector : {0:}".format(addr))
        addr *= 4096
        self.__writeEnable()
        self.__waitBusy()
        self.__CS_PIN.off()
        self.__SPI.write(bytearray([W25X_SectorErase, (addr>>16)&0xff, (addr>>8)&0xff, addr&0xff]))
        self.__CS_PIN.on()
        self.__waitBusy()
         # Wait idle
    def __waitBusy(self):
        while True:
            if self.__readSR()&0x01 == 0x01:
                time.sleep_ms(5)
            else: break
 
#block defice interface
class W25QXX_BlockDev(__W25QXX):
    def __init__(self, SPI, CS_PIN):
        self.block_size = 4096
        super().__init__(SPI, CS_PIN)
        super().read(0,1)
        # self.data = bytearray(block_size * num_blocks)
 
    def readblocks(self, block_num, buf):
        buf_tmp = self.read(block_num * self.block_size, len(buf))
        for i in range(len(buf)):
            buf[i] = buf_tmp[i]
 
    def writeblocks(self, block_num, buff):
        self.write(buff, block_num * self.block_size, len(buff))
 
    def ioctl(self, op, arg):
        if op == 4: # get number of blocks
            return self.__MEM // self.block_size
        if op == 5: # get block size
            return self.block_size

import network
import utime
import ubinascii
import gc

__sta=None

def connectWifi(ssid, pwd):
  global __sta
  if __sta is None:
    __sta=network.WLAN(network.STA_IF)
    __sta.active(True)    
    __sta.connect(ssid, pwd)
    print('Connecting to WiFi STA ...')
    utime.sleep(8)
  if __sta.isconnected():
    print('Connected: {} : {}.'.format(ssid, __sta.ifconfig()[0]))
  else:
    print('{} connect failure!'.format(ssid))
    return None

def scanAP():
  global __sta
  if __sta is None:
    __sta=network.WLAN(network.STA_IF)
  __sta.active(True)
  aps=__sta.scan()
  for ap in aps:
    ssid=ap[0].decode()
    mac=ubinascii.hexlify(ap[1], ':').decode()
    rssi=str(ap[3])+'dBm'
    print('{:>20} {:>20} {:>10}'.format(ssid, mac, rssi))

def getIP():
  global __sta
  if __sta is None:
    print("Not connect yet!")
  else:
    return __sta.ifconfig()

def df(dir='/'):
  from os import statvfs
  s=statvfs(dir)
  print((s[0]*s[3]) / 1048576,'MB') 

connectWifi("dickykohk", "vecxu-rjgax-znsry")
gc.collect()
print("---------------------------------------")
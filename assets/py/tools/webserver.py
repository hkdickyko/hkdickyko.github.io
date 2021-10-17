try:
  import usocket as socket
except:
  import socket
import ujson
import gc
import utime

class webserver:
    
  def __init__(self,port):
    self.__html=None
    self.__jSonStr=None
    self.__webserver=None
    self.__callback=None
    self.__webserver=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.__webserver.bind(('', port))
    self.__webserver.listen(5)
    self.__conn=None
 
  def html_color(self,ID,rgb):
    strValue="."+ID+"{background-color:"
    pt0=self.__html.find(strValue)+len(strValue)
    pt1=self.__html.find(";}",pt0)
    self.__html=self.__html[:pt0]+rgb + self.__html[pt1:]
 
  def html_text(self,ID,txt):
    strValue=" id=\""+ID+"\">"
    pt0=self.__html.find(strValue)+len(strValue)
    pt1=self.__html.find("</",pt0)
    self.__html=self.__html[:pt0]+txt + self.__html[pt1:]
    
  def html_update(self):
    self.__conn.send('HTTP/1.1 200 OK\n')
    self.__conn.send('Content-Type: text/html\n')
    self.__conn.send('Connection: close\n\n')
    self.__conn.sendall(self.__html)
    self.__conn.close()
 
  def html_page(self,filename):
    if self.__html is None:
      f=open(filename)
      self.__html=f.read()
      f.close()

  def callback(self,pCallback):
    self.__callback=pCallback;

  def loop(self):
    response="Error!"
    while True:
      self.__conn,addr=self.__webserver.accept()
      if not self.__html is None:
        response=self.__html
      request=self.__conn.recv(1024)
      request=str(request)
      pt0=request.find("{")
      pt1=request.find("}",pt0)+1
      if pt0 < 10:
        self.__jSonStr=request[pt0:pt1]
        if self.__jSonStr.find("{")==0:
          self.__jSonStr=self.urldecode(self.__jSonStr)
          parsed=ujson.loads(self.__jSonStr) 
          self.updateStatus(parsed)
        else:
          self.html_update()
      else:
        self.html_update()
      gc.collect()
      
  def urldecode(self,strV): 
    dic={"%21":"!","%22":'"',"%23":"#","%24":"$","%26":"&","%27":"\"","%28":"(","%29":")","%2A":"*","%2B":"+","%2C":",","%2F":"/","%3A":":","%3B":";","%3D":"=","%3F":"?","%40":"@","%5B":"[","%5D":"]","%7B":"{","%7D":"}"}
    for k,v in dic.items():
      strV=strV.replace(k,v)
    return strV

  def updateStatus(self,jlist):
    if not self.__callback is None:
      self.__callback(jlist)
    else:
      print("callback not set!")
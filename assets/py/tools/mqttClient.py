import utime
import gc
from lib.umqtt.simple2 import MQTTClient as _MQTTClient

class mqttClient:
    
  def __init__(self,IP,ID): 
    self._IP=IP
    self._ID=ID
    self._user="MQTT_User"
    self._pwd="MQTT_password"
    self._port=1883
    self._qos=1
    self._timeout=3
    self._client=None
    self._callback=None;

  def connection(self,user,password,Port,qos,timeout):
    self._user=user
    self._pwd=password
    self._port=Port
    self._qos=qos
    self._timeout=timeout

  def callback(self,callback):
    self._callback=callback
     
  def _sub_callback(self,topic,msg,retained,dup):
    if not self._callback is None:
      self._callback(topic.decode('ascii'),msg.decode('ascii'))
    else:
      print('TOPIC: {},  MSG: {}'.format(topic.decode('ascii'),msg.decode('ascii')))

  def publish(self,topic,message):
    self._client.publish(topic,message,qos=self._qos)
    for i in range(self._timeout):
      utime.sleep_ms(10)

  def subscribe(self,topic):
    self._client.subscribe(topic)
    for i in range(self._timeout):
      utime.sleep(1)
      self._client.check_msg()

  def connect(self):
    self._client= _MQTTClient(self._ID,self._IP,port=self._port,user=self._user,password=self._pwd)
    self._client.set_callback(self._sub_callback)
    self._client.connect()
    print("MQTT Conneted")

  def disconnect(self):
    self._client.disconnect()
    gc.collect()
    print("MQTT disconneted.")
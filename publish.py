import paho.mqtt.client as paho
from randomcoordinate import initial
from randomcoordinate import movement

x,y,z = initial()
a = 0
c = paho.Client()
c.connect("127.0.0.1", 1883)

while a < 500:
   x,y,z = movement(x,y,z)
   c.publish("test",x)
   a = a+1

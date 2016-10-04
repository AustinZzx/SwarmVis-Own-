import paho.mqtt.client as paho
from randomcoordinate import initial
from randomcoordinate import movement
from signal import signal, SIGPIPE, SIG_DFL

def rbtpublish():
   signal(SIGPIPE, SIG_DFL)
   b = 0
   c = paho.Client()
   c.connect("127.0.0.1", 1883)

   num = int(raw_input("Enter the number of robots you want to see: "))

   while b < num:
      x,y,z = initial()
      a = 0
      while a < 500:
         x,y,z = movement(x,y,z)
         c.publish("robot%i" %b,str(x)+" "+str(y)+" "+str(z))
         a = a+1
      b = b+1
      
rbtpublish()

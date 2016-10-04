import paho.mqtt.client as paho
from randomcoordinate import initial
from randomcoordinate import movement
from signal import signal, SIGPIPE, SIG_DFL
import time

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
    
def rbtpublish(num):
   signal(SIGPIPE, SIG_DFL)
   b = 0
   c = paho.Client()
   c.on_publish = on_publish
   c.connect("127.0.0.1", 1883)
   c.loop_start()  
   while b < num:
      x,y,z = initial()
      a = 0
      while a < 30:
         x,y,z = movement(x,y,z)
         (rc, mid) =c.publish("robot%i" %(b+1),str(x)+" "+str(y)+" "+ \
                    str(z))
         a = a+1
      b = b+1
   time.sleep(1)
      
      
num = int(raw_input("Enter the number of robots you want to see: "))
rbtpublish(num)

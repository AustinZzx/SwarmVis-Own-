import paho.mqtt.client as paho
from randomcoordinate import initial
from randomcoordinate import movement
#from signal import signal, SIGPIPE, SIG_DFL

c = paho.Client()                 #must declare a global client variable
 
def on_publish(client, userdata, mid):
    print("mid: "+str(mid))               #print out the mids
    
def pubinit():
   #signal(SIGPIPE, SIG_DFL)       #to prevent a signal error
   c.on_publish = on_publish
   c.connect("neptune.usc.edu", 1883)
   c.loop_start()
   
def simplepublish(topic, data):
   pubinit()
   (rc, mid) =c.publish(topic, data)      #publish once
   c.loop_stop()
      

def rbtpublish(num):                     #a sample simulation with
   pubinit()                             #random numbers 
   b = 0
   while b < num:
      x,y,z = initial()
      a = 0
      while a < 50:
         x,y,z = movement(x,y,z)
         (rc, mid) =c.publish("robot%i" %(b+1),str(x)+" "+str(y)+" "+
                    str(z))
         a = a+1
      b = b+1
   c.loop_stop()
   




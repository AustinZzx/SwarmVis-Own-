import paho.mqtt.client as paho
from randomcoordinate import initial
from randomcoordinate import movement
import time
import thread

c = paho.Client()                 #must declare a global client variable
 
def on_publish(client, userdata, mid):
    print("mid: "+str(mid))               #print out the mids
    
def pubinit():
   c.on_publish = on_publish
   c.connect("neptune.usc.edu", 1883)
   c.loop_start()
   
def simplepublish(topic, data):         #publish one position with a partivular topic
   pubinit()
   (rc, mid) =c.publish(topic, data)      
   c.loop_stop()
      
"""
def rbtpublish(num):                     #a sample simulation with num robots
   pubinit()                             #50 random positions for each robot
   b = 0
   while a < 100:
      x,y,z = initial()
      a = 0
      while b < num:
		time.sleep(.5)
		x,y,z = movement(x,y,z)
		(rc, mid) =c.publish("robot%i" %(b+1),str(x)+" "+str(y)+" "+str(z))
		b = b+1
      a = a+1
   c.loop_stop()
   """
   
def rbtpublishseperate(threadName, topic):           #continuously publish random positions for one robot
	pubinit()
	x,y,z = initial()
	while 1:
		time.sleep(.5)
		x,y,z = movement(x,y,z)
		(rc, mid) =c.publish(topic,str(x)+" "+str(y)+" "+str(z))
	
   




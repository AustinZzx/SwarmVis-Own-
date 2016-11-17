import paho.mqtt.client as paho
from construct import *
csub = paho.Client()

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
 
def on_message(client, userdata, msg):
	global status
    #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))    
	print(msg.topic+" "+" "+str(msg.payload))  
	if str(msg.payload) == "end":
		csub.disconnect()
		status = 0
	elif msg.topic=="robot1":            #read objects from string
		vectors = str(msg.payload).split()
		#drone1.rotate()
		drone1.f.pos = (float(vectors[0]),float(vectors[1]),float(vectors[2]))
	elif msg.topic=="robot2":
		vectors = str(msg.payload).split()
		car1.pos = (float(vectors[0]),float(vectors[1]),float(vectors[2]))
	elif msg.topic=="robot3":
		vectors = str(msg.payload).split()
		#drone1.rotate()
		drone2.f.pos = (float(vectors[0]),float(vectors[1]),float(vectors[2]))
	elif msg.topic=="robot4":
		vectors = str(msg.payload).split()
		car2.pos = (float(vectors[0]),float(vectors[1]),float(vectors[2]))
      
def subinit():
   csub.connect("neptune.usc.edu", 1883)
   csub.on_subscribe = on_subscribe
   csub.on_message = on_message

 
   
def simplesubscribe(topic, qos):
   subinit()
   csub.subscribe(topic, qos)
   csub.loop_forever()
   
def rbtsubscribe(num):
   subinit()
   d = 0
   while d < num:
      csub.subscribe("robot%i" %(d+1), qos = 1)
      d = d+1
   csub.loop_start()
   
num = int(raw_input("Enter the number of robots you want to see: "))
create_coordinate(20)
drone1 = Drone()  
drone1.f.pos = (0,0,0)      #initialize a drone
car1 = create_robot()
car1.pos = (0,0,0)          #initializa a car
drone2 = Drone()
drone2.f.pos = (0,0,0)  
car2 = create_robot()
car2.pos = (0,0,0)
rbtsubscribe(num)

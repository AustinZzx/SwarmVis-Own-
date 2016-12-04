import paho.mqtt.client as paho         #nose unit test
from construct import *

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
 
def on_message(client, userdata, msg):
    global carnum
    global dronenum
    global carlist
    global dronelist
    #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))    
    print(msg.topic+" "+" "+str(msg.payload))  
    if str(msg.payload) == "end":
        csub.disconnect()
    elif msg.topic=="subscribe":
        vectors = str(msg.payload).split()
        csub.subscribe(vectors[0], 0)
        if vectors[1]=="car":
            carnum = carnum + 1
            rbt=Car(vectors[0])
            rbt.f.pos = (0,0,0)
            carlist.append(rbt)
        if vectors[1]=="drone":
            dronenum = dronenum + 1
            rbt=Drone(vectors[0])
            rbt.f.pos = (0,0,0)
            dronelist.append(rbt)
    else:
        vectors = str(msg.payload).split()
        for i in range(0,carnum):
            if carlist[i].topic == msg.topic:       
                carlist[i].f.pos = (float(vectors[0]),float(vectors[1]),float(vectors[2]))
        for i in range(0,dronenum):
            if dronelist[i].topic == msg.topic:
                dronelist[i].f.pos = (float(vectors[0]),float(vectors[1]),float(vectors[2]))        
      
def subinit():
    csub.connect("neptune.usc.edu", 1883)
    csub.on_subscribe = on_subscribe
    csub.on_message = on_message
    global carnum
    global dronenum
    global carlist
    global dronelist
    carnum = dronenum = 0
    carlist = []
    dronelist = []
    create_coordinate(20)

 
   
def simplesubscribe(topic, qos):
    csub.subscribe(topic, qos)
    csub.loop_start()
   
def rbtsubscribe(num):
    d = 0
    while d < num:
        csub.subscribe("robot%i" %(d+1), qos = 0)
        d = d+1
    csub.loop_start()

csub = paho.Client()
subinit()
simplesubscribe("subscribe",1)

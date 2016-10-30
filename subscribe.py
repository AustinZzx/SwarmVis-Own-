import paho.mqtt.client as paho

csub = paho.Client()
message = []


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
 
def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))    
    print(msg.topic+" "+" "+str(msg.payload))  
    if str(msg.payload) == "end":
      csub.disconnect()
    else:
      message.append(str(msg.payload))
      
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
   csub.loop_forever()
   
   

num = int(raw_input("Enter the number of robots you want to see: "))

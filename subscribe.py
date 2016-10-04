import paho.mqtt.client as paho

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
 
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))    
 
def rbtsubscribe(num):
   csub = paho.Client()
   csub.connect("127.0.0.1", 1883)
   csub.on_subscribe = on_subscribe
   csub.on_message = on_message
   d = 0
   while d < num:
      csub.subscribe("robot%i" %(d+1), qos = 1)
      d = d+1
   csub.loop_forever()
   
   
   
num = int(raw_input("Enter the number of robots you want to see: "))
rbtsubscribe(num)

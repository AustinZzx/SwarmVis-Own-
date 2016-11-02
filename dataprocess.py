from subscribe import rbtsubscribe
from subscribe import message
from subscribe import num
import numpy as np

rbtsubscribe(num)
k = len(message)
print k

#rbt1x = []
#rbt1y = []
#rbt1z = []
rbt1 = np.array([]).reshape(0,3)
rbt2 = np.array([]).reshape(0,3)
rbt3 = np.array([]).reshape(0,3)

def slicerbtmsg():
	for coordinates in message[0:(k/num)]:
		vectors = coordinates.split()
		global rbt1
   #rbt1x.append(float(vectors[0]))
   #rbt1y.append(float(vectors[1]))
   #rbt1z.append(float(vectors[2]))
		rbt1 = np.vstack([rbt1, [float(vectors[0]),float(vectors[1]),float(vectors[2])]])
	for coordinates in message[(k/num):(2*k/num)]:
		vectors = coordinates.split()
		global rbt2
		rbt2 = np.vstack([rbt2, [float(vectors[0]),float(vectors[1]),float(vectors[2])]])
	for coordinates in message[(2*k/num):(3*k/num)]:
		vectors = coordinates.split()
		global rbt3
		rbt3 = np.vstack([rbt3, [float(vectors[0]),float(vectors[1]),float(vectors[2])]])	
		
slicerbtmsg()
print "robot1: "
print rbt1
print "robot2: "
print rbt2   
print "robot3: "
print rbt3   
#print rbt1x
#print rbt1y
#print rbt1z

from subscribe import rbtsubscribe
from subscribe import message
from subscribe import num
import numpy as np

rbtsubscribe(num)
k = len(message)
print k


rbt1 = np.array([]).reshape(0,3)
rbt2 = np.array([]).reshape(0,3)
rbt3 = np.array([]).reshape(0,3)
rbt4 = np.array([]).reshape(0,3)
rbt5 = np.array([]).reshape(0,3)
rbt6 = np.array([]).reshape(0,3)

def slicerbtmsg():
	for coordinates in message[0:(k/num)]:
		vectors = coordinates.split()
		global rbt1
		rbt1 = np.vstack([rbt1, [float(vectors[0]),float(vectors[1]),float(vectors[2])]])
	for coordinates in message[(k/num):(2*k/num)]:
		vectors = coordinates.split()
		global rbt2
		rbt2 = np.vstack([rbt2, [float(vectors[0]),float(vectors[1]),float(vectors[2])]])
	for coordinates in message[(2*k/num):(3*k/num)]:
		vectors = coordinates.split()
		global rbt3
		rbt3 = np.vstack([rbt3, [float(vectors[0]),float(vectors[1]),float(vectors[2])]])	
	for coordinates in message[(3*k/num):(4*k/num)]:
		vectors = coordinates.split()
		global rbt4
		rbt4 = np.vstack([rbt4, [float(vectors[0]),float(vectors[1]),float(vectors[2])]])
	for coordinates in message[(4*k/num):(5*k/num)]:
		vectors = coordinates.split()
		global rbt5
		rbt5 = np.vstack([rbt5, [float(vectors[0]),float(vectors[1]),float(vectors[2])]])
	for coordinates in message[(5*k/num):(6*k/num)]:
		vectors = coordinates.split()
		global rbt6
		rbt6 = np.vstack([rbt6, [float(vectors[0]),float(vectors[1]),float(vectors[2])]])
		
slicerbtmsg()
"""
print "robot1: "
print rbt1
print "robot2: "
print rbt2   
print "robot3: "
print rbt3   
print "robot4: "
print rbt4   
"""
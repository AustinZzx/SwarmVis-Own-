from newsubscribe import rbtsubscribe
from newsubscribe import message
from newsubscribe import num

rbtsubscribe(num)
k = len(message)
print k

rbt1x = []
rbt1y = []
rbt1z = []

for coordinates in message[0:(k/num)]:
   vectors = coordinates.split()
   rbt1x.append(float(vectors[0]))
   rbt1y.append(float(vectors[1]))
   rbt1z.append(float(vectors[2]))
print rbt1x
print rbt1y
print rbt1z

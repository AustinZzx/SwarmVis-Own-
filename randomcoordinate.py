import random

def initial():
   BUZZ = 2.0
   a = 0;
   x = random.gauss(0.0, BUZZ)
   y = random.gauss(0.0, BUZZ)
   z = random.gauss(0.0, BUZZ)
   return (x,y,z)
 
def movement(x,y,z):
   dx = random.triangular(-1.0, 1.0, 0)
   dy = random.triangular(-1.0, 1.0, 0)
   dz = random.triangular(-1.0, 1.0, 0)
   x += dx
   y += dy
   z += dz
   return (x,y,z)
     

def test():
   a = 0
   k = int(raw_input("enter how many moves you want: "))
   x,y,z = initial()
   while a<k:
      x,y,z = movement(x,y,z)
      print x,y,z
      a=a+1
   

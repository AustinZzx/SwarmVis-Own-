from visual import *
import numpy as np
from dataprocess import *
from construct import *
'''
use vpython to create a demo
control balls moving in 3D
python 2.7.10
refernce:
http://vpython.org/

'''
print """
Right button drag or Ctrl-drag to rotate "camera" to view scene.
Middle button or Alt-drag to drag up or down to zoom in or out.
  On a two-button mouse, middle is left + right.
"""

create_coordinate(20)
drone1 = Drone()
drone2 = Drone()
drone3 = Drone()
robot1 = create_robot()
robot2 = create_robot()
robot3 = create_robot()
# positions contain the coordination of balls at different time
# they should be read from files but here just to play a demo 
position1 = rbt1
position2 = rbt2
position3 = rbt3
position4 = rbt4
position5 = rbt5
position6 = rbt6
# here we set two balls start and end together
# each visit will change the position of balls
for i,j,k,l,m,n in zip(position1,position2,position3,position4,position5,position6):
	rate(7)
	# rate controls the time to loop through
	drone1.f.pos = i
	drone1.rotate()
	drone2.f.pos = j
	drone2.rotate()
	drone3.f.pos = k
	drone3.rotate()
	robot1.pos = l
	robot2.pos = m
	robot3.pos = n

print "Complete!"



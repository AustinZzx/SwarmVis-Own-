from visual import *
import numpy as np
from dataprocess import rbt1, rbt2, rbt3
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

# we will create four balls
# ball_center stands still
# ball1 and ball2 and ball3 to move

ball_center = sphere(color = color.green, radius = 0.08)

# define a coordinate system to compare
X0 = arrow(pos=(0,0,0), axis=(10,0,0), color=color.white, shaftwidth=0.03)
Y0 = arrow(pos=(0,0,0), axis=(0,10,0), color=color.white, shaftwidth=0.03)
Z0 = arrow(pos=(0,0,0), axis=(0,0,10), color=color.white, shaftwidth=0.03)

ball1 = sphere (color = color.red, radius = 0.2,make_trail = True, retain=5)
	# retain: the time of trail to retain
ball1.trail_object.radius = 0.02
ball1.trail_object.color = color.red
	#you can also set the radius and colr of trail

ball2 = sphere (color = (0.34,0.63,0.9), radius = 0.2,make_trail = True, retain=5)
ball2.trail_object.radius = 0.02

ball3 = sphere (color = color.yellow, radius = 0.2,make_trail = True, retain=5)
ball3.trail_object.radius = 0.02
ball3.trail_object.color = color.yellow
# positions contain the coordination of balls at different time
# they should be read from files but here just to play a demo 
position1 = rbt1
position2 = rbt2
position3 = rbt3
# here we set two balls start and end together
# each visit will change the position of balls
for i,j,k in zip(position1,position2,position3):
	rate(3)
	# rate controls the time to loop through
	ball1.pos = i
	ball2.pos = j
	ball3.pos = k

print "Complete!"



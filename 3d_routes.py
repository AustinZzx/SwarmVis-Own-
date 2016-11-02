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

#ball_center = sphere(color = color.green, radius = 0.08)

# define a coordinate system to compare
X0 = arrow(pos=(0,0,0), axis=(20,0,0), color=color.blue, shaftwidth=0.05)
Y0 = arrow(pos=(0,0,0), axis=(0,20,0), color=color.blue, shaftwidth=0.05)
Z0 = arrow(pos=(0,0,-0), axis=(0,0,20), color=color.blue, shaftwidth=0.05)
X0neg = arrow(pos=(-20,0,0), axis=(20,0,0), color=color.white, shaftwidth=0.05)
Y0neg = arrow(pos=(0,-20,0), axis=(0,20,0), color=color.white, shaftwidth=0.05)
Z0neg = arrow(pos=(0,0,-20), axis=(0,0,20), color=color.white, shaftwidth=0.05)

f1 = frame(make_trail = True,retain=5)    # retain: the time of trail to retain
f1.trail_object.radius = 0.02
f1.trail_object.color = color.red
ball1 = sphere(frame=f1, color = color.red, material=materials.silver, radius = 0.5,pos = (1,0,0))
box1 = box(frame=f1,color = color.red,material=materials.silver,length=1, height=1,width=1.5)
ring1 = ring(frame=f1,color = color.white,material=materials.silver,pos=(0,0,0), axis=(0,1,0), radius=1.2, thickness=0.1)

ball2 = sphere (color = color.green, material=materials.silver, radius = 0.2,make_trail = True, retain=5)
ball2.trail_object.radius = 0.02
ball2.trail_object.color = color.green

ball3 = sphere (color = color.yellow, material=materials.silver, radius = 0.2,make_trail = True, retain=5)
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
	f1.pos = i
	ball2.pos = j
	ball3.pos = k

print "Complete!"



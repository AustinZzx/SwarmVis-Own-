from visual import *
import numpy as np

def create_coordinate(length):
    X0 = arrow(pos=(0,0,0), axis=(length,0,0), color=color.red, shaftwidth=0.05)
    Y0 = arrow(pos=(0,0,0), axis=(0,length,0), color=color.red, shaftwidth=0.05)
    Z0 = arrow(pos=(0,0,-0), axis=(0,0,length), color=color.red, shaftwidth=0.05)
    X0neg = arrow(pos=((0-length),0,0), axis=(length,0,0), color=color.red, shaftwidth=0.05)
    Y0neg = arrow(pos=(0,(0-length),0), axis=(0,length,0), color=color.red, shaftwidth=0.05)
    Z0neg = arrow(pos=(0,0,(0-length)), axis=(0,0,length), color=color.red, shaftwidth=0.05)
    xtext = text(text='x', pos=(length+1,0,0), align='center', depth=-0.3, color=color.red)
    ytext = text(text='y', pos=(0,length+1,0), align='center', depth=-0.3, color=color.red)
    ztext = text(text='z', pos=(0,0,length+1), align='center', depth=-0.3, color=color.red)
    
class Drone:

    def __init__(self, topic):
        self.topic = topic
        self.f = frame(make_trail = False,retain=5) 
        self.f.trail_object.radius = 0.05
        self.f.trail_object.color = color.white
        self.ell = ellipsoid(frame=self.f, pos=(0,0,0),color = color.white, material=materials.plastic,length=1.6, height=0.4, width=0.4)
        self.ring1 = ring(frame=self.f,color = color.white,material=materials.plastic,pos=(-0.6,0.4,0), axis=(0,0,1), radius=0.4, thickness=0.08)
        self.ring2 = ring(frame=self.f,color = color.white,material=materials.plastic,pos=(0.6,0.4,0), axis=(0,0,1), radius=0.4, thickness=0.08)
        self.ring3 = ring(frame=self.f,color = color.white,material=materials.plastic,pos=(0.6,-0.4,0), axis=(0,0,1), radius=0.4, thickness=0.08)
        self.ring3 = ring(frame=self.f,color = color.white,material=materials.plastic,pos=(-0.6,-0.4,0), axis=(0,0,1), radius=0.4, thickness=0.08)
        self.rod1 = cylinder(frame=self.f,pos=(-0.3,0.11,0), color = color.white,material=materials.plastic, axis=(-0.3,0.29,0), radius=0.04)
        self.rod2 = cylinder(frame=self.f,pos=(0.3,0.11,0), color = color.white,material=materials.plastic, axis=(0.3,0.29,0), radius=0.04)
        self.rod3 = cylinder(frame=self.f,pos=(0.3,-0.11,0), color = color.white,material=materials.plastic, axis=(0.3,-0.29,0), radius=0.04)
        self.rod4 = cylinder(frame=self.f,pos=(-0.3,-0.11,0), color = color.white,material=materials.plastic, axis=(-0.3,-0.29,0), radius=0.04)
        self.roll1 = box(frame=self.f,pos=(-0.6,0.4,0), color = color.white,material=materials.plastic,length=0.6,height=0.08,width=0.05, axis=(1,0,0), radius=0.04)
        self.roll2 = box(frame=self.f,pos=(0.6,0.4,0), color = color.white,material=materials.plastic,length=0.6,height=0.08,width=0.05, axis=(1,0,0), radius=0.04)
        self.roll3 = box(frame=self.f,pos=(0.6,-0.4,0), color = color.white,material=materials.plastic,length=0.6,height=0.08,width=0.05, axis=(1,0,0), radius=0.04)
        self.roll4 = box(frame=self.f,pos=(-0.6,-0.4,0), color = color.white,material=materials.plastic,length=0.6,height=0.08,width=0.05, axis=(1,0,0), radius=0.04)
        
    def rotate(self):
        i = 0
        while i<30:
            rate(500000)
            self.roll1.rotate(angle=pi/16, axis=(0,0,1), origin=self.roll1.pos)
            self.roll2.rotate(angle=pi/16, axis=(0,0,1), origin=self.roll2.pos)
            self.roll3.rotate(angle=pi/16, axis=(0,0,1), origin=self.roll3.pos)
            self.roll4.rotate(angle=pi/16, axis=(0,0,1), origin=self.roll4.pos)
            i=i+1
    
class Car:

    def __init__(self, topic):
        self.topic = topic
        self.f = frame(make_trail = False,retain=5) 
        self.f.trail_object.radius = 0.05
        self.f.trail_object.color = color.white
        self.lower_board = box(frame=self.f, pos=(0,0,0),color = color.white, material=materials.plastic,length=1.4, height=0.7, width=0.05)
        self.upper_board = box(frame=self.f, pos=(0.35,0,0.4),color = color.white, material=materials.plastic,length=0.7, height=0.7, width=0.05)
        self.battery = box(frame=self.f, pos=(-0.35,0,0.325),color = color.white, material=materials.plastic,length=0.7, height=0.7, width=0.2)
        self.pillar1 = cylinder(frame=self.f,pos=(0.6,0.3,0), color = color.white,material=materials.plastic, axis=(0,0,0.4), radius=0.03)
        self.pillar2 = cylinder(frame=self.f,pos=(0.6,-0.3,0), color = color.white,material=materials.plastic, axis=(0,0,0.4), radius=0.03)
        self.pillar3 = cylinder(frame=self.f,pos=(-0.6,0.3,0), color = color.white,material=materials.plastic, axis=(0,0,0.4), radius=0.03)
        self.pillar4 = cylinder(frame=self.f,pos=(-0.6,-0.3,0), color = color.white,material=materials.plastic, axis=(0,0,0.4), radius=0.03)
        self.pillar5 = cylinder(frame=self.f,pos=(-0.1,0.3,0), color = color.white,material=materials.plastic, axis=(0,0,0.4), radius=0.03)
        self.pillar6 = cylinder(frame=self.f,pos=(-0.1,-0.3,0), color = color.white,material=materials.plastic, axis=(0,0,0.4), radius=0.03)
        self.connection1 = cylinder(frame=self.f,pos=(0.6,0.5,0.1), color = color.white,material=materials.plastic, axis=(0,-1,0), radius=0.03)
        self.connection2 = cylinder(frame=self.f,pos=(-0.6,0.5,0.1), color = color.white,material=materials.plastic, axis=(0,-1,0), radius=0.03)
        self.tyre1 = ring(frame=self.f,color = color.white,material=materials.plastic,pos=(0.6,0.5,0.1), axis=(0,-1,0), radius=0.2, thickness=0.04)
        self.tyre2 = ring(frame=self.f,color = color.white,material=materials.plastic,pos=(-0.6,0.5,0.1), axis=(0,-1,0), radius=0.2, thickness=0.04)
        self.tyre3 = ring(frame=self.f,color = color.white,material=materials.plastic,pos=(0.6,-0.5,0.1), axis=(0,-1,0), radius=0.2, thickness=0.04)
        self.tyre4 = ring(frame=self.f,color = color.white,material=materials.plastic,pos=(-0.6,-0.5,0.1), axis=(0,-1,0), radius=0.2, thickness=0.04)
        self.rod1 = cylinder(frame=self.f,color = color.white,material=materials.plastic,pos=(0.4,0.5,0.1), axis=(0.4,0,0),radius=0.02)
        self.rod2 = cylinder(frame=self.f,color = color.white,material=materials.plastic,pos=(0.4,0.5,0.1), axis=(0.4,0,0),radius=0.02)
        self.rod3 = cylinder(frame=self.f,color = color.white,material=materials.plastic,pos=(0.4,0.5,0.1), axis=(0.4,0,0),radius=0.02)
        self.rod4 = cylinder(frame=self.f,color = color.white,material=materials.plastic,pos=(0.4,0.5,0.1), axis=(0.4,0,0),radius=0.02)
        self.rod2 = self.rod2.rotate(angle=pi/4, axis=(0,1,0), origin=(0.6,0.5,0.1))
        self.rod3 = self.rod3.rotate(angle=pi/2, axis=(0,1,0), origin=(0.6,0.5,0.1))
        self.rod4 = self.rod4.rotate(angle=3*pi/4, axis=(0,1,0), origin=(0.6,0.5,0.1))
        self.rod5 = cylinder(frame=self.f,color = color.white,material=materials.plastic,pos=(-0.4,0.5,0.1), axis=(-0.4,0,0),radius=0.02)
        self.rod6 = cylinder(frame=self.f,color = color.white,material=materials.plastic,pos=(-0.4,0.5,0.1), axis=(-0.4,0,0),radius=0.02)
        self.rod7 = cylinder(frame=self.f,color = color.white,material=materials.plastic,pos=(-0.4,0.5,0.1), axis=(-0.4,0,0),radius=0.02)
        self.rod8 = cylinder(frame=self.f,color = color.white,material=materials.plastic,pos=(-0.4,0.5,0.1), axis=(-0.4,0,0),radius=0.02)
        self.rod6 = self.rod6.rotate(angle=pi/4, axis=(0,1,0), origin=(-0.6,0.5,0.1))
        self.rod7 = self.rod7.rotate(angle=pi/2, axis=(0,1,0), origin=(-0.6,0.5,0.1))
        self.rod8 = self.rod8.rotate(angle=3*pi/4, axis=(0,1,0), origin=(-0.6,0.5,0.1))
        self.rod9 = cylinder(frame=self.f,color = color.white,material=materials.plastic,pos=(0.4,-0.5,0.1), axis=(0.4,0,0),radius=0.02)
        self.rod10 = cylinder(frame=self.f,color = color.white,material=materials.plastic,pos=(0.4,-0.5,0.1), axis=(0.4,0,0),radius=0.02)
        self.rod11 = cylinder(frame=self.f,color = color.white,material=materials.plastic,pos=(0.4,-0.5,0.1), axis=(0.4,0,0),radius=0.02)
        self.rod12 = cylinder(frame=self.f,color = color.white,material=materials.plastic,pos=(0.4,-0.5,0.1), axis=(0.4,0,0),radius=0.02)
        self.rod10 = self.rod10.rotate(angle=pi/4, axis=(0,1,0), origin=(0.6,-0.5,0.1))
        self.rod11 = self.rod11.rotate(angle=pi/2, axis=(0,1,0), origin=(0.6,-0.5,0.1))
        self.rod12 = self.rod12.rotate(angle=3*pi/4, axis=(0,1,0), origin=(0.6,-0.5,0.1))
        self.rod13 = cylinder(frame=self.f,color = color.white,material=materials.plastic,pos=(-0.4,-0.5,0.1), axis=(-0.4,0,0),radius=0.02)
        self.rod14 = cylinder(frame=self.f,color = color.white,material=materials.plastic,pos=(-0.4,-0.5,0.1), axis=(-0.4,0,0),radius=0.02)
        self.rod15 = cylinder(frame=self.f,color = color.white,material=materials.plastic,pos=(-0.4,-0.5,0.1), axis=(-0.4,0,0),radius=0.02)
        self.rod16 = cylinder(frame=self.f,color = color.white,material=materials.plastic,pos=(-0.4,-0.5,0.1), axis=(-0.4,0,0),radius=0.02)
        self.rod14 = self.rod14.rotate(angle=pi/4, axis=(0,1,0), origin=(-0.6,-0.5,0.1))
        self.rod15 = self.rod15.rotate(angle=pi/2, axis=(0,1,0), origin=(-0.6,-0.5,0.1))
        self.rod16 = self.rod16.rotate(angle=3*pi/4, axis=(0,1,0), origin=(-0.6,-0.5,0.1))

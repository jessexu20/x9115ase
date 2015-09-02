from swampy.TurtleWorld import *
import math
def triangle(t,angle,l):
    arc=angle*math.pi/180
    edge= 2*l*math.sin(arc/2)
    fd(t,l)
    lt(t,90+angle/2)
    fd(t,edge)
    lt(t,90+angle/2)
    fd(t,l)
def drawTriangle(n):
    world = TurtleWorld()
    bob = Turtle()
    # bob.delay=0.0001
    for i in range(n):
        rt(bob,180)
        triangle(bob,360.0/n,50)
    wait_for_user()
drawTriangle(7)
from swampy.TurtleWorld import *
from math import pi
def square(t,length):
    for i in range(4):
        fd(t,length)
        lt(t)
def polygon(t,length,n):
    """Draws a polygon with n sides.
    t: Turtle
    n: sides number
    length: each side's length.
    """
    for i in range(n):
        fd(t,length)
        lt(t,360/n)
def arc(t,r,n):
    """Draws a arc with radius r, degree n.
    t: Turtle
    r: radius
    n: degree
    """
    arc_length = 2 * pi * r * abs(n) / 360
    length= arc_length/n
    for i in range(n):
        fd(t,length)
        lt(t,1)
def arc_r(t,r,n):
    """Draws a arc with radius r, degree n.
    t: Turtle
    r: radius
    n: degree
    """
    arc_length = 2 * pi * r * abs(n) / 360
    length= arc_length/n
    for i in range(n):
        fd(t,length)
        rt(t,1)
def circle(t,r):
    """Draws a circle with radius r.
    t: Turtle
    r: radius
    """
    arc(t,r,360)
def petal(t,r,d):
    for i in range(2):
        arc(t,r,d)
        lt(t,180-d)
    
def drawSquare():
    world = TurtleWorld()
    bob = Turtle()
    square(bob,i)
    wait_for_user()
def drawPolygon(n):
    world = TurtleWorld()
    bob = Turtle()
    polygon(bob,50,n)
    wait_for_user()
def drawCircle(r):
    world = TurtleWorld()
    bob = Turtle()
    bob.delay=0.0001
    circle(bob,r)
    wait_for_user()
def drawPartialCircle(l,angle):
    world = TurtleWorld()
    bob = Turtle()
    bob.delay=0.0001
    arc(bob,l,angle)
    wait_for_user()
def drawFlower(n):
    world = TurtleWorld()
    bob = Turtle()
    bob.delay=0.0001
    for i in range(1,n+1):
        petal(bob,200,360/n)
        lt(bob,360/n)
    wait_for_user()
# drawSquare()
# drawPolygon(5)
# drawCircle(50)
# drawPartialCircle(50,90)
drawFlower(20)
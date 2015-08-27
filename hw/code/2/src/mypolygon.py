from swampy.TurtleWorld import *

def square(t,length):
    print t
    for i in range(4):
        fd(t,length)
        lt(t)
    wait_for_user()
def polygon(t,length,n):
    print t
    for i in range(n):
        fd(t,length)
        lt(t,360/n)
    wait_for_user()
def arc(t,length,n):
    print t
    for i in range(n):
        fd(t,length)
        lt(t,1)
    wait_for_user()
def drawSquare():
    world = TurtleWorld()
    bob = Turtle()
    square(bob,i)

def drawPolygon(n):
    world = TurtleWorld()
    bob = Turtle()
    polygon(bob,50,n) 
def drawCircle(l):
    world = TurtleWorld()
    bob = Turtle()
    bob.delay=0.01
    polygon(bob,l,360)
def drawPartialCircle(l,angle):
    world = TurtleWorld()
    bob = Turtle()
    bob.delay=0.01
    arc(bob,l,angle)
# drawSquare()
# drawPolygon(5)
# drawCircle(2)
drawPartialCircle(1,90)
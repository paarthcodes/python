from turtle import *

penup()
goto(0,-200)
def squares():
    backward(25)
    pendown()
    for i in range(4):
        forward(50)
        left(90)
    penup()
    forward(25)
    left(90)
    forward(50)
    
def circles():
    right(90)
    pendown()
    circle(25)
    penup()
    left(90)
    forward(50)
    
for i in range(4):
    seth(0)
    squares()
    circles()
    
penup()
seth(0)
backward(25)
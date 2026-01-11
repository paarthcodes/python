from turtle import *

circle(50)
penup()
goto(-100,-200)
for i in range(3):
    pendown()
    circle(50)
    penup()
    forward(100)
goto(-50,-100)
for i in range(2):
    pendown()
    circle(50)
    penup()
    forward(100)
goto(0,0)
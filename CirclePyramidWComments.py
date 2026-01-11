from turtle import *

"""
This program creates 6 circles in a pyramid starting from the bottom and goes up. It has many circles and creates a nices pyramid.
"""

penup()
#Bottom row
goto(-100,-200)
for i in range(3):
    pendown()
    circle(50)
    penup()
    forward(100)
#Middle Row
goto(-50,-100)
for i in range(2):
    pendown()
    circle(50)
    penup()
    forward(100)
#Top Cricle
penup()
goto(0,0)
pendown()
circle(50)
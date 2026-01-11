from turtle import *

pensize(5)
penup()
backward(100)
pendown()

color("red")
forward(200)
penup()
backward(200)
pendown()

for i in range(4):
    left(60)
    color("green")
    forward(50)
    right(120)
    color("blue")
    forward(50)
    left(60)
    
color("green")
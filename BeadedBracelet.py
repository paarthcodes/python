from turtle import *

speed(0)
penup()
goto(0,-110)
def beaded_bracelet():
    pendown()
    circle(10)
    penup()
    forward(20)
    left(10)
for i in range(36):
    beaded_bracelet()
goto(0,0)
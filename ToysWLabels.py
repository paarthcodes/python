from turtle import *

speed(10)
bgcolor("tan")
penup()
goto(-200,-200)

pendown()
for i in range(4):
    forward(400)
    left(90)
   
def square():
    penup()
    goto(-100,50)
    pendown()
    color("red")
    begin_fill()
    circle(60,360,4)
    end_fill()
    penup()
    goto(-100,30)
    write("Red Square", font=("Arial", 12), align="center")

def circles():
    penup()
    goto(100,50)
    pendown()
    color("blue")
    begin_fill()
    circle(60)
    end_fill()
    penup()
    goto(100,30)
    write("Blue Circle", font=("Arial", 12), align="center")

def semi_circle():
    penup()
    goto(-125,-150)
    pendown()
    color("yellow")
    begin_fill()
    circle(60,180)
    end_fill()
    penup()
    goto(-105,-165)
    write("Yellow Semicircle", font=("Arial", 12), align="center")


def pentagon():
    penup()
    goto(100,-150)
    seth(0)
    pendown()
    color("green")
    begin_fill()
    circle(60,360,5)
    end_fill()
    penup()
    goto(100,-165)
    write("Green Pentagon", font=("Arial", 12), align="center")
   

square()
circles()
semi_circle()
pentagon()
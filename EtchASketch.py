from turtle import *

#Defines Speed
speed(0)

#A Block
penup()
goto(-175,175)
pendown()
for i in range(3):
    forward(350)
    right(90)
forward(350)
penup()

#B Block
goto(-150,150)
pendown()
for i in range (4):
    right(90)
    forward(300)
    right(90)
    forward(250)
penup()

#Dial C
goto(-150,-135)
pendown()
right(180)
circle(25)
penup()

#Dial D
goto(150,-135)
pendown()
right(180)
circle(25)
penup()

#Triangle E
goto(-165,-135)
pendown()
goto(-155,-130)
goto(-155,-140)
goto(-165,-135)
penup()

#Triangle F
goto(-85,-135)
pendown()
goto(-95,-130)
goto(-95,-140)
goto(-85,-135)
penup()

#Triangle G
goto(85,-130)
pendown()
goto(90,-140)
goto(95,-130)
goto(85,-130)
penup()

#Triangle H
goto(155,-140)
pendown()
goto(160,-130)
goto(165,-140)
goto(155,-140)

#Back to Starting Position
penup()
goto(0,0)
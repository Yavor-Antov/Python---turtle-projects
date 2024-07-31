from turtle import *

bgcolor('black')
pencolor('green')
penup()
goto(0, 200)
a = 0
b = 0
speed(0)
pendown()
while b != 210:
    fd(a)
    rt(b)
    a += 3
    b += 1

exitonclick()
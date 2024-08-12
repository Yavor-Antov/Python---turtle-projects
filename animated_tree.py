import turtle as t
from numpy import angle

t.title("Yavors' Tree animation")
t.setworldcoordinates(-2000, -2000, 2000, 2000)
screen = t.Screen()
screen.tracer(0, 0)  # Disable automatic screen updates
t.speed(0)  # Set the turtle speed to the fastest
t.hideturtle()

def yavor_tree(x, y, length, tilt, angle, n):
    if n == 0:
        return
    t.up()
    t.goto(x, y)
    t.seth(tilt)
    t.down()
    t.fd(length)
    yavor_tree(t.xcor(), t.ycor(), length / 2, t.heading(), angle, n - 1)

    t.up()
    t.goto(x, y)
    t.seth(tilt + angle)
    t.down()
    t.fd(length)
    yavor_tree(t.xcor(), t.ycor(), length / 2, t.heading(), angle, n - 1)

    t.up()
    t.goto(x, y)
    t.seth(tilt - angle)
    t.down()
    t.fd(length)
    yavor_tree(t.xcor(), t.ycor(), length / 2, t.heading(), angle, n - 1)

def animation():
    global angle
    t.clear()
    yavor_tree(0, -250, 1000, 90, angle, 7)
    screen.update()
    angle = 120 if angle <= 20 else angle - 2
    screen.ontimer(animation, 30)  # Reduce the interval time

angle = 120
animation()
screen.mainloop()
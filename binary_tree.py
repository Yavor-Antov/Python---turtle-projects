import turtle
a = turtle.Turtle()

def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t)
        t.left(40)
        tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)

a.left(90)
a.up()
a.backward(100)
a.down()
a.color("green")
tree(75, a)
turtle.done()
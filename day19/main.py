import turtle
screen = turtle.Screen()
myrtle = turtle.Turtle()


def move_forward():
    myrtle.forward(10)


def move_back():
    myrtle.forward(-10)


def clock():
    myrtle.right(5)


def counter():
    myrtle.left(5)


def re():
    myrtle.reset()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_back, "s")
screen.onkey(counter, "a")
screen.onkey(clock, "d")
screen.onkey(re, "c")
screen.exitonclick()

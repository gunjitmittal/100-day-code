import turtle
from random import choice, randint
import colorgram


def move_right():
    myrtle.right(90)
    myrtle.forward(20)


def move_left():
    myrtle.left(90)
    myrtle.forward(20)


def move_back():
    myrtle.right(180)
    myrtle.forward(20)


# colors = colorgram.extract('/Users/Shared/d/100-day-code/day18/download.jpeg', 30)
# color_list = [(color.rgb[0], color.rgb[1], color.rgb[2])for color in colors]
# print(color_list)
myrtle = turtle.Turtle()
turtle.colormode(255)
myrtle.shape("arrow")
myrtle.speed(0)
myrtle.color("cyan")
myrtle.hideturtle()
myrtle.penup()
myrtle.setx(-300)
myrtle.sety(-300)
ix = myrtle.xcor()
iy = myrtle.ycor()
colors = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]
for i in range(20):
    myrtle.sety(iy+i*30)
    for j in range(20):
        myrtle.setx(ix+j*30)
        myrtle.color(choice(colors))
        myrtle.pendown()
        myrtle.dot(20)
        myrtle.penup()
screen = turtle.Screen()
screen.exitonclick()

import turtle

screen = turtle.Screen()
screen.setup(height=400, width=500)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
print(bet)
t = []
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
for i in range(6):
    t.append(turtle.Turtle(shape="turtle"))
    t[i].penup()
    t[i].color(colors[i])
    t[i].goto(-230, -100+40*i)

screen.exitonclick()

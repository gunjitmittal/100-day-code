# import turtle
from prettytable import PrettyTable
# my_screen = turtle.Screen()
# jimmy = turtle.Turtle()
# jimmy.color("blue")
# jimmy.shape("turtle")
# jimmy.forward(100)
# print(my_screen.canvheight)
# my_screen.exitonclick()
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)

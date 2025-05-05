from turtle import  Turtle
import random

tinny=Turtle()
winny=Turtle()

colours=[
    "red", "blue", "green",  "black",   "purple",
      "cyan", "magenta", "gold", "silver", "navy",
    "turquoise", "lime", "maroon", "olive", "teal", "skyblue", "coral",
    "salmon", "orchid", "plum", "chocolate", "tan", "indigo", "violet",
     "lavender"]

def shape(no_of_sides):
    angle=360/no_of_sides
    for i in range(no_of_sides):
        tinny.forward(100)
        tinny.right(angle)
        winny.forward(100)
        winny.left(angle)

for shapeofno in range(3,11):
    tinny.color(random.choice(colours))
    winny.color(random.choice(colours))
    shape(shapeofno)
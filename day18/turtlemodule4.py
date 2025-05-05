# from turtle import Turtle
import turtle
# import turtle as t
import random


tinny=turtle.Turtle()
turtle.colormode(255)


def randcolor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    randcolor=(r,g,b)
    return randcolor

direction=[0,98,188,270]
tinny.pensize(15)
tinny.speed("fastest")

for _ in range(200):
    tinny.color(randcolor())
    tinny.forward(30)
    tinny.setheading(random.choice(direction))

    # tinny=Screen()
    # tinny.exitonclick()
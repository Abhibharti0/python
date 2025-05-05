from turtle import Turtle,Screen
tinny=Turtle()

for _ in range(20):
    tinny.pendown()
    tinny.forward(10)
    tinny.penup()
    tinny.forward(10)


screen=Screen()
screen.exitonclick()
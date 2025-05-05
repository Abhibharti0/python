from turtle import Turtle ,Screen

tinny=Turtle()
tinny.shape("turtle")
tinny.color("blue")
def step():
    tinny.forward(100)
    tinny.left(90)
step()
step()
step()
step()



screen=Screen()
screen.exitonclick()
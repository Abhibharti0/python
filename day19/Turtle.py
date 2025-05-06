#moving turtle using keyboard
from turtle import Turtle, Screen

tinny=Turtle()
screen=Screen()

def move_forwards():
    tinny.forward(10)

def move_backwards():
    tinny.backward(10)

def move_left():
    new_heading=tinny.heading()+10
    tinny.setheading(new_heading)

def move_right():
   new_heading=tinny.heading()-10
   tinny.setheading(new_heading)
def clear():
    tinny.clear()
    tinny.penup()
    tinny.home()
    tinny.pendown()

screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
screen.onkey(move_left,"a")
screen.onkey(move_right,"d")
screen.onkey(clear,"c")
screen.exitonclick()
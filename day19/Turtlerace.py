from turtle import Turtle, Screen
import random

screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="which turtle will win the race?\nRed,Black,Blue,Green,darkorange!Enter a color")

colors=["Red","Black","Blue","Green","darkorange"]
y_post=[50,25,0,-25,-50]
all_turltle=[]



for i in range(0,5):
    tinny=Turtle(shape="turtle")
    tinny.color(colors[i])
    tinny.penup()
    tinny.goto(x=-235,y=y_post[i])
    all_turltle.append(tinny)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turltle:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color == user_bet:
                print(tinny.write(f"You've won! The {winning_color} turtle is the winner.",
                             align="right", font=("Arial", 14, "bold")))
            else:    
                print(tinny.write(f"You've lost! The {winning_color} turtle is the winner.",
                             align="right", font=("Arial", 14, "bold")))

        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
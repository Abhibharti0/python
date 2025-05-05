import turtle as t
import random


tinny=t.Turtle()
t.colormode(255)


def rancolor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color

tinny.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tinny.color(rancolor())
        tinny.circle(100)
        tinny.setheading(tinny.heading()+size_of_gap)

draw_spirograph(5)
# for _ in range(200):
#     tinny.color(random_color())

tinny=t.Screen()
tinny.exitonclick()
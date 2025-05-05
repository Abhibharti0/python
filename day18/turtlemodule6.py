# import colorgram

# rgb_colors=[]
# colors=colorgram.extract('D:/study drive/python/day18/image.png',20)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as t
import random

t.colormode(255)
tinny=t.Turtle()
tinny.speed("fastest")
tinny.penup()

color_list=[(245, 243, 239), (246, 240, 242), (205, 165, 107), (152, 72, 48), (235, 238, 243), (238, 243, 238), (165, 151, 44), (225, 202, 133), (55, 94, 127), (131, 33, 24), (134, 163, 182), (48, 120, 90), (201, 91, 71), (15, 99, 73), (148, 178, 149), (68, 48, 41), (165, 143, 155), (112, 74, 78), (234, 176, 166), (53, 46, 48)]

tinny.setheading(225)
tinny.forward(300)
tinny.setheading(0)
tinny.hideturtle()
number_of_dot=100

for i in range(1,number_of_dot+1):
    tinny.dot(20,random.choice(color_list))
    # tinny.penup()
    tinny.forward(50)

    if i%10==0:
        tinny.setheading(90)
        tinny.forward(50)
        tinny.setheading(180)
        tinny.forward(500)
        tinny.setheading(0)

screen=t.Screen()
screen.exitonclick()
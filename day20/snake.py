from turtle import Turtle

Starting_position=[(0,0),(-20,0),(-40,0)]
Up=90
Down=270
Left=180
Right=0

move_distance=20
class Snake:

    def __init__(self):
        self.all_turltle=[]
        self.create_snake()
        self.head=self.all_turltle[0]
        
    def create_snake(self):
        for position in  Starting_position:
            self.add_turtle(position)

    def add_turtle(self,position):
        tinny=Turtle()
        tinny.shape("square")
        tinny.color("white")
        tinny.penup()
        tinny.goto(position)
        self.all_turltle.append(tinny)

    def extented(self):
        self.add_turtle(self.all_turltle[-1].position())

    def move(self):
        for seg_num in range (len(self.all_turltle)-1,0,-1):
            new_x=self.all_turltle[seg_num-1].xcor()
            new_y=self.all_turltle[seg_num-1].ycor()
            self.all_turltle[seg_num].goto(new_x,new_y)
        self.head.forward(move_distance)


    def up(self):
        if self.head.heading() !=Down:
            self.head.setheading(Up)

    def down(self):
        if self.head.heading() !=Up:
          self.head.setheading(Down)

    def left(self):
        if self.head.heading() !=Right:
          self.head.setheading(Left)

    def right(self):
        if self.head.heading() !=Left:
            self.head.setheading(Right)
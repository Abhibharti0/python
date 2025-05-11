from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food)<15:
            food.refresh()
            snake.extented()
            scoreboard.increase_score()

        if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
            game_is_on=False
            scoreboard.game_over()

        for i in snake.all_turltle[1:]:
            if  snake.head.distance(i) < 10:
                game_is_on=False
                scoreboard.game_over()
    


screen.exitonclick()    

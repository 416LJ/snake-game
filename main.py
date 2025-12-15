from turtle import Screen
import time

from scoreboard import Scoreboard
from snake import Snake
from food import Food

# Screen setup
screen = Screen()
screen.setup(width=600,height=650)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    if snake.head.distance(food) < 15:
        score.score += 1
        food.refresh()
        snake.extend()
        score.scoreboard()
    if not snake.check_margins():
        score.final_score()
        game_is_on = False

    for bit in snake.the_snake[1:]:
        if snake.head.distance(bit) < 10:
            game_is_on = False
            score.final_score()

screen.exitonclick()
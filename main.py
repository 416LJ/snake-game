from turtle import Screen
import time
from snake import Snake

# Screen setup
screen = Screen()
screen.setup(width=650,height=650)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    # fix the refresh rate
    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.check_margins():
        continue
    else:
        game_is_on = False

screen.exitonclick()
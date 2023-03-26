from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

snake = Snake()

screen.onkey(snake.up,"Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    
    snake.move()

screen.exitonclick()
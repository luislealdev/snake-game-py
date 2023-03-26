from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

segments = []

for turtle_index in range(3):
    new_turtle = Turtle()
    new_turtle.color("white")
    new_turtle.shape("square")

    new_turtle.penup()
    new_turtle.goto(-(turtle_index*20),0)
    segments.append(new_turtle)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)

    for seg_num in range(len(segments)-1, 0, -1):
        snake_position = segments[seg_num - 1].position()
        segments[seg_num].goto(snake_position)
    segments[0].forward(20)
    segments[0].left(90)

screen.exitonclick()
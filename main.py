from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")

turtle_list = []

for turtle_index in range(3):
    new_turtle = Turtle()
    new_turtle.color("white")
    new_turtle.shape("square")

    new_turtle.penup()
    new_turtle.goto(-(turtle_index*20),0)
    turtle_list.append(new_turtle)



screen.exitonclick()
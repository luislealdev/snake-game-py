from turtle import Turtle

# Constants
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake():

    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

    def createSnake(self):
        for turtle_index in range(3):
            new_turtle = Turtle()
            new_turtle.color("white")
            new_turtle.shape("square")

            new_turtle.penup()
            new_turtle.goto(-(turtle_index*20),0)
            self.segments.append(new_turtle)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            snake_position = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(snake_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)   
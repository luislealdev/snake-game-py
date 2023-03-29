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
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def reset(self):
        for segment in self.segments:
            segment.reset()
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]
        self.head.goto(0,0)
        

    def add_segment(self, position):
        new_turtle = Turtle()
        new_turtle.color("white")
        new_turtle.shape("square")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

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
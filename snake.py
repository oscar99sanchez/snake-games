from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (0, -20), (0, -40)]

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles [0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segmet(position)

    def add_segmet(self, position):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.turtles.append(turtle)

    def extend(self):
        self.add_segmet(self.turtles[-1].position())

    def reset(self):
        for seg in self.turtles:
            seg.goto(1000, 1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]

    def up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].setheading(90)

    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)

    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)

    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)

    def move(self):
        for seg_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[seg_num - 1].xcor()
            new_y = self.turtles[seg_num - 1].ycor()
            self.turtles[seg_num].goto(new_x, new_y)
        self.turtles[0].forward(20)


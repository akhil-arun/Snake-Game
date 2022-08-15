from turtle import Turtle


class Snake:

    def __init__(self):
        #starting_x = -40
        self.segments = []
        for i in range(3):
            self.add_segment((0 + (-20 * i), 0))
        
       
    
    def add_segment(self, position):
        part = Turtle("square")
        part.color("white")
        part.pu()
        part.goto(position)
        self.segments.append(part)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto((new_x, new_y))

    # self.segments[0] is the head of the snake    
        self.segments[0].forward(20)
    
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)











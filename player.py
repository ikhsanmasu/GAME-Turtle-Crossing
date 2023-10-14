from turtle import Turtle

class Crosser(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.shapesize(1)
        self.setheading(90)
        self.goto_start()

    def move(self):
        self.forward(20)

    def goto_start(self):
        self.goto((0, -260))
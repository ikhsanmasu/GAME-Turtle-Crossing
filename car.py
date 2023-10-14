from turtle import Turtle

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        # self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.setheading(180)

    def move(self):
        self.forward(10)

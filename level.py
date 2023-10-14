from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.penup()
        self.hideturtle()
        self.goto((-380, 270))
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level {self.current_level}", align="left", font=("Arial", 15, "normal"))

    def increase(self):
        self.current_level += 1
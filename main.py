from turtle import Screen, Turtle
from player import Crosser
from time import sleep
from cars_manager import carsManager
from random import randint
from level import Level

screen = Screen()
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)
screen.colormode(255)

level = Level()

player = Crosser()
screen.onkey(player.move, "Up")

def game_over():
    start_again = Turtle()
    start_again.penup()
    start_again.hideturtle()
    start_again.color("red")
    start_again.write("       GAME OVER\nClick anywhere to exit", align="center", font=("Arial", 20, "normal"))

cars_manager = carsManager()
game_is_on = True
while game_is_on:
    try:
        cars_manager.move()
        chance = randint(0, 20 - level.current_level)

        if chance == 0:
            cars_manager.add_car()

        if player.ycor() > 320:
            player.goto_start()
            level.increase()
            level.update()
            cars_manager.increase_speed()

        for car in cars_manager.cars:
            if player.distance(car) < 40 and player.ycor() == car.ycor():
                game_over()
                game_is_on = False

        screen.update()
        sleep(0.1)
    except:
        pass

screen.exitonclick()
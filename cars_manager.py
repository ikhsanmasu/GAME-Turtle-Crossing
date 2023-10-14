from car import Car
from random import choice, randint

class carsManager:
    def __init__(self):
        self.cars = []
        self.speed = 5
        self.position = [y for y in range(-200, 240, 20)]
        self.add_car()

    def add_car(self):
        new_car = Car()
        new_car.goto((450, choice(self.position)))
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        new_car.color((r, g, b))
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)
            if car.xcor() < -450:
                self.cars.remove(car)

    def increase_speed(self):
        self.speed += 1
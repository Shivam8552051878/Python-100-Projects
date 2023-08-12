from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.x_pos = 300
        self.y_pos = random.randint(-240, 240)

    def create_car(self):
        car = Turtle()
        car.penup()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.shapesize(stretch_len=2)
        self.y_pos = random.randint(-240, 240)
        car.goto(self.x_pos, self.y_pos)
        self.cars.append(car)

    def create_random_car(self):
        for i in range(0, random.randint(0, 5)):
            self.create_car()

    def x_increase(self):
        self.x_pos = self.x_pos - random.randint(5, 10)

    def move(self):
        for car in self.cars:
            car.goto(self.x_pos, self.y_pos)

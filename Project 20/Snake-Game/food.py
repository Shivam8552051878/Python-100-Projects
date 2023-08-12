from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("blue")
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.random_food()

    def random_food(self):
        self.hideturtle()
        xcor = random.randint(-250, 250)
        ycor = random.randint(-250, 250)
        self.goto(xcor, ycor)
        self.showturtle()


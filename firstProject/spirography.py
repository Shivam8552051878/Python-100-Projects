import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
tim.color("red")

screen = Screen()
screen.colormode()
screen.colormode(255)

direction = [0, 90, 180, 270]


def changeColor(tim):
    red = round(random.random() * 255)
    blue = round(random.random() * 255)
    green = round(random.random() * 255)
    tim.color(red, blue, green)


direction_count = 0
tim.speed(0)
print(tim.speed())
while direction_count != 360:
    changeColor(tim)
    tim.circle(100)
    tim.setheading(direction_count)
    direction_count += 10


screen.exitonclick()

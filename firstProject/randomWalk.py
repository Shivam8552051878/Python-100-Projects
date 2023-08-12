from turtle import Turtle, Screen
import random

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


def walk_random(how, dist=20):
    for i in range(how):
        changeColor(tim)
        tim.setheading(random.choice(direction))
        tim.forward(dist)

tim.width(5)
walk_random(50,30)
# tim.circle(100,extent=50,steps=2)

screen.exitonclick()
print(screen.mode())

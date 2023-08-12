import random
from turtle import Turtle, Screen


DOT_SIZE = 15

tim = Turtle()
tim.penup()
tim.shape("turtle")
tim.hideturtle()
screen = Screen()
screen.colormode()
screen.colormode(255)

direction = [0, 90, 180, 270]
print(screen.colormode())

def changeColor():
    red = round(random.random() * 255)
    blue = round(random.random() * 255)
    green = round(random.random() * 255)
    return (red,blue,green)



def move_start(tim):
    tim.goto(-275,-270)



def move_left(tim):
    tim.dot(DOT_SIZE,changeColor())
    tim.left(90)
    tim.forward(30)
    tim.left(90)

def move_right(tim):
    tim.dot(DOT_SIZE,changeColor())
    tim.right(90)
    tim.forward(30)
    tim.right(90)


move_start(tim)
for i in range(20):
    status = 0
    while status <= 10:
        tim.dot(DOT_SIZE,changeColor())
        tim.forward(50)
        status += 1
    if i % 2 == 0:
        move_left(tim)
    else:
        move_right(tim)
    status = 0

tim.showturtle()
screen.exitonclick()
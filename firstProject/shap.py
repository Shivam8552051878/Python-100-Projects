from turtle import Turtle,Screen
import random
tim = Turtle()
tim.shape("arrow")
tim.color("red")


screen = Screen()
screen.colormode()
screen.colormode(255)

def makeShape(start,end):
    for i in range(start, end):
        red = round(random.random() * 255)
        blue = round(random.random() * 255)
        green = round(random.random() * 255)
        tim.color((red, green, blue))

        count = 0
        while count != i:
            tim.forward(100)
            tim.right(360 / i)

            count += 1
        count = 0
makeShape(3,10)
screen.exitonclick()

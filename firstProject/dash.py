from turtle import Turtle,Screen

tim = Turtle()
tim.shape("arrow")
for i in range(30):
    tim.forward(3)
    tim.penup()
    tim.forward(3)
    tim.pendown()




screen = Screen()
screen.exitonclick()

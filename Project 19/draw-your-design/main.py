import turtle

tim = turtle.Turtle()
screen = turtle.Screen()

def move_forword():
    return tim.forward(10)


def move_backwar():
    return tim.back(10)

def turnleft():
    newHead = tim.heading() + 10
    return tim.setheading(newHead)

def turnRight():
    newHead = tim.heading() - 10
    return tim.setheading(newHead)


def clearScreen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkeypress(move_forword, key="space")
screen.onkeypress(move_backwar, key="b")
screen.onkeypress(turnleft, key="l")
screen.onkeypress(turnRight, key="r")
screen.onkeypress(clearScreen, key="c")

screen.exitonclick()
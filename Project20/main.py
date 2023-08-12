import turtle
import random


SCORE = 0
SNAKE_LENGTH = 1



screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.listen()


snake = turtle.Turtle(shape="square")
snake.penup()
snake.resizemode()


food = turtle.Turtle(shape="circle")
food.penup()
food.color("blue")
food.shapesize(stretch_len=0.5,stretch_wid=0.5)


def move_food_random():
    xcor = random.randint(-300, 300)
    ycor = random.randint(-300, 300)
    food.goto(xcor, ycor)


def tEast():
    if  snake.heading() != 180:
        snake.setheading(0)


def tNorth():
    if snake.heading() != 270:
        snake.setheading(90)


def tWest():
    if snake.heading() != 0:
        snake.setheading(180)


def tSouth():
    if snake.heading() != 270:
        snake.setheading(270)


def forWord():
    snake.forward(10)


game_over = False

snake.goto(-20.00, 0.00)
print(food.distance, snake.distance)

while not game_over:
    snake.forward(2)
    if snake.xcor() < -280 or snake.xcor() > 280 or snake.ycor() < -280 or snake.ycor() > 280:
        game_over = True

    if food.position() == snake.position():
       # game_over = True
        SNAKE_LENGTH += SNAKE_LENGTH
        snake.shapesize(stretch_len=SNAKE_LENGTH)
        SCORE += 1
        move_food_random()


    if snake.distance(food) < 15:
        # game_over = True
        SNAKE_LENGTH += SNAKE_LENGTH
        snake.shapesize(stretch_len=SNAKE_LENGTH)
        SCORE += 1
        move_food_random()

    screen.onkeypress(tEast, "Right")
    screen.onkeypress(tWest, "Left")
    screen.onkeypress(tNorth, "Up")
    screen.onkeypress(tSouth, "Down")
    screen.onkeypress(forWord, "space")

screen.exitonclick()

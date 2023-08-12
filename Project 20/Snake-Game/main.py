from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time




screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.x_cor() < -270 or snake.x_cor() > 270 or snake.y_cor() < -270 or snake.y_cor() > 270:
        # print("Colide")
        scoreboard.game_over()
        game_is_on = False


    if snake.head.distance(food) < 15:
        snake.extend()
        food.random_food()
        scoreboard.show_score()

    if snake.collision():
        game_is_on = False
        scoreboard.game_over()



screen.exitonclick()
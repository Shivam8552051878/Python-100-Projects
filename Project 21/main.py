from turtle import Turtle,Screen

from ball import Ball
from paddle import MakePaddle
from scoreboard import ScoreBoard

from time import sleep


screen = Screen()


screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PANGA")
screen.listen()
screen.tracer(0)

border = Turtle()
border.color("white")
border.penup()
border.hideturtle()
border.goto(0, 300)
border.right(90)
border.width(3)




while border.ycor() > -300:
    border.pendown()
    border.forward(10)
    border.penup()
    border.forward(10)

ball = Ball()

# border.showturtle()

l_paddle = MakePaddle(-350)
r_paddle = MakePaddle(350)
scoreboard = ScoreBoard()
screen.update()
screen.tracer(1)
# screen.update()

screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")


game_over = False
while not game_over:
    sleep(ball.move_speed)

    ball.move()
    if ball.xcor() > 390 or ball.xcor() < -390:
        print(ball.xcor())
        if ball.xcor() < 300:
            print(f"left paddle{l_paddle.score}")
            scoreboard.l_score += 1
            scoreboard.print_score()

        else:
            print(f"right paddle: {r_paddle.score}")
            scoreboard.r_score += 1
            scoreboard.print_score()

        ball.reset_postion()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.change_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() > -340:
        ball.change_x()












screen.exitonclick()

import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player1 = Player()
screen.onkeypress(player1.move, "Up")

scoreBoard = Scoreboard()

game_is_on = True

cars_list = []
count = 0
while game_is_on:
    time.sleep(0.1)
    scoreBoard.display()
    screen.update()
    if count % 6 == 0:
        cars = CarManager()
        cars.create_random_car()
        cars_list.append(cars)
        count = 0
    for car in cars_list:
        car.x_increase()
        car.move()
        for cr in car.cars:
            if cr.distance(player1) < 20:
                scoreBoard.game_over()
                game_is_on = False

    count += 1

    if player1.finishLine():
        scoreBoard.score_up()

screen.exitonclick()

from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-220, 260)
        self.display()

    def display(self):
        self.clear()
        self.write(f"Level: {self.score}", False, "center", FONT)

    def score_up(self):
        self.score += 1
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, "center", FONT)

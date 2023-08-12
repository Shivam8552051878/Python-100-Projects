from turtle import Turtle

ALIGHNMENT = "center"
FONT = ('Arial', 15, 'bold')
MOVE = False


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.score = 0
        self.penup()
        self.color("red")
        self.shape("square")
        self.show_score()


    def show_score(self):
        self.clear()
        self.write(arg=f"Your Score is: {self.score}", move=MOVE, align=ALIGHNMENT, font= FONT)
        self.score += 1

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"Game Over", move=MOVE, align=ALIGHNMENT, font=FONT)


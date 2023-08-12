from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.width(5)
        self.l_score = 0
        self.r_score = 0
        self.print_score()



    def print_score(self):
        self.clear()
        self.goto(-100, 220)
        self.write(str(self.l_score), "center", font=('Arial', 50, 'bold'))
        self.goto(100, 220)
        self.write(str(self.r_score), "center", font=('Arial',50, 'bold'))
from turtle import Turtle


class MakePaddle(Turtle):
    def __init__(self,angle):
        super().__init__(shape="square")
        self.penup()
        self.color("white")
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.right(90)
        self.x_value = angle
        self.goto(self.x_value,0)
        self.score = 0

    def move_up(self):
        if self.ycor() < 240:
            self.backward(10)

    def move_down(self):
        if self.ycor() > -240:
            self.forward(10)




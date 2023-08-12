from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.turtlesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.1




    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)



    def change_y(self):
        self.y_move *= -1

    def change_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_postion(self):
        self.home()
        self.change_x()
        self.move_speed = 0.1



from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.right(270)
        self.y_move = MOVE_DISTANCE
        self.speed_move = 0.9


    def move(self):
        new_y_pos = self.ycor() + self.y_move
        return self.goto(self.xcor(), new_y_pos)

    def finishLine(self):
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.speed_move *= 0.9
            return True






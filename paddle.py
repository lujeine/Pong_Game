from turtle import *


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)

    def go_up(self):
        if self.ycor() < 230:
            self.goto(self.xcor(), self.ycor() + 30)

    def go_down(self):
        if self.ycor() > -220:
            self.goto(self.xcor(), self.ycor() - 30)

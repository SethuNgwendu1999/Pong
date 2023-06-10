from turtle import Turtle
WIDTH = -240
FORWARD = 35
add = 15
sub = 15


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.paddle = []
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.resizemode("paddle1")
        self.shapesize(5, 1, 1)


    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), y=new_y)

from turtle import Turtle


class Ball(Turtle):
    pos_x = 5
    pos_y = 5

    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(x=0, y=0)
        self.y_move = 10
        self.x_move = 10
        self.quicker = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_ball(self):
        self.y_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.quicker *= 0.9


    def reset_ball(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.quicker = 0.1









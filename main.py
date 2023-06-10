from turtle import Screen
from paddle import Paddle
from ball import Ball
from Scoreboard import Scoreboard
import time

s = Screen()
l = Paddle((-350, 0))
r = Paddle((350, 0))
b = Ball()
sc = Scoreboard()

s.setup(width=800, height=600)
s.bgcolor("black")
s.title("Pong Game")
s.tracer(0)
s.listen()
s.onkey(r.up, "w")
s.onkey(r.down, "s")
s.onkey(l.up, "Up")
s.onkey(l.down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(b.quicker)
    s.update()

    # moves ball
    b.move_ball()

    # ball bounce from top and bottom wall
    if b.ycor() > 280 or b.ycor() < -280:
        b.bounce_ball()

    if b.distance(r) < 50 and b.xcor() > 320 or b.distance(l) < 50 and b.xcor() < -320:
        b.bounce_x()

    if b.xcor() == 400:
        b.reset_ball()
        sc.l_point()
        sc.clear()
        sc.update_scoreboard()

    if b.xcor() == -400:
        b.reset_ball()
        sc.r_point()
        sc.clear()
        sc.update_scoreboard()



s.exitonclick()

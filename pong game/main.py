from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreborad import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()
scoreborad = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if abs(ball.ycor()) > 270:
        ball.y_bounce()

    if ball.distance(r_paddle) < 30 or ball.distance(l_paddle) < 30:
        ball.x_bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreborad.increasing_l_score()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreborad.increasing_r_score()

screen.exitonclick()



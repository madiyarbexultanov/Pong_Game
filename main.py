from turtle import  Screen
from paddle import  Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


left_paddle = Paddle((-380, 0))
right_paddle = Paddle((380, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detecting collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x_r_paddle()

    # Detecting collision with left paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x_l_paddle()


    # Detecting collision with outbounds
    if ball.xcor() > 380:
        ball.new_game()
        scoreboard.l_counter()


    if ball.xcor() < -380:
        ball.new_game()
        scoreboard.r_counter()


screen.exitonclick()
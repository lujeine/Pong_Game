from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

game_is_on = True

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

right_p = Paddle(350, 0)
left_p = Paddle(-350, 0)

ball = Ball()

scoreboard = Scoreboard()

middle_line = Turtle()
middle_line.goto(0, 0)
middle_line.shape("square")
middle_line.color("white")
middle_line.shapesize(stretch_wid=25, stretch_len=0.08)

screen.listen()
screen.onkey(right_p.go_up, "Up")
screen.onkey(right_p.go_down, "Down")
screen.onkey(left_p.go_up, "w")
screen.onkey(left_p.go_down, "s")


while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if (ball.xcor() > 320 and ball.distance(right_p) < 50) or (ball.xcor() < -320 and ball.distance(left_p) < 50):
        ball.bounce_x()

    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.update_score1()

    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.update_score2()

screen.exitonclick()

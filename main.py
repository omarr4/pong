import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

USER_XCOR = -375
PC_XCOR = 367

screen = Screen()
screen.setup(width=800, height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

paddle_left = Paddle(USER_XCOR)
paddle_right = Paddle(PC_XCOR)
ball = Ball()
scoreboard = Scoreboard()

last_paddled = paddle_left

screen.onkeypress(fun=paddle_left.move_up, key="Up")
screen.onkeypress(fun=paddle_left.move_down, key="Down")
screen.onkeypress(fun=paddle_right.move_up, key="w")
screen.onkeypress(fun=paddle_right.move_down, key="s")

current = time.time_ns()
last = 0
while True:
    last = current
    current = time.time_ns()
    time_elapsed = current - last
    delta_time = time_elapsed / 10 ** 9
    screen.update()
    ball.move(delta_time)
    # Detect collision with wall
    if not ball.is_within_space():
        ball.bounce_y()

    touch_left = paddle_left != last_paddled and ball.collider.intersect(paddle_left.collider)
    touch_right = paddle_right != last_paddled and ball.collider.intersect(paddle_right.collider)
    if touch_left:
        last_paddled = paddle_left
    elif touch_right:
        last_paddled = paddle_right
    # Detect collision with both paddles
    if touch_left or touch_right:
        ball.bounce_x()
        ball.new_random_color()
        ball.speed_up()

    if ball.miss_right():
        scoreboard.update_score('left')
        ball.ball_reset(-1)
        last_paddled = paddle_right
    elif ball.miss_left():
        scoreboard.update_score('right')
        ball.ball_reset(1)
        last_paddled = paddle_left

screen.exitonclick()

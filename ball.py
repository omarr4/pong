from turtle import Turtle
import random
from collider import Collider

SHAPE = "circle"
SPEED = "fastest"
START_SPEED = 200
TOP_WALL_COR = 280
BOTTOM_WALL_COR = -280
MOVEMENT_SPEEDUP = 1.1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.new_random_color()
        self.speed(SPEED)
        self.y_move = START_SPEED
        self.x_move = START_SPEED
        self.penup()
        self.collider = Collider(0, 0, 20, 20)

    def move(self, delta_time):
        new_x = self.xcor() + self.x_move * delta_time
        new_y = self.ycor() + self.y_move * delta_time
        self.goto(new_x, new_y)
        self.collider.set_position(new_x, new_y)

    def new_random_color(self):
        self.color(
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )

    def is_within_space(self):
        half_win = self.getscreen().window_height() / 2
        if self.y_move > 0:
            # moves up
            return half_win > self.collider.y2()
        else:
            # move down
            return -half_win < self.collider.y1()

    def miss_right(self):
        return self.collider.x2() > self.getscreen().window_width() / 2

    def miss_left(self):
        return self.collider.x1() < -self.getscreen().window_width() / 2

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def speed_up(self):
        self.x_move *= MOVEMENT_SPEEDUP
        self.y_move *= MOVEMENT_SPEEDUP

    def ball_reset(self, direction):
        self.goto(0, 0)
        self.y_move = START_SPEED * direction
        self.x_move = START_SPEED * direction

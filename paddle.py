from turtle import Turtle
from collider import Collider

SHAPE = "square"
COLOR = "white"
STEPS = 20
TOP_WALL_COR = 240
BOTTOM_WALL_COR = -240


class Paddle(Turtle):
    def __init__(self, position_x):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.speed('fastest')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position_x, 0)
        self.collider = Collider(position_x, 0, 20, 100)

    def exceeded_top(self):
        if self.ycor() > TOP_WALL_COR:
            self.sety(TOP_WALL_COR - 2)

    def exceeded_bottom(self):
        if self.ycor() < BOTTOM_WALL_COR:
            self.sety(BOTTOM_WALL_COR + 2)

    def move_up(self):
        self.sety(self.ycor() + STEPS)
        self.collider.set_y(self.ycor())
        self.exceeded_top()

    def move_down(self):
        self.sety(self.ycor() - STEPS)
        self.collider.set_y(self.ycor())
        self.exceeded_bottom()

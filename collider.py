from turtle import Turtle


class Collider(Turtle):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.fillcolor('')
        self.pencolor('')
        self.penup()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.shapesize(height / 20, width / 20)
        self.goto(x, y)

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.goto(x, y)

    def intersect(self, other):
        cond1 = self.x1() < other.x2()
        cond2 = self.x2() > other.x1()
        cond3 = self.y1() < other.y2()
        cond4 = self.y2() > other.y1()
        return cond1 and cond2 and cond3 and cond4

    def x2(self):
        return self.x + self.width / 2

    def y2(self):
        return self.y + self.height / 2

    def x1(self):
        return self.x - self.width / 2

    def y1(self):
        return self.y - self.height / 2

    def set_y(self, y):
        self.y = y
        self.sety(y)

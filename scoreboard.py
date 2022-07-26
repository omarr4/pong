from turtle import Turtle
FONT = ('Arial', 60, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.create_middle_line()
        self.score_left = 0
        self.score_right = 0
        self.write_left()
        self.write_right()

    def update_score(self, scorer):
        self.clear()
        if scorer == 'left':
            self.score_left += 1
        else:
            self.score_right += 1

        self.write_right()
        self.write_left()
        self.create_middle_line()

    def write_left(self):
        self.goto(-125, 210)
        self.write(arg=self.score_left,
                   font=FONT)

    def write_right(self):
        self.goto(82, 210)
        self.write(arg=self.score_right,
                   font=FONT)

    def create_middle_line(self):
        self.color("white")
        self.goto(0, -278)
        self.pensize(2)
        self.setheading(90)
        for _ in range(14):
            self.pendown()
            self.forward(21)
            self.penup()
            self.forward(21)
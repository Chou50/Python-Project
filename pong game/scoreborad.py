from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-30, 240)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(30, 240)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

    def increasing_l_score(self):
        self.l_score += 1
        self.update()

    def increasing_r_score(self):
        self.r_score += 1
        self.update()



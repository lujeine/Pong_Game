from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 270)
        self.write(f"{self.score1}   |   {self.score2}", align='center', font=('Arial', 16, 'bold'))

    def update_score1(self):
        self.score1 += 1
        self.update_scoreboard()

    def update_score2(self):
        self.score2 += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score1}   |   {self.score2}", align='center', font=('Arial', 16, 'bold'))

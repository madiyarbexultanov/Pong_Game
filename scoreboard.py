from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-200, 275)
        self.write(f"Score: {self.l_score}", align="center", font=('Arial', 18, 'bold'))
        self.goto(200, 275)
        self.write(f"Score: {self.r_score}", align="center", font=('Arial', 18, 'bold'))

    def l_counter(self):
        self.l_score += 1
        self.update_score()

    def r_counter(self):
        self.r_score += 1
        self.update_score()
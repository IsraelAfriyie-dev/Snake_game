from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 16, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"GAME OVER!", align=ALIGNMENT, font=('Arial', 32, 'bold'))
        self.goto(0, -36)
        self.write(f"Final score: {self.score}", align=ALIGNMENT, font=FONT)


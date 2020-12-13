from turtle import Turtle

ALIGNMENT, FONT, START_POSITION = "center", ("Courier", 22, "normal"), (0, 250)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(START_POSITION)
        self.pendown()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def restart(self):
        self.clear()
        self.score = 0

from turtle import Turtle

ALIGNMENT, FONT, START_POSITION = "center", ("Courier", 22, "normal"), (0, 250)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        with open("high_score.txt") as file:
            high_score = int(file.read())
            self.high_score = high_score
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(START_POSITION)
        self.pendown()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} | High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)

    def restart(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.score))
        self.score = 0

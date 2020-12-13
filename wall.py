from turtle import Turtle


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pensize(10)
        self.hideturtle()
        self.color("white")
        self.draw_wall()
        self.goto(-300, 300)
        self.pendown()
        self.draw_wall()

    def draw_wall(self):
        self.goto(290, 300)
        self.goto(290, -300)
        self.goto(-300, -300)
        self.goto(-300, 300)

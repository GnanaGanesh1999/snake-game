from turtle import Turtle
from random import randint

BOUNDARY = [280, -280]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")

    def refresh(self):
        self.speed("fastest")
        random_x, random_y = float(randint(BOUNDARY[1], BOUNDARY[0])), float(randint(BOUNDARY[1], BOUNDARY[0]))
        self.goto(random_x, random_y)

from turtle import Turtle, Screen
from time import sleep
from snake import Snake
from food import Food
from score import Score
from wall import Wall

screen = Screen()
screen.setup(width=620, height=620)
screen.bgcolor("black")
screen.title("Mt Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
wall = Wall()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()
    # snake.loop_inside()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.detect_collision_wih_snake() or snake.detect_collision_with_wall():
        score.game_over()
        game_is_on = False

screen.exitonclick()

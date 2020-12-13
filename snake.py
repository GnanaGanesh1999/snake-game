from turtle import Turtle

STARTING_POSITIONS = [(-3, 0)]
MOVE_DISTANCE = 15
X_BOUNDARY, Y_BOUNDARY = (-295, 280), (-300, 300)
TURN_ANGLE = 90
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:

    def __init__(self):
        self.segments = []
        self.add_segment(position=(-10, 0), is_start=True)
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position, is_start=False):
        if is_start:
            new_segment = Turtle("square")
        else:
            new_segment = Turtle("circle")
        new_segment.shapesize(0.6, 0.6, 1)
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        size_of_segment = len(self.segments) - 1
        for seg_num in range(size_of_segment, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def loop_inside(self):
        if self.head.xcor() >= X_BOUNDARY[1]:
            self.head.setx(X_BOUNDARY[0])
        elif self.head.ycor() <= Y_BOUNDARY[0]:
            self.head.sety(Y_BOUNDARY[1])
        elif self.head.xcor() <= X_BOUNDARY[0]:
            self.head.setx(X_BOUNDARY[1])
        elif self.head.ycor() >= Y_BOUNDARY[1]:
            self.head.sety(Y_BOUNDARY[0])

    def detect_collision_with_wall(self):
        return self.head.xcor() >= X_BOUNDARY[1] or self.head.ycor() <= Y_BOUNDARY[0] or \
               self.head.xcor() <= X_BOUNDARY[0] or self.head.ycor() >= Y_BOUNDARY[1]

    def detect_collision_wih_snake(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

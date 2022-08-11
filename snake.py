from turtle import Turtle
import random

# screen sizes
SCREEN_W = 600
SCREEN_H = 600
MOVE_STEP = 20
# degree
MOVE_UP = 90
MOVE_DOWN = 270
MOVE_LEFT = 180
MOVE_RIGHT = 0
# screen edges
WALL_RIGHT = SCREEN_W / 2
WALL_LEFT = -SCREEN_W / 2
WALL_TOP = SCREEN_H / 2
WALL_FLOOR = -SCREEN_H / 2
COLORS = ["red", "orange", "blue", "green", "purple", "white", "pink", "cyan", "magenta", "yellow"]


class Snake:

    # init class params
    def __init__(self):
        self.snake_block = 3
        self.x_start = 0
        self.y_start = 0
        self.snake_body_size = 20
        self.snake_body = []
        self.shape = "square"
        self.color = "white"
        self.speed = 0.1
        self.birth()
        self.head = self.snake_body[0]

    # initialize the snake body
    def birth(self):
        for idx in range(self.snake_block):
            xy_pos = (self.x_start - self.snake_body_size * idx, self.y_start)
            self.add_body_block(xy_pos)

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000, 1000)
        self.snake_body.clear()
        self.birth()
        self.head = self.snake_body[0]
        # self.snake_body = self.snake_body[1:3]
        # self.head.goto(self.x_start, self.y_start)

    # add a snake body block once it eats a food
    def add_body_block(self, xy_pos):
        """Add another body block to itself"""
        new_snake = Turtle(shape=self.shape)
        new_snake.pu()
        new_snake.color(random.choice(COLORS))
        new_snake.setpos(xy_pos)
        self.snake_body.append(new_snake)

    # extend the snake body
    def extend_body(self):
        self.add_body_block(self.snake_body[-1].pos())

    # move the snake body
    def move(self):
        """The head of the snake moves, the body and tail follow"""
        for snake_block in range(len(self.snake_body) - 1, 0, -1):
            x_new = self.snake_body[snake_block - 1].xcor()
            y_new = self.snake_body[snake_block - 1].ycor()
            self.snake_body[snake_block].goto(x_new, y_new)

        # Settings to allow going through walls
        if self.head.xcor() > WALL_RIGHT:
            self.head.setx(WALL_LEFT)
        if self.head.xcor() < WALL_LEFT:
            self.head.setx(WALL_RIGHT)
        if self.head.ycor() > WALL_TOP:
            self.head.sety(WALL_FLOOR)
        if self.head.ycor() < WALL_FLOOR:
            self.head.sety(WALL_TOP)
        # Move the snake block
        self.head.forward(MOVE_STEP)

        # # Check if the head hits itself
        # if self.head in self.snake_body:
        #     print("The snake bumps into its own body!")

    # go up
    def up(self):
        if self.head.heading() != MOVE_DOWN:
            self.head.setheading(MOVE_UP)

    # go down
    def down(self):
        if self.head.heading() != MOVE_UP:
            self.head.setheading(MOVE_DOWN)

    # turn left
    def left(self):
        if self.head.heading() != MOVE_RIGHT:
            self.head.setheading(MOVE_LEFT)

    # turn right
    def right(self):
        if self.head.heading() != MOVE_LEFT:
            self.head.setheading(MOVE_RIGHT)

from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        random_x = random.randrange(-280, 280)
        random_y = random.randrange(-280, 280)
        self.goto(random_x, random_y)
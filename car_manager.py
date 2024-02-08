from turtle import Turtle
import random


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setpos(300, random.randint(-250,250))
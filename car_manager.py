from turtle import Turtle
import random

START_X_POS = 300
CAR_COLOURS = ["red", "blue", "yellow", "green", "orange", "purple", "magenta"]
CAR_MOVE_DISTANCE = 5


class CarManager():

    def __init__(self):
        self.cars = []

    def new_car(self):
        new_car = Turtle(shape="square")
        new_car.penup()
        new_car.color(random.choice(CAR_COLOURS))
        new_car.setpos(START_X_POS, random.randint(-250, 250))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car_new_xpos = car.xcor() - CAR_MOVE_DISTANCE
            car.setx(car_new_xpos)

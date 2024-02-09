import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager

# from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
count = 0

screen.listen()
screen.onkeypress(fun=player.move_up, key="w")

game_is_on = True
while game_is_on:
    count += 1
    time.sleep(0.1)
    screen.update()
    car.move_car()
    # Add a new car every sixth loop
    if count == 6:
        count = 0
        car.new_car()

screen.exitonclick()


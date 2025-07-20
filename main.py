import time
from turtle import Screen

import car_manager
import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

timmy = Player()
screen.listen()
screen.onkey(timmy.move,"Up")
scoreboard = Scoreboard()
game_is_on = True

u = 0

while game_is_on:
    time.sleep(0.1)
    if u % 6 == 0:

        car = CarManager()
        car.create_car()

    for e in car_manager.cars:
        e.move()

        if e.distance(timmy) < 30 :
            timmy.goto(player.STARTING_POSITION)
            print("lost")
        if timmy.ycor() > 260:
            scoreboard.point()
            timmy.goto(player.STARTING_POSITION)
            car_manager.MOVE_INCREMENT += 10
    u+=1

    screen.update()


screen.exitonclick()
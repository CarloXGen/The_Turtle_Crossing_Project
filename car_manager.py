from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0
cars = []

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        color = random.choice(COLORS)
        self.color(color)
        self.penup()
        self.shapesize(1,2.5)
        cars.append(self)
        self.i = random.randint(1,23)
    def create_car(self):
        self.goto(260,240 - 20*self.i)

    def move(self):
        x_cor = self.xcor() - STARTING_MOVE_DISTANCE - MOVE_INCREMENT
        y_cor = self.ycor()

        self.goto(x_cor,y_cor)

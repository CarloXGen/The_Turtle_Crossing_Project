from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(-20, 260)
        self.write(f"Level : {self.level}", move = False , font=("Arial",22,"normal"))

    def point(self):
        self.level +=1
        self.update_score()
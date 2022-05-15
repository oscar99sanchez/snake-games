from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

with open("data.txt") as file:
    contenido = file.read()



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hight_score = int(contenido)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: = {self.score} High Score: {self.hight_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.hight_score:
            self.hight_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

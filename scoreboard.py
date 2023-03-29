from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hight_score = self.get_hight_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def get_hight_score(self):
        with open("high_score.txt") as file:
            score = int(file.read())
        return score
    
    def update_scoreboard(self):
        if self.score > self.hight_score:
            self.hight_score = self.score
            self.update_high_score()
        self.write(f"Score: {self.score} Best Score: {self.hight_score}", align=ALIGMENT, font=FONT)
    
    def update_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.score))
    
    def reset(self):
        self.clear()
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGMENT, font=FONT )

    def increment_score(self):
        self.score = self.score+1
        self.clear()
        self.update_scoreboard()

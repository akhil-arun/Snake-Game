from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.color("yellow")
        self.pu()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
    
    def inc_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def reset(self): 
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        with open("data.txt", mode="w") as file:
            file.write(f"{self.highscore}")
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
   
   # def game_over(self):
     #   self.color("red")
     #   self.goto(0,0)
     #   self.write(f"GAME OVER!", align=ALIGNMENT,font=("Courier", 36, "normal"))


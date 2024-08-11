from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
FONT_2 = ("Courier New", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("old lace")
        self.goto(0 , 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align= ALIGNMENT ,font = FONT)

    def game_over(self):
        self.goto(0 , 0)
        self.color("white")
        self.write("GAME OVER.", align= ALIGNMENT ,font = FONT_2)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
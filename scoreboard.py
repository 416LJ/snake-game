from turtle import Turtle

try:
    with open(file="high_score.txt") as file:
        data = file.read()
except FileNotFoundError:
    print(f"Error: The file was not found.")
    data = 0

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(data)
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=300)
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(arg=f"Score : {self.score} : High Score : {self.high_score}",font=('Courier', 20, 'normal'),align="center",move=False)


    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open(file="high_score.txt", mode="w") as wfile:
            wfile.write(f"{self.high_score}")

        self.scoreboard()


    def update_score(self):
        self.score += 1
        self.scoreboard()
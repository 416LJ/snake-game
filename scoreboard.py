from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        self.score = 0
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=300)
        self.scoreboard()


    def scoreboard(self):
        self.clear()
        self.write(arg=f"Score : {self.score}",font=('Courier', 20, 'normal'),align="center",move=False)


    def final_score(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=0)
        self.write(arg=f"GAME OVER", font=('Courier', 24, 'normal'), align="center", move=False)
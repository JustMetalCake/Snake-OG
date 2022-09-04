from turtle import Turtle


class Scoreboard(Turtle):
    

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.goto(-200, 275)
        self.hideturtle()
        self.color("lime")
        self.update_score()
        

    def increase_score(self):
        self.score += 1
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Current Score: {self.score} High Score: {self.high_score}", font=('Courier', 20, 'normal'))
    

    def reset_board(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:    #saves high score upon program end
                data.write(str(self.high_score))
        self.score = 0
        self.update_score() 



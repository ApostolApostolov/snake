from turtle import Turtle
import time

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(-50, 280)
        self.score = 0
        self.hideturtle()
        self.read_highscore()
        self.write(f"Score: {self.score} High Score: {self.high_score}", font=('Ariel', 12, 'bold'))
        #print(self.update_scoreboard())


    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_new_highscore()

        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", font=('Ariel', 12, 'bold'))
        #self.write("yes", font=('Ariel', 12, 'bold'))

    def read_highscore(self):
        try:
            with open("highscore.txt", mode="r") as file:
                content = file.read()
                print(content)
                self.high_score = int(content)
        except:
            with open("highscore.txt", mode="w") as file:
                file.write("0")

    def write_new_highscore(self):
        with open("highscore.txt", mode="w") as file:
            file.write(str(self.high_score))

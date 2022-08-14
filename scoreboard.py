from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "normal")
SCORE_FILE_NAME = "data.txt"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.color("white")
        self.score = 0
        with open(SCORE_FILE_NAME, mode="r") as data:
            self.hiscore = int(data.read())
        self.setpos(0, 260)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"High score: {self.hiscore} Score: {self.score}", align=ALIGN, font=FONT)

    def reset_pos(self):
        # x_new = (self.shapesize + 600 / 2)
        x_new = 0
        y_new = 250
        xy_pos = (x_new, y_new)
        self.setposition(xy_pos)

    def update_score(self):
        self.score += 10
        if self.hiscore < self.score:
            self.hiscore = self.score
            self.save_score()
        self.display_score()

    def reset_score(self):
        self.score = 0
        self.display_score()

    def game_over(self):
        # self.goto(0, 0)
        self.reset_score()
        self.display_score()
        # self.write("GAME OVER", align=ALIGN, font=FONT)

    def save_score(self):
        with open(SCORE_FILE_NAME, mode="w") as file:
            file.write(f"{self.hiscore}")
        self.display_score()


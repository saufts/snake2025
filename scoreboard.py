from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('arial', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.pencolor('white')
        self.goto(0, 260)

        self.write(f'Score: {self.score}', False, align=ALIGNMENT, font=FONT)


    def refresh(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', False, align=ALIGNMENT, font=FONT)




import time


class Hud:
    def __init__(self, hudTurtle, setup):
        self.time = 0
        self.name = 'Player 1'
        self.turtle = hudTurtle
        self.setup = setup
        self.start = time.perf_counter()

    def draw(self, pontos):
        self.turtle.penup()
        self.turtle.goto(self.setup['size'][0]/2 +
                         10, self.setup['size'][0]/2-30)
        self.turtle.pendown()
        self.turtle.write(self.name, font=("Arial", 16, "normal"))
        self.turtle.penup()
        self.turtle.goto(self.setup['size'][0]/2 +
                         15, self.setup['size'][0]/2-240)
        self.turtle.pendown()
        self.turtle.write(f'Score:', font=("Arial", 16, "normal"))
        self.turtle.penup()
        self.turtle.goto(self.setup['size'][0]/2 +
                         40, self.setup['size'][0]/2-270)
        self.turtle.pendown()
        self.turtle.write(f'{pontos}', font=("Arial", 16, "normal"))
        self.turtle.penup()
        self.turtle.goto(self.setup['size'][0]/2 +
                         10, self.setup['size'][0]/2-440)
        self.turtle.pendown()
        self.turtle.write(
            f'Tempo:', font=("Arial", 16, "normal"))
        self.turtle.penup()
        self.turtle.goto(self.setup['size'][0]/2 +
                         40, self.setup['size'][0]/2-480)
        self.turtle.pendown()
        self.turtle.write(
            f'{(time.perf_counter()  - self.start) :.0f}', font=("Arial", 16, "normal"))
        self.turtle.penup()

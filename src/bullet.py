import math
from copy import copy


class Bullet:
    def __init__(self, turtle, setup, player):
        cellSizeX = (setup['size'][0] / setup['cells'])
        cellSizeY = (setup['size'][1] / setup['cells'])
        self.setup = setup
        self.turtle = turtle
        self.size = cellSizeX * 0.8
        self.x = player.x
        self.y = player.y
        self.index = copy(player.index)
        self.direction = player.direction
        self.speed = setup['size'][0] / setup['cells']

        self.start = False
        self.show = True

    def shape(self):
        angle = 90
        self.turtle.penup()
        self.turtle.setheading(0)

        if(self.direction == 'up'):
            self.turtle.left(angle)
            self.turtle.backward(self.size/2)

        if(self.direction == 'down'):
            self.turtle.right(angle)
            self.turtle.backward(self.size/2)

        if(self.direction == 'left'):
            self.turtle.backward(self.size/2)

        if(self.direction == 'right'):
            self.turtle.left(angle*2)
            self.turtle.backward(self.size/2)

        self.turtle.pendown()
        self.turtle.forward(self.size/4)
        self.turtle.penup()
        self.turtle.forward(self.size/4)
        self.turtle.pendown()
        self.turtle.forward(self.size/4)

    def draw(self, Map):
        if self.show:
            self.move(Map)
            self.turtle.penup()
            self.turtle.goto(self.x, self.y)
            self.turtle.setheading(0)
            self.turtle.pendown()
            self.shape()

    def move(self, Map):

        if(self.direction == 'up'):
            if((self.y + self.speed) > self.setup['size'][1]/2):
                self.show = False
                return
            else:
                self.collision([0, 1], Map)
                self.y += self.speed
                self.index[1] += 1
            return

        if(self.direction == 'down'):
            if((self.y - self.speed) < -self.setup['size'][1]/2):
                self.show = False
                return
            else:
                self.collision([0, -1], Map)
                self.y -= self.speed
                self.index[1] -= 1
            return
        if(self.direction == 'left'):
            if((self.x - self.speed) < -self.setup['size'][0]/2):
                self.show = False
                return
            else:
                self.collision([-1, 0], Map)
                self.x -= self.speed
                self.index[0] -= 1
            return
        if(self.direction == 'right'):
            if((self.x + self.speed) > self.setup['size'][0]/2):
                self.show = False
                return
            else:
                self.collision([1, 0], Map)
                self.x += self.speed
                self.index[0] += 1
            return

    def collision(self, move, Map):
        futureMove = [self.index[0]+move[0], self.index[1]+move[1]]

        try:
            if(Map[futureMove[0]][futureMove[1]].value == 1):
                if (Map[futureMove[0]][futureMove[1]].life > 0):
                    Map[futureMove[0]][futureMove[1]].life -= 1
                    Map[futureMove[0]][futureMove[1]].draw()
                    self.show = False
        except:
            pass

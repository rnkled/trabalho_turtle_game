import math
import random


class Enemy:
    def __init__(self, enemyTurtle, setup):
        cellSizeX = (setup['size'][0] / setup['cells'])
        cellSizeY = (setup['size'][1] / setup['cells'])
        self.setup = setup
        self.EnemyTurtle = enemyTurtle
        self.size = cellSizeX * 0.8
        self.x = (cellSizeX * 0.5) if setup['cells'] % 2 == 0 else 0
        self.y = (setup['size'][1]/2) - (cellSizeX)/2
        self.index = [math.floor(setup['cells']/2), setup['cells']-1]
        self.direction = 'down'
        self.speed = setup['size'][0] / setup['cells']

        self.start = True

        self.alive = True
        self.nextMove = 5
        self.count = 0

    def shape(self):
        u = self.size/15
        angle = 90
        self.EnemyTurtle.penup()
        self.EnemyTurtle.setheading(0)
        self.EnemyTurtle.pencolor('#FF0000')

        if(self.direction == 'up'):
            self.EnemyTurtle.backward(self.size/2)
            self.EnemyTurtle.right(angle)
            self.EnemyTurtle.backward(self.size/2)

        if(self.direction == 'down'):
            self.EnemyTurtle.forward(self.size/2)
            self.EnemyTurtle.left(angle)
            self.EnemyTurtle.backward(self.size/2)

        if(self.direction == 'left'):
            self.EnemyTurtle.backward(self.size/2)
            self.EnemyTurtle.right(angle)
            self.EnemyTurtle.backward(self.size/2)
            self.EnemyTurtle.forward(self.size)
            self.EnemyTurtle.left(angle)

        if(self.direction == 'right'):
            self.EnemyTurtle.forward(self.size/2)
            self.EnemyTurtle.left(angle)
            self.EnemyTurtle.forward(self.size/2)
            self.EnemyTurtle.left(angle)

        self.EnemyTurtle.pendown()
        self.EnemyTurtle.forward(self.size)
        self.EnemyTurtle.left(angle)
        self.EnemyTurtle.forward(3*u)
        self.EnemyTurtle.left(angle)
        self.EnemyTurtle.forward(4*u)
        self.EnemyTurtle.forward(6*u)
        self.EnemyTurtle.backward(6*u)
        self.EnemyTurtle.right(angle)
        self.EnemyTurtle.forward(2*u)
        self.EnemyTurtle.right(angle)
        self.EnemyTurtle.forward(1*u)
        self.EnemyTurtle.left(angle)
        self.EnemyTurtle.forward(5*u)
        self.EnemyTurtle.left(angle)
        self.EnemyTurtle.forward(1*u)
        self.EnemyTurtle.right(angle)
        self.EnemyTurtle.forward(2*u)
        self.EnemyTurtle.right(angle)
        self.EnemyTurtle.backward(6*u)
        self.EnemyTurtle.forward(6*u)
        self.EnemyTurtle.forward(4*u)
        self.EnemyTurtle.left(angle)
        self.EnemyTurtle.forward(3*u)
        self.EnemyTurtle.left(angle)
        self.EnemyTurtle.forward(15*u)
        self.EnemyTurtle.left(angle)
        self.EnemyTurtle.forward(3*u)
        self.EnemyTurtle.left(angle)
        self.EnemyTurtle.forward(5*u)
        self.EnemyTurtle.right(angle)
        self.EnemyTurtle.forward(2*u)
        self.EnemyTurtle.right(angle)
        self.EnemyTurtle.forward(1*u)
        self.EnemyTurtle.left(angle)
        self.EnemyTurtle.forward(1*u)
        self.EnemyTurtle.right(angle)
        self.EnemyTurtle.forward(2*u)
        self.EnemyTurtle.left(angle)
        self.EnemyTurtle.forward(1*u)
        self.EnemyTurtle.right(angle)
        self.EnemyTurtle.forward(4*u)
        self.EnemyTurtle.left(angle)
        self.EnemyTurtle.forward(1*u)
        self.EnemyTurtle.left(angle)
        self.EnemyTurtle.forward(4*u)
        self.EnemyTurtle.right(angle)
        self.EnemyTurtle.forward(1*u)
        self.EnemyTurtle.left(angle)
        self.EnemyTurtle.forward(2*u)
        self.EnemyTurtle.right(angle)
        self.EnemyTurtle.forward(1*u)
        self.EnemyTurtle.left(angle)
        self.EnemyTurtle.forward(1*u)
        self.EnemyTurtle.right(angle)
        self.EnemyTurtle.forward(2*u)
        self.EnemyTurtle.right(angle)
        self.EnemyTurtle.forward(5*u)
        self.EnemyTurtle.left(angle)
        self.EnemyTurtle.forward(3*u)
        self.EnemyTurtle.penup()
        self.EnemyTurtle.right(angle*2)
        self.EnemyTurtle.forward(self.size/2)
        self.EnemyTurtle.right(angle)
        self.EnemyTurtle.forward(self.size/2)
        self.EnemyTurtle.left(angle)

    def draw(self, Map):
        if(self.alive):
            self.randomMove()
            self.move(Map)
            self.EnemyTurtle.penup()
            self.EnemyTurtle.goto(self.x, self.y)
            self.EnemyTurtle.setheading(0)
            self.EnemyTurtle.pendown()
            self.shape()

    def move(self, Map):

        # print(self.index)

        if(self.start == False):
            return

        if(self.direction == 'up'):
            if((self.y + self.speed) > self.setup['size'][1]/2 or self.collision([0, 1], Map)):
                self.count = self.nextMove
                return
            else:
                self.y += self.speed
                self.index[1] += 1
            return
        if(self.direction == 'down'):
            if((self.y - self.speed) < -self.setup['size'][1]/2 or self.collision([0, -1], Map)):
                self.count = self.nextMove
                return
            else:
                self.y -= self.speed
                self.index[1] -= 1
            return
        if(self.direction == 'left'):
            if((self.x - self.speed) < -self.setup['size'][0]/2 or self.collision([-1, 0], Map)):
                self.count = self.nextMove
                return
            else:
                self.x -= self.speed
                self.index[0] -= 1
            return
        if(self.direction == 'right'):
            if((self.x + self.speed) > self.setup['size'][0]/2 or self.collision([1, 0], Map)):
                self.count = self.nextMove
                return
            else:
                self.x += self.speed
                self.index[0] += 1
            return

    def collision(self, move, Map):
        futureMove = [self.index[0]+move[0], self.index[1]+move[1]]
        if(Map[futureMove[0]][futureMove[1]].value == 1):
            return True
        else:
            return False


# Controls

    def up(self):
        self.start = True
        self.direction = 'up'

    def down(self):
        self.start = True
        self.direction = 'down'

    def left(self):
        self.start = True
        self.direction = 'left'

    def right(self):
        self.start = True
        self.direction = 'right'

    def randomMove(self):

        if self.count >= self.nextMove:
            self.nextMove = random.randint(1, 6)
            self.count = 0

            number = random.randint(1, 4)

            if(number == 1):
                self.up()
                return
            if(number == 2):
                self.down()
                return
            if(number == 3):
                self.left()
                return
            if(number == 4):
                self.right()
                return
        else:
            self.count += 1

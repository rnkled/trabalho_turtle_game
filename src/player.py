import math


class Player:
    def __init__(self, playerTurtle, setup):
        self.cellSizeX = (setup['size'][0] / setup['cells'])
        self.cellSizeY = (setup['size'][1] / setup['cells'])
        self.setup = setup
        self.playerTurtle = playerTurtle
        self.size = self.cellSizeX * 0.8
        self.x = (self.cellSizeX * 0.5) if setup['cells'] % 2 == 0 else 0
        self.y = (-setup['size'][1]/2) + (self.cellSizeX)/2
        self.index = [math.floor(setup['cells']/2), 0]
        self.direction = 'up'
        self.speed = setup['size'][0] / setup['cells']

        self.start = False
        self.alive = True

    def shape(self):
        u = self.size/15
        angle = 90
        self.playerTurtle.penup()

        self.playerTurtle.setheading(0)

        if(self.direction == 'up'):
            self.playerTurtle.backward(self.size/2)
            self.playerTurtle.right(angle)
            self.playerTurtle.backward(self.size/2)

        if(self.direction == 'down'):
            self.playerTurtle.forward(self.size/2)
            self.playerTurtle.left(angle)
            self.playerTurtle.backward(self.size/2)

        if(self.direction == 'left'):
            self.playerTurtle.backward(self.size/2)
            self.playerTurtle.right(angle)
            self.playerTurtle.backward(self.size/2)
            self.playerTurtle.forward(self.size)
            self.playerTurtle.left(angle)

        if(self.direction == 'right'):
            self.playerTurtle.forward(self.size/2)
            self.playerTurtle.left(angle)
            self.playerTurtle.forward(self.size/2)
            self.playerTurtle.left(angle)

        self.playerTurtle.pendown()
        self.playerTurtle.forward(self.size)
        self.playerTurtle.left(angle)
        self.playerTurtle.forward(3*u)
        self.playerTurtle.left(angle)
        self.playerTurtle.forward(4*u)
        self.playerTurtle.forward(6*u)
        self.playerTurtle.backward(6*u)
        self.playerTurtle.right(angle)
        self.playerTurtle.forward(2*u)
        self.playerTurtle.right(angle)
        self.playerTurtle.forward(1*u)
        self.playerTurtle.left(angle)
        self.playerTurtle.forward(5*u)
        self.playerTurtle.left(angle)
        self.playerTurtle.forward(1*u)
        self.playerTurtle.right(angle)
        self.playerTurtle.forward(2*u)
        self.playerTurtle.right(angle)
        self.playerTurtle.backward(6*u)
        self.playerTurtle.forward(6*u)
        self.playerTurtle.forward(4*u)
        self.playerTurtle.left(angle)
        self.playerTurtle.forward(3*u)
        self.playerTurtle.left(angle)
        self.playerTurtle.forward(15*u)
        self.playerTurtle.left(angle)
        self.playerTurtle.forward(3*u)
        self.playerTurtle.left(angle)
        self.playerTurtle.forward(5*u)
        self.playerTurtle.right(angle)
        self.playerTurtle.forward(2*u)
        self.playerTurtle.right(angle)
        self.playerTurtle.forward(1*u)
        self.playerTurtle.left(angle)
        self.playerTurtle.forward(1*u)
        self.playerTurtle.right(angle)
        self.playerTurtle.forward(2*u)
        self.playerTurtle.left(angle)
        self.playerTurtle.forward(1*u)
        self.playerTurtle.right(angle)
        self.playerTurtle.forward(4*u)
        self.playerTurtle.left(angle)
        self.playerTurtle.forward(1*u)
        self.playerTurtle.left(angle)
        self.playerTurtle.forward(4*u)
        self.playerTurtle.right(angle)
        self.playerTurtle.forward(1*u)
        self.playerTurtle.left(angle)
        self.playerTurtle.forward(2*u)
        self.playerTurtle.right(angle)
        self.playerTurtle.forward(1*u)
        self.playerTurtle.left(angle)
        self.playerTurtle.forward(1*u)
        self.playerTurtle.right(angle)
        self.playerTurtle.forward(2*u)
        self.playerTurtle.right(angle)
        self.playerTurtle.forward(5*u)
        self.playerTurtle.left(angle)
        self.playerTurtle.forward(3*u)
        self.playerTurtle.penup()
        self.playerTurtle.right(angle*2)
        self.playerTurtle.forward(self.size/2)
        self.playerTurtle.right(angle)
        self.playerTurtle.forward(self.size/2)
        self.playerTurtle.left(angle)

    def draw(self, Map):
        if(self.alive):
            self.move(Map)
            self.playerTurtle.penup()
            self.playerTurtle.goto(self.x, self.y)
            self.playerTurtle.setheading(0)
            self.playerTurtle.pendown()
            self.shape()

    def move(self, Map):

        # print(self.index)

        if(self.start == False):
            return

        if(self.direction == 'up'):
            if((self.y + self.speed) > self.setup['size'][1]/2 or self.collision([0, 1], Map)):
                return
            else:
                self.y += self.speed
                self.index[1] += 1
            return
        if(self.direction == 'down'):
            if((self.y - self.speed) < -self.setup['size'][1]/2 or self.collision([0, -1], Map)):
                return
            else:
                self.y -= self.speed
                self.index[1] -= 1
            return
        if(self.direction == 'left'):
            if((self.x - self.speed) < -self.setup['size'][0]/2 or self.collision([-1, 0], Map)):
                return
            else:
                self.x -= self.speed
                self.index[0] -= 1
            return
        if(self.direction == 'right'):
            if((self.x + self.speed) > self.setup['size'][0]/2 or self.collision([1, 0], Map)):
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

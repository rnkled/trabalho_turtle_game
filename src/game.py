from player import *
from bullet import *
from block import *


class Game:
    def __init__(self, mapTurtle, bulletTurtle, playerTurtle, setup):
        self.player = Player(playerTurtle, setup)
        self.mapTurtle = mapTurtle
        self.playerTurtle = playerTurtle
        self.bulletTurtle = bulletTurtle
        self.setup = setup
        self.cellNumber = setup['cells']
        self.width = setup['size'][0]
        self.height = setup['size'][1]
        self.grid = False
        self.bullets = []
        self.Map = self.loadMap(setup)
        self.renderMap()

    def loadMap(self, setup):
        Map = []

        for y in range(0, self.cellNumber, 1):
            Map.append([])
            for x in range(0, self.cellNumber, 1):
                block = Block(setup['Map'][y][x],
                              self.mapTurtle, self.renderMap)
                Map[y].append(block)
        return Map

    def renderMap(self):
        cellsNumber = self.cellNumber
        w = self.width/cellsNumber
        h = self.height/cellsNumber

        self.mapTurtle.penup()
        self.mapTurtle.setheading(0)
        self.mapTurtle.goto(-self.width/2, -self.height/2)
        self.mapTurtle.pendown()
        self.mapTurtle.forward(self.width)
        self.mapTurtle.left(90)
        self.mapTurtle.forward(self.height)
        self.mapTurtle.left(90)
        self.mapTurtle.forward(self.width)
        self.mapTurtle.left(90)
        self.mapTurtle.forward(self.height)

        for y in range(0, cellsNumber, 1):
            print('\n')
            for x in range(0, cellsNumber, 1):
                self.Map[x][y].x = -self.width/2+x*w
                self.Map[x][y].y = -self.width/2+y*h
                self.Map[x][y].w = w
                self.Map[x][y].h = h
                self.Map[x][y].draw()
                self.Map[x][y].draw()

    def draw(self):
        self.drawPlayer()

    def drawPlayer(self):
        self.playerTurtle.clear()
        self.player.draw(self.Map)
        self.playerTurtle._update()

    def drawBullets(self):
        self.bulletTurtle._clear()
        for bullet in self.bullets:
            if(bullet.show):
                bullet.draw(self.Map)

        self.bulletTurtle._update()

    def shot(self):
        bullet = Bullet(self.bulletTurtle, self.setup, self.player)
        self.bullets.append(bullet)

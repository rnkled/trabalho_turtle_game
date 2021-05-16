from player import *
from bullet import *
from block import *
from enemy import *
from hud import *


class Game:
    def __init__(self, mapTurtle, bulletTurtle, playerTurtle, enemyTurtle, hudTurtle, setup):
        self.player = Player(playerTurtle, setup)
        self.mapTurtle = mapTurtle
        self.playerTurtle = playerTurtle
        self.bulletTurtle = bulletTurtle
        self.enemyTurtle = enemyTurtle
        self.hudTurtle = hudTurtle
        self.hud = Hud(hudTurtle, setup)
        self.setup = setup
        self.cellNumber = setup['cells']
        self.width = setup['size'][0]
        self.height = setup['size'][1]
        self.grid = False
        self.bullets = []
        self.enemys = []
        self.enemyNumber = 3
        self.addEnemys()
        self.Map = self.loadMap(setup)
        self.renderMap()
        self.pontos = 0

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
            for x in range(0, cellsNumber, 1):
                self.Map[x][y].x = -self.width/2+x*w
                self.Map[x][y].y = -self.width/2+y*h
                self.Map[x][y].w = w
                self.Map[x][y].h = h
                self.Map[x][y].draw()
                self.Map[x][y].draw()

    def draw(self):
        self.checkHits()
        self.drawPlayer()
        self.drawEnemys()
        self.drawHud()

    def drawPlayer(self):
        self.playerTurtle.clear()
        self.player.draw(self.Map)
        self.playerTurtle._update()

    def drawEnemys(self):
        self.enemyTurtle.clear()
        for enemy in self.enemys:
            enemy.draw(self.Map)
        self.enemyTurtle._update()

    def drawBullets(self):
        self.bulletTurtle._clear()
        for bullet in self.bullets:
            if(bullet.show):
                bullet.draw(self.Map, self.enemys, self.addPonto)

        self.bulletTurtle._update()

    def shot(self):
        if(self.player.alive):
            bullet = Bullet(self.bulletTurtle, self.setup, self.player)
            self.bullets.append(bullet)

    def addEnemys(self):
        for i in range(0, self.enemyNumber, 1):
            self.enemys.append(Enemy(self.enemyTurtle, self.setup))

    def checkHits(self):
        for enemy in self.enemys:
            if(enemy.alive):
                if(enemy.index == self.player.index):
                    self.player.alive = False

    def drawHud(self):
        self.hudTurtle.clear()
        self.hud.draw(self.pontos)
        self.hudTurtle._update()

    def addPonto(self):
        self.pontos += 1

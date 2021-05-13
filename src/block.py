class Block:
    def __init__(self, value, mapTurtle, renderMap):
        self.value = value
        self.life = 4
        self.mapTurtle = mapTurtle
        self.renderMap = renderMap
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.dead = False

    def rerender(self):
        if(self.dead == False):
            self.mapTurtle.clear()
            self.renderMap()
            self.mapTurtle._update
            self.life = -1

    def draw(self):
        if (self.life == 0):
            self.value = 0
            self.rerender()
        if self.value == 1:
            self.mapTurtle.penup()
            self.mapTurtle.setheading(0)
            self.mapTurtle.goto(self.x, self.y)
            self.mapTurtle.pendown()
            self.mapTurtle.forward(self.w)
            self.mapTurtle.left(90)
            self.mapTurtle.forward(self.h)
            self.mapTurtle.left(90)
            self.mapTurtle.forward(self.w)
            self.mapTurtle.left(90)
            self.mapTurtle.forward(self.h)
            self.mapTurtle.left(90)
            if(self.life < 4):
                self.mapTurtle.goto(self.x+self.w, self.y+self.h)

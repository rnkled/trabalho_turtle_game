class Block:
    def __init__(self, value, mapTurtle, renderMap):
        self.value = value
        self.life = 5
        self.mapTurtle = mapTurtle
        self.renderMap = renderMap
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.dead = False

    def draw(self):
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
            if(self.life < 5):
                self.mapTurtle.goto(self.x+self.w, self.y+self.h)
            if(self.life < 4):
                self.mapTurtle.goto(self.x, self.y+self.h)
                self.mapTurtle.goto(self.x+self.w, self.y)
            if(self.life < 3):
                self.mapTurtle.penup()
                self.mapTurtle.goto(self.x, self.y+self.h/2)
                self.mapTurtle.pendown()
                self.mapTurtle.goto(self.x+self.w, self.y+self.h/2)
            if(self.life < 3):
                self.mapTurtle.penup()
                self.mapTurtle.goto(self.x+self.w/2, self.y+self.h)
                self.mapTurtle.pendown()
                self.mapTurtle.goto(self.x+self.w/2, self.y)
            if(self.life < 1):
                self.value = 0
                self.mapTurtle.clear()
                self.renderMap()

import turtle
import threading
from game import *
from time import sleep
from os import system, stat
import json
import glob


def getPos(px, py):
    x = int((px+size[0]/2)/(size[0]/cells))
    y = int((py+size[1]/2)/(size[1]/cells))
    ################
    if(x > cells-1 or y > cells-1):
        return
    if(x < 0 or y < 0):
        return
    ################
    if(Map[x][y] == 0):
        Map[x][y] = 1
    else:
        Map[x][y] = 0
    renderMap()


def renderMap():
    turtle.clear()
    cellsNumber = cells
    w = size[0]/cellsNumber
    h = size[1]/cellsNumber

    turtle.penup()
    turtle.setheading(0)
    turtle.goto(-size[0]/2, -size[1]/2)
    turtle.pendown()
    turtle.forward(size[0])
    turtle.left(90)
    turtle.forward(size[1])
    turtle.left(90)
    turtle.forward(size[0])
    turtle.left(90)
    turtle.forward(size[1])

    def cell(x, y):
        turtle.penup()
        turtle.setheading(0)
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)

    for y in range(0, cellsNumber, 1):
        for x in range(0, cellsNumber, 1):
            if(Map[x][y] == 1):
                cell(-size[0]/2+w*x, -size[1]/2+h*y)
                turtle.write((x, y))
            # cell(-size[0]/2+w*x, -size[1]/2+h*y)


def reset():
    for y in range(0, cells):
        for x in range(0, cells):
            Map[y][x] = 0
    renderMap()
    turtle.penup()
    turtle.goto(size[0]/2 - 60, size[1]/2)
    turtle.pendown()
    turtle.write(('Map Reseted!'))


def save():

    maps = glob.glob("./maps/*.json")

    if(len(maps) > 0):
        last = maps[-1]
        string = last[-8:]
        number = int(string.split('.')[0])+1
    else:
        number = 1

    data = {}
    data['size'] = size
    data['cells'] = cells
    data['Map'] = Map
    with open(f'./maps/map_{number:03}.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4, sort_keys=True)
    turtle.penup()
    turtle.goto(size[0]/2 - 140, size[1]/2)
    turtle.pendown()
    turtle.write((f'Map Saved as map_{number:03}.json!'))


def main():
    renderMap()
    while on:
        turtle.update()
        sleep(0.2)


# Setup
on = True
size = [600, 600]
cells = 11
Map = [[]]
# Setting up the Screen
screen = turtle.Screen()

screen.setup(size[0]+100, size[1]+50)
screen.clearscreen()
screen.bgcolor("white")

# Setting Map Up
for y in range(0, cells):
    Map.append([])
    for x in range(0, cells):
        Map[y].append(0)


# Turtle Configs
turtle.tracer(0, 0)
turtle.speed(0)
turtle.hideturtle()

# Instancing Game
# Setting the main function to handle the game in another thread
thread = threading.Thread(target=main)

# Controls
turtle.onscreenclick(getPos)
screen.onkeypress(reset, "R")
screen.onkeypress(save, "S")
screen.onkeypress(reset, "r")
screen.onkeypress(save, "s")
screen.listen()

# Play
thread.start()
screen.mainloop()
on = False

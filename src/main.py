import turtle
import threading
import json
import glob
from game import *
from time import sleep


def main():
    frames = 0
    while gameState == 'Game':

        if frames % 15 == 0:
            game.draw()

        if frames % 5 == 0:
            game.drawBullets()

        frames += 1
        sleep(0.01)


def loadMap():
    maps = glob.glob("./maps/*.json")

    if len(maps) == 1:
        with open(maps[0], 'r') as file:
            Map = json.load(file)
            return Map

    for string in maps:
        print(string)

    print('Qual mapa deseja carregar?')

    selected = -1

    while True:
        selected = input('Digite o Número do Mapa: ')
        try:
            selected = int(selected)
            if 0 < selected <= len(maps):
                break
            else:
                raise ValueError
        except ValueError:
            print('Este não é um Número válido, tente novamente.')
            continue

    with open(maps[selected-1], 'r') as file:
        Map = json.load(file)
    return Map


# Setting up the Screen

setup = loadMap()
screen = turtle.Screen()
screen.setup(setup['size'][0]+100, setup['size'][1]+50)
screen.clearscreen()
screen.bgcolor("white")

# Turtle Configs

bulletTurtle = turtle.Turtle()
bulletTurtle.speed(0)
bulletTurtle.hideturtle()

mapTurtle = turtle.Turtle()
mapTurtle.speed(0)
mapTurtle.hideturtle()

turtle.tracer(0, 0)
playerTurtle = turtle.Turtle()
playerTurtle.speed(0)
playerTurtle.hideturtle()

# Instancing Game
game = Game(mapTurtle, bulletTurtle, playerTurtle, setup)

# Setting the main function to handle the game in another thread
thread = threading.Thread(target=main)

# Controls

screen.onkeypress(game.player.up, "w")
screen.onkeypress(game.player.down, "s")
screen.onkeypress(game.player.left, "a")
screen.onkeypress(game.player.right, "d")
screen.onkeypress(game.player.up, "W")
screen.onkeypress(game.player.down, "S")
screen.onkeypress(game.player.left, "A")
screen.onkeypress(game.player.right, "D")
screen.onkeypress(game.shot, "f")
screen.onkeypress(game.shot, "F")
screen.onkeypress(game.shot, "space")
screen.listen()

# Play2
gameState = 'Game'
thread.start()
screen.mainloop()
gameState = 'End'

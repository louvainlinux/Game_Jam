"""
Created on Thu Jul 12 11:46:10 2018 
@author: Quentin
"""
from pygame.locals import *
from random import randint
import pygame
import time
from snake import *

def wallCollision(x,y,width,height):
    if (x<0 or x>=width or y<0 or y>=height):
        return True
    return False

def valid_pos(app, x, y):
        for i in range(0,app.player.length):
            if ((app.player.x[i] == x and app.player.y[i] == y) or (app.other_player.x[i] == x and app.other_player.y[i] == y)):
                return False
        return True

def isCollision(x1,y1,x2,y2):
    if x1 == x2 and y1 == y2:
        return True
    return False

def movePlayer(player, keys):
    if (keys[K_RIGHT]):
        player.moveRight()

    if (keys[K_LEFT]):
        player.moveLeft()

    if (keys[K_UP]):
        player.moveUp()

    if (keys[K_DOWN]):
        player.moveDown()

def moveOtherPlayer(player, keys):
    if (keys[K_D]):
        player.moveRight()

    if (keys[K_Q]):
        player.moveLeft()

    if (keys[K_Z]):
        player.moveUp()

    if (keys[K_S]):
        player.moveDown()

def snakeSpeed(length):
    if (length < 10):
        speed = 1
    elif (length < 15):
        speed = 2
    elif (length < 20):
        speed = 3
    else:
        speed = 4

    return speed

def setLevel(app, level):
    app.level = level

if __name__ == "__main__" :
    theApp = App()
    setLevel(theApp, 4)
    window = Window(theApp._display_surf)
    button = Button(window, restart(theApp), theApp)
    theApp.setWindow(window)
    theApp.setButton(button)
    theApp.on_execute()

import pygame as py
py.init()
from sys import exit

x = 100

y = 100

WIDTH = 800
HEIGHT = 600

myface = py.image.load("sixthsense.png")

gamewindow = py.display.set_mode((WIDTH, HEIGHT))

playgame = True

while playgame == True:

    events = py.event.get()

    keys = py.key.get_pressed()
    
    if keys[py.K_LEFT]:
        # move left
        if x > -195: x -= 5

    if keys[py.K_RIGHT]:
        # move right
        if x < 420: x += 5

    if keys[py.K_DOWN]:
        # move down
        if y < 295: y += 5

    if keys[py.K_UP]:
        # move up
        if y > -140: y -= 5

    if keys[py.K_ESCAPE]:
        playgame = False

    for event in events:
        if event.type == py.QUIT: playgame = False

    gamewindow.fill((0, 0, 0))

    gamewindow.blit(myface, (x, y))

    py.display.update()

    py.time.delay(25)
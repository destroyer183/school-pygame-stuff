import pygame as py
py.init()
from sys import exit

x = 100

y = 100

WIDTH = 800
HEIGHT = 600

gamewindow = py.display.set_mode((WIDTH, HEIGHT))

playgame = True

while playgame == True:

    events = py.event.get()

    keys = py.key.get_pressed()
    
    if keys[py.K_LEFT]:
        # move left
        if x > 50: x -= 5

    if keys[py.K_RIGHT]:
        # move right
        if x < 550: x += 5

    if keys[py.K_DOWN]:
        # move down
        if y < 550: y += 5

    if keys[py.K_UP]:
        # move up
        if y > 50: y -= 5

    if keys[py.K_ESCAPE]:
        playgame = False

    for event in events:
        if event.type == py.QUIT: playgame = False

    gamewindow.fill((0, 0, 0))

    py.draw.circle(gamewindow, (0, 0, 255), (x, y), 50, 10)

    py.display.update()

    py.time.delay(25)
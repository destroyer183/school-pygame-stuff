import pygame as py
from sys import exit
py.init()

x = 50

y = 50

WIDTH = 800
HEIGHT = 600

image = py.image.load("cursor.png")

imagerect = image.get_rect()

imagew = 50

imageh = 50

image_rect = py.Rect(300, 300, imagew, imageh)

gamewindow = py.display.set_mode((WIDTH, HEIGHT))

playgame = True

circle = True

while playgame == True:

    events = py.event.get()

    keys = py.key.get_pressed()
    
    if keys[py.K_LEFT]:
        # move left
        if x > 50: x -= 5

    if keys[py.K_RIGHT]:
        # move right
        if x < 750: x += 5

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

    pygamecircle = py.draw.circle(gamewindow, (0, 0, 255), (x, y), 50, 10)

    circle_rect = py.Rect(x, y, 100, 100)

    if image_rect.colliderect(circle_rect): 
        circle = False
        print("it worked")

    if circle: gamewindow.blit(image, (200, 200))

    py.display.update()

    py.time.delay(25)
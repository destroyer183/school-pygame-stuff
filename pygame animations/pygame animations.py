import pygame as py

py.init()

WIDTH = 800
HEIGHT = 600
the_screen = py.display.set_mode((WIDTH, HEIGHT))

PURPLE = (86, 3, 252)

ball_x = 0

while ball_x < 800:
    
    the_screen.fill((0, 0, 0))

    py.time.delay(20)

    ball_x += 1

    py.draw.circle(the_screen, PURPLE, (ball_x, 300), 100, 0)

    py.display.update()

    py.event.get()
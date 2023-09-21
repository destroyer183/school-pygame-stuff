import pygame as py
from time import sleep 

py.init()

# create the program screen
WIDTH = 800
HEIGHT = 600
game_window = py.display.set_mode((WIDTH, HEIGHT))

# color constants
BLACK = (0, 0, 0)

# white background
py.draw.rect(game_window, (255, 255, 255), (0, 0, WIDTH, HEIGHT), 0)

# head
py.draw.circle(game_window, BLACK, (400, 100), 40, 0)

# body
py.draw.rect(game_window, BLACK, (385, 140, 30, 150), 0)

#  arms
py.draw.rect(game_window, BLACK, (415, 150, 150, 20), 0)
py.draw.rect(game_window, BLACK, (235, 150, 150, 20), 0)

# waist
py.draw.rect(game_window, BLACK, (355, 290, 90, 30), 0)

# legs
py.draw.rect(game_window, BLACK, (355, 320, 20, 150), 0)
py.draw.rect(game_window, BLACK, (425, 320, 20, 150), 0)

py.display.update()

sleep(60000)
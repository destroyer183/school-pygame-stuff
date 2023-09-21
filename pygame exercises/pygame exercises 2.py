import pygame as py
import time

py.init()

# create the program screen
WIDTH = 800
HEIGHT = 600
game_window = py.display.set_mode((WIDTH, HEIGHT))

# white background
py.draw.rect(game_window, (255, 255, 255), (0, 0, WIDTH, HEIGHT), 0)

# hair
py.draw.rect(game_window, (59, 44, 33), (300, 90, 200, 50), 0)
py.draw.rect(game_window, (59, 44, 33), (275, 115, 250, 50), 0)
py.draw.rect(game_window, (59, 44, 33), (250, 140, 300, 50), 0)
py.draw.rect(game_window, (59, 44, 33), (225, 165, 350, 50), 0)

# head
py.draw.circle(game_window, (232, 194, 104), (400, 300), 200, 0)

# eyes
py.draw.circle(game_window, (255, 255, 255), (300, 225), 40, 0)
py.draw.circle(game_window, (0, 200, 0), (300, 225), 25, 0)
py.draw.circle(game_window, (0, 0, 0), (300, 225), 20, 0)
py.draw.circle(game_window, (255, 255, 255), (500, 225), 40, 0)
py.draw.circle(game_window, (0, 200, 0), (500, 225), 25, 0)
py.draw.circle(game_window, (0, 0, 0), (500, 225), 20, 0)

# eyebrows
py.draw.rect(game_window, (59, 44, 33), (260, 170, 80, 10), 0)
py.draw.rect(game_window, (59, 44, 33), (460, 170, 80, 10), 0)

# nose
py.draw.circle(game_window, (200, 150, 75), (400, 300), 25, 0)

# mouth
py.draw.rect(game_window, (100, 0, 0), (290, 340, 220, 80), 0)
py.draw.rect(game_window, (0, 0, 0), (300, 350, 200, 60), 0)

# teeth
py.draw.rect(game_window, (255, 255, 255), (300, 350, 10, 20), 0)
py.draw.rect(game_window, (255, 255, 255), (320, 350, 10, 20), 0)
py.draw.rect(game_window, (255, 255, 255), (340, 350, 10, 20), 0)
py.draw.rect(game_window, (255, 255, 255), (360, 350, 10, 20), 0)
py.draw.rect(game_window, (255, 255, 255), (380, 350, 10, 20), 0)
py.draw.rect(game_window, (255, 255, 255), (400, 350, 10, 20), 0)
py.draw.rect(game_window, (255, 255, 255), (420, 350, 10, 20), 0)
py.draw.rect(game_window, (255, 255, 255), (440, 350, 10, 20), 0)
py.draw.rect(game_window, (255, 255, 255), (460, 350, 10, 20), 0)
py.draw.rect(game_window, (255, 255, 255), (480, 350, 10, 20), 0)

py.draw.rect(game_window, (255, 255, 255), (310, 390, 10, 20), 0)
py.draw.rect(game_window, (255, 255, 255), (330, 390, 10, 20), 0)
py.draw.rect(game_window, (255, 255, 255), (350, 390, 10, 20), 0)
py.draw.rect(game_window, (255, 255, 255), (370, 390, 10, 20), 0)
py.draw.rect(game_window, (255, 255, 255), (390, 390, 10, 20), 0)
py.draw.rect(game_window, (255, 255, 255), (410, 390, 10, 20), 0)
py.draw.rect(game_window, (255, 255, 255), (430, 390, 10, 20), 0)
py.draw.rect(game_window, (255, 255, 255), (450, 390, 10, 20), 0)
py.draw.rect(game_window, (255, 255, 255), (470, 390, 10, 20), 0)
py.draw.rect(game_window, (255, 255, 255), (490, 390, 10, 20), 0)


py.display.update()

time.sleep(60000)
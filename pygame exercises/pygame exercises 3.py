import pygame as py
import time

py.init()

# create the program screen
WIDTH = 400
HEIGHT = 300
game_window = py.display.set_mode((WIDTH, HEIGHT))

# white background
py.draw.rect(game_window, (255, 255, 255), (0, 0, WIDTH, HEIGHT), 0)

# logo
py.draw.rect(game_window, (255, 0, 0), (0, 0, 25, 25), 0)
py.draw.rect(game_window, (0, 255, 0), (2.5, 2.5, 20, 20), 0)
py.draw.rect(game_window, (0, 0, 255), (5, 5, 15, 15), 0)

# company name
main_font = py.font.SysFont("Arial", 16)
title_text = main_font.render("Sugon Inc.", True, (0, 0, 0))
game_window.blit(title_text, (200, 0))

# my name
main_font = py.font.SysFont("Arial", 32)
title_text = main_font.render("Jacob Zante", True, (0, 0, 0))
game_window.blit(title_text, (100, 100))

# job title
main_font = py.font.SysFont("Arial", 16)
title_text = main_font.render("professional world of tanks gamer", True, (0, 0, 0))
game_window.blit(title_text, (100, 150))

# contact info
main_font = py.font.SysFont("Arial", 16)
title_text = main_font.render("101-202-8008", True, (0, 0, 0))
game_window.blit(title_text, (50, 200))
main_font = py.font.SysFont("Arial", 16)
title_text = main_font.render("destroyer183@gmale.kom", True, (0, 0, 0))
game_window.blit(title_text, (50, 225))
main_font = py.font.SysFont("Arial", 16)
title_text = main_font.render("121 freddy fazbear street", True, (0, 0, 0))
game_window.blit(title_text, (50, 250))

py.display.update()

time.sleep(60000)
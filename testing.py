import pygame as py
import sys

py.init()

running = True
starting_screen = True

WIDTH = 800
HEIGHT = 600

game_window = py.display.set_mode((WIDTH, HEIGHT))

Arial = py.font.SysFont('Arial', 20)

while starting_screen:

    keys = py.key.get_pressed()

    events = py.event.get()

    game_window.fill((0, 0, 0))

    instructions = Arial.render('press any key to move on', True, (255, 255, 255))

    instructions_rect = instructions.get_rect(center=(400, 200))

    game_window.blit(instructions, instructions_rect)

    print('looping')


    if keys[py.K_RETURN]:

        print('button press detected')

        starting_screen = False

    for event in events:

        if event.type == py.QUIT:

            running = False

            starting_screen = False

            sys.exit()

    py.display.update()

    py.time.delay(25)

while running:

    keys = py.key.get_pressed()

    events = py.event.get()

    game_window.fill((0, 0, 0))

    

    py.display.update()

    py.time.delay(25)
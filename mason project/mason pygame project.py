# the start
import sys, pygame
pygame.init()

# basic setup for graphics
WIDTH = 800
HEIGHT = 600
game_screen = pygame.display.set_mode((WIDTH, HEIGHT))

# color for the graphics for drawing
MOON_COLOR = (100, 100, 100)
GROUND_COLOR = (0, 128, 0)
SKY_COLOR = (0, 0, 255)
SUN_COLOR = (255, 255, 0)
NIGHT_GROUND_COLOR = (0, 100, 0)
NIGHT_SKY_COLOR = (25, 25, 112)

# puzzle variables
piece_1_collected = False
piece_2_collected = False
piece_3_collected = False
piece_4_collected = False



# images
stickman = pygame.image.load("stickman.png").convert_alpha()
stickman = pygame.transform.scale(stickman, (80, 92.5))

treasure = pygame.image.load('treasure.png').convert_alpha()
treasure = pygame.transform.scale(treasure, (97.5, 70))

puzzle_piece1 = pygame.image.load('puzzle piece 1.png').convert_alpha()
puzzle_piece1 = pygame.transform.scale(puzzle_piece1, (78, 101))

puzzle_piece2 = pygame.image.load('puzzle piece 2.png').convert_alpha()
puzzle_piece2 = pygame.transform.scale(puzzle_piece2, (101, 78))

puzzle_piece3 = pygame.image.load('puzzle piece 3.png').convert_alpha()
puzzle_piece3 = pygame.transform.scale(puzzle_piece3, (101, 78))

puzzle_piece4 = pygame.image.load('puzzle piece 4.png').convert_alpha()
puzzle_piece4 = pygame.transform.scale(puzzle_piece4, (78, 101))



# player variables
player_x = 200
player_y = 100
player_speed = 10



# sun stuff
is_night = False
SUN_RADIUS = 40
sun_x = 0 - SUN_RADIUS
sun_y = 100
SUN_SPEED = 10



# fonts
font = pygame.font.SysFont('Arial', 20)



def draw_house():

    pygame.draw.rect(game_screen, (150, 75, 0), (550, 350, 100, 75), 0)

    pygame.draw.polygon(game_screen, (200, 100, 0), [(550, 350), (650, 350), (600, 312.5)], 0)

    pygame.draw.rect(game_screen, (205, 127, 50), (582, 387.5, 40, 39), 0)

    
    



# game loop
is_running = True
starting_screen = True
win_screen = False
lose_screen = False

while starting_screen:

    events = pygame.event.get()

    keys = pygame.key.get_pressed()

    game_screen.fill((0, 0, 0))

    instructions_text1 = font.render('How to play the game:', True, (255, 255, 255))
    instructions_text1_rect = instructions_text1.get_rect(center=(400, 200))
    game_screen.blit(instructions_text1, instructions_text1_rect)

    instructions_text2 = font.render('You have 1 day and 1 night to collect all puzzle pieces and go back home.', True, (255, 255, 255))
    instructions_text2_rect = instructions_text2.get_rect(center=(400, 225))
    game_screen.blit(instructions_text2, instructions_text2_rect)

    instructions_text3 = font.render('Press enter to continue.', True, (255, 255, 255))
    instructions_text3_rect = instructions_text3.get_rect(center=(400, 250))
    game_screen.blit(instructions_text3, instructions_text3_rect)



    

    if keys[pygame.K_RETURN]:

        starting_screen = False

    for event in events:

        if event.type == pygame.QUIT:

            starting_screen, is_running = False, False

            pygame.quit()

            sys.exit()

    pygame.display.update()

    pygame.time.delay(25)





while is_running:

    events = pygame.event.get()

    keys = pygame.key.get_pressed()

    if is_night:

        current_sun_color = MOON_COLOR

        current_ground_color = NIGHT_GROUND_COLOR

        current_sky_color = NIGHT_SKY_COLOR

    else: 

        current_sun_color = SUN_COLOR

        current_ground_color = GROUND_COLOR

        current_sky_color = SKY_COLOR



    game_screen.fill(current_sky_color)

    pygame.draw.rect(game_screen, current_ground_color, (0, 200, 800, 400), 0)

    pygame.draw.circle(game_screen, current_sun_color, (sun_x, sun_y), SUN_RADIUS, 0)


    
    draw_house()

    house_rect = pygame.Rect(550, 350, 100, 75)



    treasure_rect1 = treasure.get_rect(center=(200, 400))
    game_screen.blit(treasure, treasure_rect1)

    treasure_rect2 = treasure.get_rect(center=(400, 300))
    game_screen.blit(treasure, treasure_rect2)

    treasure_rect3 = treasure.get_rect(center=(500, 500))
    game_screen.blit(treasure, treasure_rect3)

    treasure_rect4 = treasure.get_rect(center=(150, 500))
    game_screen.blit(treasure, treasure_rect4)

    treasure_rect5 = treasure.get_rect(center=(700, 300))
    game_screen.blit(treasure, treasure_rect5)

    treasure_rect6 = treasure.get_rect(center=(100, 300))
    game_screen.blit(treasure, treasure_rect6)

    treasure_rect7 = treasure.get_rect(center=(375, 475))
    game_screen.blit(treasure, treasure_rect7)

    treasure_rect8 = treasure.get_rect(center=(725, 500))
    game_screen.blit(treasure, treasure_rect8)




    stickman_rect = stickman.get_rect(center=(player_x, player_y))
    game_screen.blit(stickman, stickman_rect)


    

    if sun_x >= WIDTH + SUN_RADIUS:

        if is_night:

            lose_screen = True
            is_running = False

        is_night = not is_night

        sun_x = 0 - SUN_RADIUS



    sun_x += SUN_SPEED



    for event in events:

        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()



    if keys[pygame.K_SPACE]:

        if stickman_rect.colliderect(treasure_rect1):

            piece_1_collected = True

            puzzle_piece1_rect = puzzle_piece1.get_rect(center=(200, 400))

            game_screen.blit(puzzle_piece1, puzzle_piece1_rect)

        

        if stickman_rect.colliderect(treasure_rect2):

            piece_2_collected = True

            puzzle_piece2_rect = puzzle_piece2.get_rect(center=(400, 300))

            game_screen.blit(puzzle_piece2, puzzle_piece2_rect)

        

        if stickman_rect.colliderect(treasure_rect3):

            piece_3_collected = True

            puzzle_piece3_rect = puzzle_piece3.get_rect(center=(500, 500))

            game_screen.blit(puzzle_piece3, puzzle_piece3_rect)



        if stickman_rect.colliderect(treasure_rect5):

            piece_4_collected = True

            puzzle_piece4_rect = puzzle_piece4.get_rect(center=(700, 300))

            game_screen.blit(puzzle_piece4, puzzle_piece4_rect)

        

        if stickman_rect.colliderect(house_rect):

            if piece_1_collected == True and piece_2_collected == True and piece_3_collected == True and piece_4_collected == True:

                win_screen = True

                is_running = False




    if keys[pygame.K_w]:
        player_y -= player_speed

    if keys[pygame.K_a]:
        player_x -= player_speed

    if keys[pygame.K_s]:
        player_y += player_speed

    if keys[pygame.K_d]:
        player_x += player_speed

    if player_x >= WIDTH:
        player_x = WIDTH

    if player_x <= 0:
        player_x = 0

    if player_y >= HEIGHT:
        player_y = HEIGHT

    if player_y <= 170:
        player_y = 170



    pygame.display.update()

    pygame.time.delay(25)


while win_screen:

    events = pygame.event.get()

    keys = pygame.key.get_pressed()

    game_screen.fill((0, 0, 0))



    win_text1 = font.render('You have won the game!', True, (255, 255, 255))

    win_text1_rect = win_text1.get_rect(center=(400, 200))

    game_screen.blit(win_text1, win_text1_rect)


    for event in events:

        if event.type == pygame.QUIT:

            win_screen = False

            pygame.quit()
            sys.exit()



    pygame.display.update()

    pygame.time.delay(25)




while lose_screen:

    events = pygame.event.get()

    keys = pygame.key.get_pressed()

    game_screen.fill((0, 0, 0))



    lose_text1 = font.render('You ran out of time!', True, (255, 255, 255))

    lose_text1_rect = lose_text1.get_rect(center=(400, 200))

    game_screen.blit(lose_text1, lose_text1_rect)


    for event in events:

        if event.type == pygame.QUIT:

            win_screen = False

            pygame.quit()
            sys.exit()



    pygame.display.update()

    pygame.time.delay(25)


    
    


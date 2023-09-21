# the start
import sys, pygame, math, random
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



# images
stickman = pygame.image.load("stickman.png").convert_alpha()
stickman = pygame.transform.scale(stickman, (80, 92.5))

fireball_right = pygame.image.load('fireball right.png').convert_alpha()
fireball_right = pygame.transform.scale(fireball_right, (96, 75))

fireball_left = pygame.image.load('fireball left.png').convert_alpha()
fireball_left = pygame.transform.scale(fireball_left, (96, 75))

boss_left = pygame.image.load('boss left.png').convert_alpha()
boss_left = pygame.transform.scale(boss_left, (136.2, 128.4))

boss_right = pygame.image.load('boss right.png').convert_alpha()
boss_right = pygame.transform.scale(boss_right, (136.2, 128.4))

laser_beam = pygame.image.load('laser beam.png').convert_alpha()
laser_beam = pygame.transform.scale(laser_beam, (80, 80))
laser_beam = pygame.transform.rotate(laser_beam, 90)

heart = pygame.image.load("heart.png").convert_alpha()
heart = pygame.transform.scale(heart, (27, 27))



# player variables
player_x = 200
player_y = 100
player_speed = 4
player_health = 2


# boss stuff
boss_x = 700
boss_y = 300
boss_x_speed = -2
boss_y_speed = -2
laser_x = 0
laser_y = 0
laser_x_speed = 10
laser_y_speed = 10
laser_on_screen = False
boss_health = 200




# bullet stuff
bullet_x = 0
bullet_y = 0
bullet_x_speed = 10
bullet_y_speed = 10
bullet_on_screen = False



# sun stuff
is_night = False
SUN_RADIUS = 40
sun_x = 0 - SUN_RADIUS
sun_y = 100
SUN_SPEED = 2



# fonts
font = pygame.font.SysFont('Arial', 20) 



def draw_bullet():
    global bullet_x, bullet_y, step_x, step_y, bullet_on_screen, dist_x, dist_y, fireball_rect
    

    if not bullet_on_screen:

        bullet_x = player_x

        bullet_y = player_y

        mouse_position = pygame.mouse.get_pos()

        mouse_x = mouse_position[0]

        mouse_y = mouse_position[1]

        dist_x = mouse_x - player_x

        dist_y = mouse_y - player_y

        steps_number = max(abs(dist_x), abs(dist_y))

        step_x = float(dist_x) / (steps_number / bullet_x_speed)

        step_y = float(dist_y) / (steps_number / bullet_y_speed)

    

    else:

        bullet_x += step_x
        bullet_y += step_y

        if step_x < 0:

            fireball = fireball_left 

        else:

            fireball = fireball_right

        
            
        fireball = pygame.transform.rotate(fireball, math.degrees(math.atan(dist_y / dist_x)) * -1)
            
        fireball_rect = fireball.get_rect(center=(bullet_x, bullet_y))
        game_screen.blit(fireball, fireball_rect)



    if bullet_x >= WIDTH or bullet_x <= 0 or bullet_y >= HEIGHT or bullet_y <= 0:

        bullet_on_screen = False



# draw the boss
def draw_boss():
    global boss_x, boss_y, boss_x_speed, boss_y_speed, boss_rect

    player_dist_x = player_x - boss_x

    player_dist_y = player_y - boss_y

    if player_dist_x < 0:

        boss = boss_left

    else:

        boss = boss_right

    try:

        boss = pygame.transform.rotate(boss, math.degrees(math.atan(player_dist_y / player_dist_x)) * -1)

    except:pass

    boss_x += boss_x_speed
    boss_y += boss_y_speed

    boss_rect = boss.get_rect(center=(boss_x, boss_y))
    game_screen.blit(boss, boss_rect)

    if boss_x >= WIDTH - 70:
        boss_x = WIDTH - 70
        boss_x_speed *= -1
        boss_x_speed += random.randint(-1, 1)
        if boss_x_speed == 0:
            boss_x_speed = 1


    if boss_x <= 70:
        boss_x = 70
        boss_x_speed *= -1
        boss_x_speed += random.randint(-1, 1)
        if boss_x_speed == 0:
            boss_x_speed = 1
        

    if boss_y >= HEIGHT - 70:
        boss_y = HEIGHT - 70
        boss_y_speed *= -1
        boss_y_speed += random.randint(-1, 1)
        if boss_y_speed == 0:
            boss_y_speed = 1
        

    if boss_y <= 70:
        boss_y = 70
        boss_y_speed *= -1
        boss_y_speed += random.randint(-1, 1)
        if boss_y_speed == 0:
            boss_y_speed = 1



def draw_laser():

    global laser_x, laser_y, laser_step_x, laser_step_y, laser_on_screen, laser_dist_x, laser_dist_y, laser_rect
    
    

    if not laser_on_screen:

        laser_x = boss_x

        laser_y = boss_y

        laser_dist_x = player_x - boss_x

        laser_dist_y = player_y - boss_y

        steps_number = max(abs(laser_dist_x), abs(laser_dist_y))

        laser_step_x = float(laser_dist_x) / (steps_number / laser_x_speed)

        laser_step_y = float(laser_dist_y) / (steps_number / laser_y_speed)

    

    else:

        laser_x += laser_step_x
        laser_y += laser_step_y

        laser = laser_beam
            
        laser = pygame.transform.rotate(laser, math.degrees(math.atan(laser_dist_y / laser_dist_x)) * -1)
            
        laser_rect = laser.get_rect(center=(laser_x, laser_y))
        game_screen.blit(laser, laser_rect)



    laser_on_screen = True



    if laser_x >= WIDTH or laser_x <= 0 or laser_y >= HEIGHT or laser_y <= 0:

        laser_on_screen = False



# boss health
def draw_boss_health():

    pygame.draw.rect(game_screen, (0, 0, 0), (290, 0, 220, 50), 0)

    pygame.draw.rect(game_screen, (255, 0, 0), (300, 10, boss_health, 30), 0)



# draw player health
def draw_player_health():


    if player_health >= 1:

        game_screen.blit(heart, (player_x - 30, player_y - 80))

    if player_health >= 2:

        game_screen.blit(heart, (player_x, player_y - 80))





def collisions():

    global player_health, boss_health, laser_on_screen, bullet_on_screen, laser_x, laser_y, bullet_x, bullet_y, laser, fireball, laser_rect, fireball_rect

    try:

        if laser_rect.colliderect(stickman_rect):

            player_health -= 1

            laser_on_screen = False

            laser_x = boss_x

            laser_y = boss_y

            laser = laser_beam

            laser_rect = laser.get_rect(center=(laser_x, laser_y))



        if fireball_rect.colliderect(boss_rect):

            boss_health -= 20

            bullet_on_screen = False

            bullet_x = player_x

            bullet_y = player_y

            if step_x < 0:

                fireball = fireball_left 

            else:

                fireball = fireball_right

            fireball_rect = fireball.get_rect(center=(bullet_x, bullet_y))

            

    except:pass



# game loop
is_running = True
starting_screen = True
win_screen = False
lose_screen = False

while starting_screen:

    events = pygame.event.get()

    keys = pygame.key.get_pressed()

    game_screen.fill((0, 0, 0))

    instructions_text1 = font.render('Defeat the boss!', True, (255, 255, 255))
    instructions_text1_rect = instructions_text1.get_rect(center=(400, 200))
    game_screen.blit(instructions_text1, instructions_text1_rect)

    instructions_text2 = font.render('Press SPACE to shoot', True, (255, 255, 255))
    instructions_text2_rect = instructions_text2.get_rect(center=(400, 225))
    game_screen.blit(instructions_text2, instructions_text2_rect)

    instructions_text3 = font.render('Press enter to continue', True, (255, 255, 255))
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



    stickman_rect = stickman.get_rect(center=(player_x, player_y))
    game_screen.blit(stickman, stickman_rect)


    

    if sun_x >= WIDTH + SUN_RADIUS:

        is_night = not is_night

        sun_x = 0 - SUN_RADIUS



    sun_x += SUN_SPEED


    
    draw_bullet()

    draw_boss()

    draw_laser()

    draw_boss_health()

    draw_player_health()

    collisions()

    if player_health == 0:
        
        lose_screen = True

        is_running = False
        

    if boss_health == 0:
        win_screen = True
        is_running = False
        



    for event in events:

        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()



    if keys[pygame.K_SPACE]:
        bullet_on_screen = True

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



    win_text1 = font.render('You killed the boss!', True, (255, 255, 255))

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



    lose_text1 = font.render('You died!', True, (255, 255, 255))

    lose_text1_rect = lose_text1.get_rect(center=(400, 200))

    game_screen.blit(lose_text1, lose_text1_rect)


    for event in events:

        if event.type == pygame.QUIT:

            win_screen = False

            pygame.quit()
            sys.exit()



    pygame.display.update()

    pygame.time.delay(25)


    
    


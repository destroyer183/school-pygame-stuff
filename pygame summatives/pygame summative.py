# imports
import pygame as py
from sys import exit
import os
py.init()

# priority list
# use images instead of text for cpu and gpu benchmarks

# this makes sure the window is scaled correctly when it is displayed.
if os.name == "nt":
    try:
        import ctypes
        
        awareness  = ctypes.c_int()
        error_Code = ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))
        error_Code = ctypes.windll.shcore.SetProcessDpiAwareness(2)
        success    = ctypes.windll.user32.SetProcessDPIAware()
    except:pass 

# open the information file with all text and images
file = open("text.txt")
info = file.readlines()

# set up variables for game components
play_game        = True
selection_number = 0
budget           = "not chosen"
cpu_type         = 0
cost             = 0

# fonts
title_font = py.font.SysFont("Arial", 100)
main_font  = py.font.SysFont("Arial", 50)
small_font = py.font.SysFont("Arial", 30)

# GUI dimensions
HEIGHT = 1000
WIDTH  = 1600

# image starting location
y = 200
x = 420

# choice box colors to show highlighting and errors.
first_box_color  = (0, 0, 0)
second_box_color = (0, 0, 0)
third_box_color  = (0, 0, 0)
buy_box_color    = (0, 0, 0)

# keep track of choices made
choice0 = 0
choice1 = 0
choice2 = 0
choice3 = 0
choice4 = 0
choice5 = 0
choice6 = 0
choice7 = 0
choice8 = 0
choice9 = 0

# image rectangle
char = py.image.load("images/character.png")
char_rect = char.get_rect()

# set up window
game_window = py.display.set_mode((WIDTH, HEIGHT))
game_window.fill((200, 200, 200))

# game loop
while play_game == True:

    char_rect = py.Rect(x, y, char_rect.width, char_rect.height)

    events    = py.event.get()

    keys      = py.key.get_pressed()

    game_window.fill((200, 200, 200))

    game_window.blit(char, (x, y))

    # draws the choices on the GUI
    if selection_number < 10:

        # header
        header_text = title_font.render(info[selection_number].strip(), True, (0, 0, 0))
        help_text   = main_font. render("press 'h' for help",           True, (0, 0, 0))
        header_rect = header_text.get_rect(center=(800, 55))
        help_rect   = help_text.  get_rect(center=(800, 150))
        game_window.blit(header_text, header_rect)
        game_window.blit(help_text, help_rect)
        
        # choices with three options
        if selection_number == 0 or selection_number == 5 or selection_number == 6 or selection_number == 7:

            # put the collision rectangles in the correct locations
            first_rect   = py.Rect(100,  200, 300, 300)
            second_rect  = py.Rect(650,  200, 300, 300)
            third_rect   = py.Rect(1200, 200, 300, 300)

            # option boxes
            py.draw.rect(game_window, first_box_color,  (100,  200, 300, 300), 10)
            py.draw.rect(game_window, second_box_color, (650,  200, 300, 300), 10)
            py.draw.rect(game_window, third_box_color,  (1200, 200, 300, 300), 10)

            # images
            option1     = py.image.load  (info[11 + selection_number].strip())
            option2     = py.image.load  (info[22 + selection_number].strip())
            option3     = py.image.load  (info[33 + selection_number].strip())

            # item names
            option1_text = main_font.render(info[42 + selection_number].strip(), True, (0, 0, 0))
            option2_text = main_font.render(info[53 + selection_number].strip(), True, (0, 0, 0))
            option3_text = main_font.render(info[64 + selection_number].strip(), True, (0, 0, 0))

            # item prices
            if selection_number != 0: price1_text = main_font.render("Price: $" + info[73 + selection_number].strip(), True, (0, 0, 0))
            else                    : price1_text = main_font.render(             info[73 + selection_number].strip(), True, (0, 0, 0))
            if selection_number != 0: price2_text = main_font.render("Price: $" + info[84 + selection_number].strip(), True, (0, 0, 0))
            else                    : price2_text = main_font.render(             info[84 + selection_number].strip(), True, (0, 0, 0))
            if selection_number != 0: price3_text = main_font.render("Price: $" + info[95 + selection_number].strip(), True, (0, 0, 0))
            else                    : price3_text = main_font.render(             info[95 + selection_number].strip(), True, (0, 0, 0))

            # rectangles
            option1_rect = option1.     get_rect(center=(250,  350))
            option2_rect = option2.     get_rect(center=(800,  350))
            option3_rect = option3.     get_rect(center=(1350, 350))
            text1_rect   = option1_text.get_rect(center=(250,  550))
            text2_rect   = option2_text.get_rect(center=(800,  550))
            text3_rect   = option3_text.get_rect(center=(1350, 550))
            price1_rect  = price1_text. get_rect(center=(250,  600))
            price2_rect  = price2_text. get_rect(center=(800,  600))
            price3_rect  = price3_text. get_rect(center=(1350, 600))
        
            # placing everything
            game_window.blit(option1,      option1_rect)
            game_window.blit(option2,      option2_rect)
            game_window.blit(option3,      option3_rect)
            game_window.blit(option1_text, text1_rect)
            game_window.blit(option2_text, text2_rect)
            game_window.blit(option3_text, text3_rect)
            game_window.blit(price1_text,  price1_rect)
            game_window.blit(price2_text,  price2_rect)
            game_window.blit(price3_text,  price3_rect)

        # choices with two options
        else:
            if selection_number < 11:
                # put the collision rectangles in the correct locations
                first_rect   = py.Rect(0,     0,   500, 660)
                second_rect  = py.Rect(1100,  0,   500, 660)
                third_rect   = py.Rect(10000, 200, 300, 300)

                # option boxes
                py.draw.rect(game_window, first_box_color,  (0,    0, 500, 660), 10)
                py.draw.rect(game_window, second_box_color, (1100, 0, 500, 660), 10)

                # images
                option1     = py.image.load  (info[11 + selection_number].strip())
                option2     = py.image.load  (info[22 + selection_number].strip())

                # item names
                option1_text = main_font.render(             info[42 + selection_number].strip(), True, (0, 0, 0))
                option2_text = main_font.render(             info[53 + selection_number].strip(), True, (0, 0, 0))

                # item prices
                price1_text  = main_font.render("Price: $" + info[73 + selection_number].strip(), True, (0, 0, 0))
                price2_text  = main_font.render("Price: $" + info[84 + selection_number].strip(), True, (0, 0, 0))

                # rectangles
                option1_rect = option1.     get_rect(center=(250,  350))
                option2_rect = option2.     get_rect(center=(1350, 350))
                text1_rect   = option1_text.get_rect(center=(250,  550))
                text2_rect   = option2_text.get_rect(center=(1350, 550))
                price1_rect  = price1_text. get_rect(center=(250,  600))
                price2_rect  = price2_text. get_rect(center=(1350, 600))

                # placing everything
                game_window.blit(option1,      option1_rect)
                game_window.blit(option2,      option2_rect)
                game_window.blit(option1_text, text1_rect)
                game_window.blit(option2_text, text2_rect)
                game_window.blit(price1_text,  price1_rect)
                game_window.blit(price2_text,  price2_rect)



    if selection_number < 10:
        # this displays the budget only if it has been chosen
        if budget != "not chosen":
            budget_text = main_font.render("Budget: $" + str(budget), True, (0, 0, 0))
            budget_rect = budget_text.get_rect(center=(800, 700))
            game_window.blit(budget_text, budget_rect)



        # highlights the box in green if the user is hovering over it
        if char_rect.colliderect(first_rect) : first_box_color  = (0, 255, 0)
        else                                 : first_box_color  = (0, 0,   0)
        if char_rect.colliderect(second_rect): second_box_color = (0, 255, 0)
        else                                 : second_box_color = (0, 0,   0)
        if char_rect.colliderect(third_rect) : third_box_color  = (0, 255, 0)
        else                                 : third_box_color  = (0, 0,   0)



        # this section deals with the cart at the bottom
        cart_text = main_font.render("Cart:", True, (0, 0, 0))
        cart_rect = cart_text.get_rect(center=(80, 810))
        game_window.blit(cart_text, cart_rect)
        py.draw.rect(game_window, (0, 0, 0), (150,  735, 150, 150), 10)
        py.draw.rect(game_window, (0, 0, 0), (310,  735, 150, 150), 10)
        py.draw.rect(game_window, (0, 0, 0), (470,  735, 150, 150), 10)
        py.draw.rect(game_window, (0, 0, 0), (630,  735, 150, 150), 10)
        py.draw.rect(game_window, (0, 0, 0), (790,  735, 150, 150), 10)
        py.draw.rect(game_window, (0, 0, 0), (950,  735, 150, 150), 10)
        py.draw.rect(game_window, (0, 0, 0), (1110, 735, 150, 150), 10)
        py.draw.rect(game_window, (0, 0, 0), (1270, 735, 150, 150), 10)
        py.draw.rect(game_window, (0, 0, 0), (1430, 735, 150, 150), 10)

        # placing images
        if choice1 != 0:
            item1      = py.image.load(info[11 * choice1 + 1].strip())
            item1      = py.transform.scale(item1, (125, 125))
            item1_rect = item1.    get_rect(center=(225, 810))
            game_window.blit(item1, item1_rect)
        if choice2 != 0:
            item2      = py.image.load(info[11 * choice2 + 2].strip())
            item2      = py.transform.scale(item2, (125, 125))
            item2_rect = item2.    get_rect(center=(385, 810))
            game_window.blit(item2, item2_rect)
        if choice3 != 0:
            item3      = py.image.load(info[11 * choice3 + 3].strip())
            item3      = py.transform.scale(item3, (125, 125))
            item3_rect = item3.    get_rect(center=(545, 810))
            game_window.blit(item3, item3_rect)
        if choice4 != 0:
            item4      = py.image.load(info[11 * choice4 + 4].strip())
            item4      = py.transform.scale(item4, (125, 125))
            item4_rect = item4.    get_rect(center=(705, 810))
            game_window.blit(item4, item4_rect)
        if choice5 != 0:
            item5      = py.image.load(info[11 * choice5 + 5].strip())
            item5      = py.transform.scale(item5, (125, 125))
            item5_rect = item5.    get_rect(center=(865, 810))
            game_window.blit(item5, item5_rect)
        if choice6 != 0:
            item6      = py.image.load(info[11 * choice6 + 6].strip())
            item6      = py.transform.scale(item6, (125,  125))
            item6_rect = item6.    get_rect(center=(1025, 810))
            game_window.blit(item6, item6_rect)
        if choice7 != 0:
            item7      = py.image.load(info[11 * choice7 + 7].strip())
            item7      = py.transform.scale(item7, (125,  125))
            item7_rect = item7.    get_rect(center=(1185, 810))
            game_window.blit(item7, item7_rect)
        if choice8 != 0:
            item8      = py.image.load(info[11 * choice8 + 8].strip())
            item8      = py.transform.scale(item8, (125,  125))
            item8_rect = item8.    get_rect(center=(1345, 810))
            game_window.blit(item8, item8_rect)
        if choice9 != 0:
            item9      = py.image.load(info[11 * choice9 + 9].strip())
            item9      = py.transform.scale(item9, (125,  125))
            item9_rect = item9.    get_rect(center=(1505, 810))
            game_window.blit(item9, item9_rect)

        # dividing line in between cart and options
        py.draw.rect(game_window, (0, 0, 0), (-100, 650, 3000, 3000), 10)

    

    # function to display more info about an item when a button is pressed
    def information():
        # cpu benchmarks
        if selection_number == 1:
            if char_rect.colliderect(first_rect): 
                game_window.fill((200, 200, 200))
                info1 = small_font.render(info[103 + selection_number].strip(), True, (0, 0, 0))
                cpu1_bench = py.image.load("images/ryzen 3 benchmark.png")
                cpu1_bench = py.transform.scale (cpu1_bench, (700, 300))
                info1_rect = info1.     get_rect(center=     (800, 500))
                cpu1_rect  = cpu1_bench.get_rect(center=     (800, 700))
                game_window.blit(info1,      info1_rect)
                game_window.blit(cpu1_bench, cpu1_rect)
                
            elif char_rect.colliderect(second_rect):
                game_window.fill((200, 200, 200))
                info2 = small_font.render(info[113 + selection_number].strip(), True, (0, 0, 0))
                cpu2_bench = py.image.load("images/intel i3 benchmark.png")
                cpu2_bench = py.transform.scale (cpu2_bench, (700, 300))
                info2_rect = info2.     get_rect(center=     (800, 500))
                cpu2_rect  = cpu2_bench.get_rect(center=     (800, 700))
                game_window.blit(info2,      info2_rect)
                game_window.blit(cpu2_bench, cpu2_rect)

        # gpu benchmarks
        elif selection_number == 5:
            if char_rect.colliderect(first_rect): 
                game_window.fill((200, 200, 200))
                info1 = small_font.render(info[103 + selection_number].strip(), True, (0, 0, 0))
                gpu1_bench = py.image.load("images/4080 benchmark.png")
                info1_rect = info1.     get_rect(center=(800, 500))
                gpu1_rect  = gpu1_bench.get_rect(center=(800, 700))
                game_window.blit(info1,      info1_rect)
                game_window.blit(gpu1_bench, gpu1_rect)
                
            elif char_rect.colliderect(second_rect):
                game_window.fill((200, 200, 200))
                info2 = small_font.render(info[113 + selection_number].strip(), True, (0, 0, 0))
                gpu2_bench = py.image.load("images/3060 benchmark.png")
                info2_rect = info2.     get_rect(center=(800, 500))
                gpu2_rect  = gpu2_bench.get_rect(center=(800, 700))
                game_window.blit(info2,      info2_rect)
                game_window.blit(gpu2_bench, gpu2_rect)

            elif char_rect.colliderect(third_rect):
                game_window.fill((200, 200, 200))
                info3 = small_font.render(info[113 + selection_number].strip(), True, (0, 0, 0))
                gpu3_bench = py.image.load("images/1650 benchmark.png")
                info3_rect = info3.     get_rect(center=(800, 500))
                gpu3_rect  = gpu3_bench.get_rect(center=(800, 700))
                game_window.blit(info3,      info3_rect)
                game_window.blit(gpu3_bench, gpu3_rect)

        # other information
        elif selection_number != 0:
            if char_rect.colliderect(first_rect): 
                game_window.fill((200, 200, 200))
                info1 = small_font.render(info[103 + selection_number].strip(), True, (0, 0, 0))
                info1_rect = info1.get_rect(center=(800, 500))
                game_window.blit(info1, info1_rect)

            elif char_rect.colliderect(second_rect):
                game_window.fill((200, 200, 200))
                info2 = small_font.render(info[113 + selection_number].strip(), True, (0, 0, 0))
                info2_rect = info2.get_rect(center=(800, 500))
                game_window.blit(info2, info2_rect)

            elif char_rect.colliderect(third_rect):
                game_window.fill((200, 200, 200))
                info3 = small_font.render(info[123 + selection_number].strip(), True, (0, 0, 0))
                info3_rect = info3.get_rect(center=(800, 500))
                game_window.blit(info3, info3_rect)

    

    # this deals with everything that can happen when the user presses enter
    if keys[py.K_SPACE]:
        # sets a variable that will be used to determine if the motherboard the user chooses is compatible with the cpu
        if selection_number == 1:
            if   char_rect.colliderect(first_rect) : cpu_type = 1
            elif char_rect.colliderect(second_rect): cpu_type = 2

        if selection_number == 0:
            # set the budget
            if   char_rect.colliderect(first_rect)  and choice0 != 1: budget, choice0 = 3000, 1
            elif char_rect.colliderect(second_rect) and choice0 != 2: budget, choice0 = 1500, 2
            elif char_rect.colliderect(third_rect)  and choice0 != 3: budget, choice0 = 1000, 3
            # reset the options
            choice1 = 0
            choice2 = 0
            choice3 = 0
            choice4 = 0
            choice5 = 0
            choice6 = 0
            choice7 = 0
            choice8 = 0
            choice9 = 0

        # this figures out which choice variable the select function needs to look at in order to work properly
        def select_find():
            if selection_number == 0: select(choice0)
            if selection_number == 1: select(choice1)
            if selection_number == 2: select(choice2)
            if selection_number == 3: select(choice3)
            if selection_number == 4: select(choice4)
            if selection_number == 5: select(choice5)
            if selection_number == 6: select(choice6)
            if selection_number == 7: select(choice7)
            if selection_number == 8: select(choice8)
            if selection_number == 9: select(choice9)

        # this makes sure that you can choose options, but not the same one more than once.
        def select(choice):
            global choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8, choice9, budget

            if selection_number != 0:
                if selection_number == 2:
                    if char_rect.colliderect(first_rect) and choice == 0:
                        if cpu_type == 2 or cpu_type == 0:
                            # make a box flash red if you can't choose it
                            for i in range(3):
                                py.draw.rect(game_window, (255, 0, 0), (0, 0, 500, 660), 10)
                                py.time.delay(200)
                                py.display.update()
                                py.draw.rect(game_window, (0, 255, 0), (0, 0, 500, 660), 10)
                                py.time.delay(200)
                                py.display.update()
                        else:
                            if budget  >= int(info[73 + selection_number].strip()): 
                                budget -= int(info[73 + selection_number].strip())
                                choice2 = 1
                                
                    elif char_rect.colliderect(second_rect) and choice == 0:
                        if cpu_type == 1 or cpu_type == 0:
                            for i in range(3):
                                py.draw.rect(game_window, (255, 0, 0), (1100, 0, 500, 660), 10)
                                py.time.delay(200)
                                py.display.update()
                                py.draw.rect(game_window, (0, 255, 0), (1100, 0, 500, 660), 10)
                                py.time.delay(200)
                                py.display.update()
                        else:
                            if budget  >= int(info[84 + selection_number].strip()): 
                                budget -= int(info[84 + selection_number].strip())
                                choice2 = 2

                elif char_rect.colliderect(first_rect) and choice == 0:
                    if budget  >= int(info[73 + selection_number].strip()): 
                        budget -= int(info[73 + selection_number].strip())
                        if selection_number == 1: choice1 = 1
                        if selection_number == 2: choice2 = 1
                        if selection_number == 3: choice3 = 1
                        if selection_number == 4: choice4 = 1
                        if selection_number == 5: choice5 = 1
                        if selection_number == 6: choice6 = 1
                        if selection_number == 7: choice7 = 1
                        if selection_number == 8: choice8 = 1
                        if selection_number == 9: choice9 = 1
                        
                    else:
                        for i in range(3):
                            budget_text = main_font.render("Budget: $" + str(budget), True, (255, 0, 0))
                            py.draw.rect(game_window, (0, 0, 0), (-100, 650, 3000, 3000), 10)
                            game_window.blit(budget_text, budget_rect)
                            py.time.delay(200)
                            py.display.update()
                            budget_text = main_font.render("Budget: $" + str(budget), True, (0, 0, 0))
                            py.draw.rect(game_window, (0, 0, 0), (-100, 650, 3000, 3000), 10)
                            game_window.blit(budget_text, budget_rect)
                            py.time.delay(200)
                            py.display.update()

                elif char_rect.colliderect(second_rect) and choice == 0: 
                    if budget  >= int(info[84 + selection_number].strip()): 
                        budget -= int(info[84 + selection_number].strip())
                        if selection_number == 1: choice1 = 2
                        if selection_number == 2: choice2 = 2
                        if selection_number == 3: choice3 = 2
                        if selection_number == 4: choice4 = 2
                        if selection_number == 5: choice5 = 2
                        if selection_number == 6: choice6 = 2
                        if selection_number == 7: choice7 = 2
                        if selection_number == 8: choice8 = 2
                        if selection_number == 9: choice9 = 2
                        
                    else:
                        for i in range(3):
                            budget_text = main_font.render("Budget: $" + str(budget), True, (255, 0, 0))
                            game_window.blit(budget_text, budget_rect)
                            py.time.delay(200)
                            py.display.update()
                            budget_text = main_font.render("Budget: $" + str(budget), True, (0, 0, 0))
                            game_window.blit(budget_text, budget_rect)
                            py.time.delay(200)
                            py.display.update()
                elif char_rect.colliderect(third_rect) and choice == 0: 
                    if budget  >= int(info[95 + selection_number].strip()): 
                        budget -= int(info[95 + selection_number].strip())
                        if selection_number == 5: choice5 = 3
                        if selection_number == 6: choice6 = 3
                        if selection_number == 7: choice7 = 3
                        
                        
                    else:
                        for i in range(3):
                            budget_text = main_font.render("Budget: $" + str(budget), True, (255, 0, 0))
                            game_window.blit(budget_text, budget_rect)
                            py.time.delay(200)
                            py.display.update()
                            budget_text = main_font.render("Budget: $" + str(budget), True, (0, 0, 0))
                            game_window.blit(budget_text, budget_rect)
                            py.time.delay(200)
                            py.display.update()
        select_find()
        py.time.delay(100)



    # button functions to clear current choice
    def clear_find():
        if selection_number == 1: clear(choice1)
        if selection_number == 2: clear(choice2)
        if selection_number == 3: clear(choice3)
        if selection_number == 4: clear(choice4)
        if selection_number == 5: clear(choice5)
        if selection_number == 6: clear(choice6)
        if selection_number == 7: clear(choice7)
        if selection_number == 8: clear(choice8)
        if selection_number == 9: clear(choice9)

    def clear(choice):
        global budget, choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8, choice9
        if selection_number == 1 or selection_number == 2:
            if   choice1 == 1: budget += int(info[74].strip())
            elif choice1 == 2: budget += int(info[85].strip())
            if   choice2 == 1: budget += int(info[75].strip())
            elif choice2 == 2: budget += int(info[86].strip())
        else:
            if   choice == 1: budget += int(info[73 + selection_number].strip())
            elif choice == 2: budget += int(info[84 + selection_number].strip())
            elif choice == 3: budget += int(info[95 + selection_number].strip())
        if selection_number == 1: choice1 = 0
        if selection_number == 1: choice2 = 0
        if selection_number == 2: choice2 = 0
        if selection_number == 2: choice1 = 0
        if selection_number == 3: choice3 = 0
        if selection_number == 4: choice4 = 0
        if selection_number == 5: choice5 = 0
        if selection_number == 6: choice6 = 0
        if selection_number == 7: choice7 = 0
        if selection_number == 8: choice8 = 0
        if selection_number == 9: choice9 = 0
        py.time.delay(250)



    # makes sure a box is highlighted permanently when it is chosen
    def highlight_find():
        if selection_number == 1: highlight(choice1)
        if selection_number == 2: highlight(choice2)
        if selection_number == 3: highlight(choice3)
        if selection_number == 4: highlight(choice4)
        if selection_number == 5: highlight(choice5)
        if selection_number == 6: highlight(choice6)
        if selection_number == 7: highlight(choice7)
        if selection_number == 8: highlight(choice8)
        if selection_number == 9: highlight(choice9)

    def highlight(choice):
        global first_box_color, second_box_color, third_box_color
        if choice == 1: first_box_color  = (0, 255, 0)
        if choice == 2: second_box_color = (0, 255, 0)
        if choice == 3: third_box_color  = (0, 255, 0)

    highlight_find()
    
        

    # button that will be displayed when the user has chosen all components.
    if choice0 != 0 and choice1 != 0 and choice2 != 0 and choice3 != 0 and choice4 != 0 and choice5 != 0 and choice6 != 0 and choice7 != 0 and choice8 != 0 and choice9 != 0:
        py.draw.rect(game_window, buy_box_color, (731, 899, 140, 90), 10)
        buy_text = main_font.render("Buy", True, (0, 0, 0))
        buy_rect = buy_text.get_rect(center=(800, 940))
        game_window.blit(buy_text, buy_rect)

        if char_rect.colliderect(buy_rect): buy_box_color = (0, 255, 0)
        else                              : buy_box_color = (0, 0, 0)

        if keys[py.K_SPACE]:
            if char_rect.colliderect(buy_rect):
                if selection_number == 10: play_game = False
                else: 
                    cost, selection_number = 0, 10
                    cost += int(info[11 * choice1 + 63].strip()) + int(info[11 * choice2 + 64].strip()) + int(info[11 * choice3 + 65].strip()) + int(info[11 * choice4 + 66].strip()) + int(info[11 * choice5 + 67].strip()) + int(info[11 * choice6 + 68].strip()) + int(info[11 * choice7 + 69].strip()) + int(info[11 * choice8 + 70].strip()) + int(info[11 * choice9 + 71].strip())
                py.time.delay(250)

        if selection_number == 10:
            # text
            cart_text        = main_font.render("Cart:",           True, (0, 0, 0))
            price_text       = main_font.render("Price:",          True, (0, 0, 0))
            budget_text      = main_font.render("Budget:",         True, (0, 0, 0))
            total_budget     = py.image.load  (info[11 * choice0].strip()        )
            total_cost       = main_font.render("Cost:",           True, (0, 0, 0))
            cost_text        = main_font.render("$" + str(cost),   True, (0, 0, 0))
            extra_budget     = main_font.render("Extra:",          True, (0, 0, 0))
            remaining_budget = main_font.render("$" + str(budget), True, (0, 0, 0))
            other_text       = main_font.render(info[132].strip(), True, (0, 0, 0))

            # rectangles
            cart_rect         = cart_text.       get_rect(center=(75,  100))
            price_rect        = price_text.      get_rect(center=(75,  240))
            budget_rect       = budget_text.     get_rect(center=(75,  380))
            total_budget_rect = total_budget.    get_rect(center=(225, 380))
            cost_rect         = total_cost.      get_rect(center=(75,  520))
            cost_text_rect    = cost_text.       get_rect(center=(225, 520))
            extra_rect        = extra_budget.    get_rect(center=(75,  640))
            remaining_rect    = remaining_budget.get_rect(center=(225, 640))
            other_rect        = other_text.      get_rect(center=(800, 700))

            # add text and rectangles to window
            game_window.blit(cart_text,         cart_rect)
            game_window.blit(price_text,        price_rect)
            game_window.blit(budget_text,       budget_rect)
            game_window.blit(total_budget,      total_budget_rect)
            game_window.blit(total_cost,        cost_rect)
            game_window.blit(cost_text,         cost_text_rect)
            game_window.blit(extra_budget,      extra_rect)
            game_window.blit(remaining_budget,  remaining_rect)
            game_window.blit(other_text,        other_rect)

            # image boxes
            py.draw.rect(game_window, (0, 0, 0), (150,  25, 150, 150), 10)
            py.draw.rect(game_window, (0, 0, 0), (310,  25, 150, 150), 10)
            py.draw.rect(game_window, (0, 0, 0), (470,  25, 150, 150), 10)
            py.draw.rect(game_window, (0, 0, 0), (630,  25, 150, 150), 10)
            py.draw.rect(game_window, (0, 0, 0), (790,  25, 150, 150), 10)
            py.draw.rect(game_window, (0, 0, 0), (950,  25, 150, 150), 10)
            py.draw.rect(game_window, (0, 0, 0), (1110, 25, 150, 150), 10)
            py.draw.rect(game_window, (0, 0, 0), (1270, 25, 150, 150), 10)
            py.draw.rect(game_window, (0, 0, 0), (1430, 25, 150, 150), 10)

            # images and prices
            if choice1 != 0:
                item1            = py.image.load   (      info[11 * choice1 + 1 ].strip())
                item1_price      = main_font.render("$" + info[11 * choice1 + 63].strip(), True, (0, 0, 0))
                item1            = py.transform.scale  (item1, (125, 125))
                item1_rect       = item1.      get_rect(center=(225, 100))
                item1_price_rect = item1_price.get_rect(center=(225, 240))
                game_window.blit(item1,       item1_rect)
                game_window.blit(item1_price, item1_price_rect)
            if choice2 != 0:
                item2            = py.image.load   (      info[11 * choice2 + 2 ].strip())
                item2_price      = main_font.render("$" + info[11 * choice2 + 64].strip(), True, (0, 0, 0))
                item2            = py.transform.scale  (item2, (125, 125))
                item2_rect       = item2.      get_rect(center=(385, 100))
                item2_price_rect = item2_price.get_rect(center=(385, 240))
                game_window.blit(item2,       item2_rect)
                game_window.blit(item2_price, item2_price_rect)
            if choice3 != 0:
                item3            = py.image.load   (      info[11 * choice3 + 3 ].strip())
                item3_price      = main_font.render("$" + info[11 * choice3 + 65].strip(), True, (0, 0, 0))
                item3            = py.transform.scale  (item3, (125, 125))
                item3_rect       = item3.      get_rect(center=(545, 100))
                item3_price_rect = item3_price.get_rect(center=(545, 240))
                game_window.blit(item3,       item3_rect)
                game_window.blit(item3_price, item3_price_rect)
            if choice4 != 0:
                item4            = py.image.load   (      info[11 * choice4 + 4 ].strip())
                item4_price      = main_font.render("$" + info[11 * choice2 + 66].strip(), True, (0, 0, 0))
                item4            = py.transform.scale  (item4, (125, 125))
                item4_rect       = item3.      get_rect(center=(705, 100))
                item4_price_rect = item4_price.get_rect(center=(705, 240))
                game_window.blit(item4,       item4_rect)
                game_window.blit(item4_price, item4_price_rect)
            if choice5 != 0:
                item5            = py.image.load   (      info[11 * choice5 + 5 ].strip())
                item5_price      = main_font.render("$" + info[11 * choice2 + 67].strip(), True, (0, 0, 0))
                item5            = py.transform.scale  (item5, (125, 125))
                item5_rect       = item5.      get_rect(center=(865, 100))
                item5_price_rect = item5_price.get_rect(center=(865, 240))
                game_window.blit(item5,       item5_rect)
                game_window.blit(item5_price, item5_price_rect)
            if choice6 != 0:
                item6            = py.image.load   (      info[11 * choice6 + 6 ].strip())
                item6_price      = main_font.render("$" + info[11 * choice2 + 68].strip(), True, (0, 0, 0))
                item6            = py.transform.scale  (item6, (125,  125))
                item6_rect       = item3.      get_rect(center=(1025, 100))
                item6_price_rect = item6_price.get_rect(center=(1025, 240))
                game_window.blit(item6,       item6_rect)
                game_window.blit(item6_price, item6_price_rect)
            if choice7 != 0:
                item7            = py.image.load   (      info[11 * choice7 + 7 ].strip())
                item7_price      = main_font.render("$" + info[11 * choice2 + 69].strip(), True, (0, 0, 0))
                item7            = py.transform.scale  (item7, (125,  125))
                item7_rect       = item7.      get_rect(center=(1185, 100))
                item7_price_rect = item7_price.get_rect(center=(1185, 240))
                game_window.blit(item7,       item7_rect)
                game_window.blit(item7_price, item7_price_rect)
            if choice8 != 0:
                item8            = py.image.load   (      info[11 * choice8 + 8 ].strip())
                item8_price      = main_font.render("$" + info[11 * choice2 + 70].strip(), True, (0, 0, 0))
                item8            = py.transform.scale  (item8, (125,  125))
                item8_rect       = item8.      get_rect(center=(1345, 100))
                item8_price_rect = item8_price.get_rect(center=(1345, 240))
                game_window.blit(item8,       item8_rect)
                game_window.blit(item8_price, item8_price_rect)
            if choice9 != 0:
                item9            = py.image.load   (      info[11 * choice9 + 9 ].strip())
                item9_price      = main_font.render("$" + info[11 * choice2 + 71].strip(), True, (0, 0, 0))
                item9            = py.transform.scale  (item9, (125,  125))
                item9_rect       = item9.      get_rect(center=(1505, 100))
                item9_price_rect = item9_price.get_rect(center=(1505, 240))
                game_window.blit(item9,       item9_rect)
                game_window.blit(item9_price, item9_price_rect)



    # this displays the controls when the user presses 'h'
    def help():
        # clear the background
        game_window.fill((200, 200, 200))

        # text
        wasd            = main_font.render("use WASD to move around",         True, (0, 0, 0))
        left_arrow_key  = main_font.render("Left Arrow = previous option",    True, (0, 0, 0))
        right_arrow_key = main_font.render("Right Arrow = next option",       True, (0, 0, 0))
        enter_key       = main_font.render("Space = choose option",           True, (0, 0, 0))
        backspace_key   = main_font.render("Backspace = clear option choice", True, (0, 0, 0))
        escape_key      = main_font.render("Escape = close program",          True, (0, 0, 0))
        info_key        = main_font.render("i = display info of item",        True, (0, 0, 0))

        # place text
        game_window.blit(wasd,            (100, 100))
        game_window.blit(left_arrow_key,  (100, 200))
        game_window.blit(right_arrow_key, (100, 300))
        game_window.blit(enter_key,       (100, 400))
        game_window.blit(backspace_key,   (100, 500))
        game_window.blit(escape_key,      (100, 600))
        game_window.blit(info_key,        (100, 700))
        py.time.delay(100)

    

    # keybindings
    if keys[py.K_a]:
        # move left
        if x > -10 : x -= 5

    if keys[py.K_d]:
        # move right
        if x < 1405: x += 5

    if keys[py.K_s]:
        # move down
        if y < 810 : y += 5

    if keys[py.K_w]:
        # move up
        if y > -25 : y -= 5

    if keys[py.K_LEFT]:
        # go back one choice
        if budget != "not chosen": 
            if selection_number > 0: selection_number -= 1; py.time.delay(250)

    if keys[py.K_RIGHT]:
        # go forwards one choice
        if budget != "not chosen": 
            if selection_number < 9: selection_number += 1; py.time.delay(250)

    if keys[py.K_ESCAPE]: 
        # quit program
        play_game = False

    if keys[py.K_BACKSPACE]: 
        # clear choice
        clear_find()

    if keys[py.K_h]: 
        # display keybinds
        help()

    if keys[py.K_i]: 
        # disply additional information
        information()

    for event in events:
        # close program
        if event.type == py.QUIT: play_game = False

    py.display.update()

    py.time.delay(25)
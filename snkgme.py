import pygame
import random
import os

x = pygame.init()
pygame.mixer.init()
# PROJECT FLAPPY

# creating window
scr_wdth = 1400
scr_hight = 760
gameWindow = pygame.display.set_mode((scr_wdth,scr_hight))
pygame.display.set_caption("A Gift To my Dearest Freind PRANAV")
pygame.display.update()

# background image
bgim = pygame.image.load("game_images\snkbg.jpg.jfif")
bgim = pygame.transform.scale(bgim, (scr_wdth,scr_hight)).convert_alpha() # this convert alpha used just so that no eveft should be there on image after running the fps

# Game start image
strtimg = pygame.image.load("game_images\strtgm.jfif")
strtimg = pygame.transform.scale(strtimg,(scr_wdth,scr_hight)).convert_alpha()

# Game over Image
gmover = pygame.image.load("game_images\gmover2.jfif")
gmover = pygame.transform.scale(gmover,(scr_wdth,scr_hight)).convert_alpha()

# sounds
choosing_eat_sound = random.choice(["eat_sounds\_Funny_meme_sound_no_copyright_BACKGROUND_MUSIC_gaming_omRZLUvEjIg.mp3","eat_sounds\Burp_Sound_Effect_HD__NJZDf1HaF6k_140.mp3","eat_sounds\Hehe_Boy_Meme_Sound_Effect_HD__QM6GaoPDv2k_140.mp3","eat_sounds\Love_Eating_Sound_Effect_HD__GOrM8Z_FFCQ_140.mp3"])
eat_sound = pygame.mixer.Sound(choosing_eat_sound)


choosing_ded_sound = random.choice(["game_fcked up sound\snk_hit.mp3","game_fcked up sound\AAAAUUUGHHHH_Meme_Sound_Effect_BmbM5B4NjxY_140.mp3","game_fcked up sound\AHHHHHHH_sound_effect_hySmztVCfpY_140.mp3","game_fcked up sound\GET_THE_FUCK_OUT_OF_HERE_Sound_Effect_DkMMTVsqOxc_140.mp3","game_fcked up sound\It_was_at_this_moment_he_knew_he_fucked_up_Sound_Effec_wCj1ZfApGYA.mp3","game_fcked up sound\Shut_up_sound_effect_JF1I6h9y_To_140.mp3"])
ded_sound = pygame.mixer.Sound(choosing_ded_sound)



fps = 60 # frame per second
clock = pygame.time.Clock()

font = pygame.font.SysFont(None,55) # adding score board on the screen



def text_screen(text, color, x, y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow, color, snk_lst, snake_size):

    for x,y in snk_lst:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size]) #creating head of the snake

# GAME COLORS

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
scr_color = (128,0,128)

# WELCOME SCREEN

def welcome():
    str_music = "game_start_sounds\_MDK_Press_Start_FREE_DOWNLOAD__XoLouT7TqZY_140.mp3"
    pygame.mixer.music.load(str_music)
    pygame.mixer.music.play()
    game_exit = False
    while not game_exit:
        
        gameWindow.fill(white)
        gameWindow.blit(strtimg,(0,0))
        # text_screen("CHALIYE SHURU KARTE HAI!",black,100,250) 
        # text_screen("press SPACE to start....",black,100,300) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("game_start_sounds\snk_theme.mp3")
                    pygame.mixer.music.play(-1)
                    gameloop()    
        pygame.display.update()
        clock.tick(fps)

# CREATING GAME LOOP

def gameloop():

    # GAME SPECIFIC VARIABLES
    game_exit = False
    game_over = False
    snake_x = 45 # will tell from where snake should be there on x coordinate of the screen
    snake_y = 55 # will tell from where snake should be there on y coordinate of the screen
    snake_size = 10
    snake_velx = 0 # gving some velocity to snake
    snake_vely = 0

    if (not os.path.exists("hiscore_snk.txt")):
        with open("hiscore_snk.txt","w") as f:
            f.write("0")

    with open("hiscore_snk.txt","r") as f:
        hiscore = f.read()

    food_x = random.randint(20,scr_wdth/2) # will tell from where food should be there on x coordinate of the screen, well it'll be generated randomly anywhere on the screen because we're using random module
    food_y = random.randint(20,scr_hight/2) # will tell from where food should be there on y coordinate of the screen

    snk_lst = []
    snk_len = 1

    vel_value = 4

    score = 0

    


    while not game_exit: # just a tip- if you wanna make a fast game, then try not to put much things isnide the game loop

        if game_over:

            with open("hiscore_snk.txt","w") as f:
                f.write(str(hiscore))

            gameWindow.fill(white)
            gameWindow.blit(gmover,(0,0))
            # text_screen("Game Over, press ENTER to continue",red,100,250)

            for event in pygame.event.get(): # taking event one by one from pygame .event.get(), it tells whatever we do on screen and whenever we press x on top right corner, it quits
                if event.type == pygame.QUIT:
                    game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:         
            for event in pygame.event.get(): # taking event one by one from pygame .event.get(), it tells whatever we do on screen and whenever we press x on top right corner, it quits
                if event.type == pygame.QUIT:
                    game_exit = True

                if event.type == pygame.KEYDOWN: # agar keyboard me koi key press ki gayi ho to

                    if event.key == pygame.K_RIGHT:
                        snake_velx = vel_value # moving snake in positive x direction on pressing right arrow key and keeps on updating because of line 53 and 54 in while loop
                        snake_vely = 0 # putting vel of snake in v direction 0, whenever it's moving in x direction so that, it should avoid moving diagonally like resultant, we will do the same with velx while changing the vely
                    
                    if event.key == pygame.K_LEFT:
                        snake_velx = -vel_value
                        snake_vely = 0

                    if event.key == pygame.K_UP:
                        snake_vely = -vel_value
                        snake_velx = 0

                    if event.key == pygame.K_DOWN:
                        snake_vely = vel_value
                        snake_velx = 0

            snake_x += snake_velx # while loop updating the speed of the snake
            snake_y += snake_vely

            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6: # abs will be working for giving it an abstract value, not much precised, so that even if x,y coordinates of food and snake are little but farrer from each other then also it should consider it as collision
                eat_sound.play()
                score += 10
                

                food_x = random.randint(20,scr_wdth/2) # will tell from where food should be there on x coordinate of the screen, well it'll be generated randomly anywhere on the screen because we're using random module
                food_y = random.randint(20,scr_hight/2) # will tell from where food should be there on y coordinate of the screen
                snk_len += 4

                if score>int(hiscore):
                    hiscore = score


            gameWindow.fill(green)
            gameWindow.blit(bgim, (0,0))
            text_screen(f"SCORE: {score}        HIGHSCORE: {hiscore}",scr_color,5,5)
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size]) # drwaing food

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_lst.append(head)

            if len(snk_lst)>snk_len:
                del snk_lst[0]

            if snake_x<0 or snake_x>scr_wdth or snake_y<0 or snake_y>scr_hight:
                ded_sound.play()
                pygame.mixer.music.load("game_start_sounds\Moye_moye_rbchcJjEwL4_140.mp3")
                pygame.mixer.music.play()
                game_over = True

            if head in snk_lst[:-1]:
                ded_sound.play()
                pygame.mixer.music.load("game_start_sounds\Moye_moye_rbchcJjEwL4_140.mp3")
                pygame.mixer.music.play()
                game_over = True
                

            plot_snake(gameWindow,black,snk_lst,snake_size)

        pygame.display.update()
        clock.tick(fps) # whatever you wrote inside the while loop till before this line will be inside the while loop, but now, this line update the screen that much time as you want in a "single second!"
    pygame.quit()
    quit()                

welcome()  

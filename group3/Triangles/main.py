import pygame, sys, math, random
from pygame.locals import *

## time stamp that marks when the game starts
start_time = pygame.time.get_ticks()

try:
    import android
except ImportError:
    android = None

        
class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        RED = (255, 0, 0)
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = random.randrange(0, 470, 7)
        self.image.fill(RED)
        
    
    def update(self):
        self.rect.bottom = self.rect.bottom + 7
        

## Horizontal Bomb sprite class
class Bomb2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        PURPLE = (231, 165, 255)
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()
        self.rect.left = 480
        self.rect.top = random.randrange(0, 320, 7)
        self.image.fill(PURPLE)
    
    def update(self):
        self.rect.left = self.rect.left - 7
        
        
## Side bomb sprite class
class Bomb_rand1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ORANGE = (255, 151, 23)
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()
        self.rect.left = random.randrange(0, 30, 7)
        self.rect.top = 0
        self.image.fill(ORANGE)
    
    def update(self):
        self.rect.bottom = self.rect.bottom + 7
        

## Side2 bomb sprite class
class Bomb_rand2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        GREEN = (24, 226, 44)
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()
        self.rect.left = random.randrange(440, 470, 7)
        self.rect.top = 0
        self.image.fill(GREEN)
    
    def update(self):
        self.rect.bottom = self.rect.bottom + 7
        
        
## Side 3 bomb sprite class        
class Bomb_rand3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        PURPLE = (190, 23, 255)
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()
        self.rect.left = 480
        self.rect.top = random.randrange(280, 310, 7)
        self.image.fill(PURPLE)
    
    def update(self):
        self.rect.left = self.rect.left - 7        


## sprite class for the bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self, player_rect, direction):
        pygame.sprite.Sprite.__init__(self)
        WHITE = (255, 255, 255)
        self.direction = direction
        self.image = pygame.Surface((5, 5))
        self.rect = self.image.get_rect()
        self.rect.center = player_rect.center
        self.image.fill(WHITE)
        
        
    def update(self):
        if self.direction == "right":
            self.rect.right = self.rect.right + 9
        if self.direction == "left":
            self.rect.left = self.rect.left - 9
        if self.direction == "up":
            self.rect.top = self.rect.top - 9
        if self.direction == "down":
            self.rect.bottom = self.rect.bottom + 9
        
        

pygame.init()
clock = pygame.time.Clock()
FPS = 30

YELLOW = (239, 251, 3)
GREEN = (3, 251, 143)
PLAYER_GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (188, 0, 255)
LIGHT_BLUE = (60, 223, 245)
BLUE_2 = (64, 60, 245)
PINK = (235, 60, 245)
ORANGE = (255, 151, 23)
WHITE = (255, 255, 255)
WHITE_2 = (199, 199, 199)
DARK_RED = (199, 25, 25)

## initialize fonts
timer_font = pygame.font.Font("img/animeace2_reg.ttf", 16)

direction = "down"

## Setup for rectangles
control_size = 60
center_rect = pygame.Rect(0, 0, control_size, control_size)
center_rect.center = (90, 230)

external_rect = pygame.Rect(0, 0, control_size * math.sqrt(3) + control_size, control_size * math.sqrt(3) + control_size)
external_rect.center = center_rect.center

player_rect = pygame.Rect(200, 200, 30, 30)

## Setup for triangles
top_triangle_pointlist = (center_rect.topleft, center_rect.topright, (center_rect.centerx, external_rect.top))
right_triangle_pointlist = (center_rect.topright, center_rect.bottomright, (external_rect.right, center_rect.centery))
bottom_triangle_pointlist = (center_rect.bottomright, center_rect.bottomleft, (center_rect.centerx, external_rect.bottom))
left_triangle_pointlist = (center_rect.bottomleft, center_rect.topleft, (external_rect.left, center_rect.centery))

windowSurface = pygame.display.set_mode((480, 320), 0, 32)
#direction = "stop"


## Instantaiting the vertical bomb group
bomb = Bomb()
bomb_group = pygame.sprite.Group()
bomb_group.add(bomb)

## Instantaitating the horizontal bomb group
bomb2 = Bomb2()
bomb2_group = pygame.sprite.Group()
# bomb2_group.add(bomb2)


## Instantiating the random bomb group
bomb_rand1 = Bomb_rand1()
bomb_rand1_group = pygame.sprite.Group()
bomb_rand1_group.add(bomb_rand1)

##
bomb_rand2 = Bomb_rand2()
bomb_rand2_group = pygame.sprite.Group()
#bomb_rand2_group.add(bomb_rand2)

##
bomb_rand3 = Bomb_rand3()
bomb_rand3_group = pygame.sprite.Group()
#bomb_rand3_group.add(bomb_rand3)


## Instantiating the bullet group
# bullet = Bullet(player_rect, direction)
bullet_group = pygame.sprite.Group()
# bullet_group.add(bullet)


## bomb detection
current_time = pygame.time.get_ticks()
trigger = pygame.time.get_ticks() + 500
horiz_trigger = trigger
trigger_rand1 = trigger
trigger_rand2 = trigger
trigger_rand3 = trigger


## fonts for the gameOver screen
playAgain_font = pygame.font.Font("img/animeace2_reg.ttf", 40)
playAgain_rect = pygame.Rect(100, 150, 100, 30)

yes_font = pygame.font.Font("img/ASTONISH.TTF", 45)
yes_rect = pygame.Rect(50, 230, 60, 40)

no_font = pygame.font.Font("img/BLOODY.ttf", 45)
no_rect = pygame.Rect(300, 230, 60, 40)


gameOn = True

level = 1
minTrigger = 500
maxTrigger = 800

h_minTrigger = 700
h_maxTrigger = 1000



## rectangle to fire the bullet
fire_rect = pygame.Rect(380, 230, 50, 50)


## The counter for the shield
shield_counter = 3
shield_hits = 5
shield_state = False

zero = 1000




if android:
    android.init()
    android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


        elif event.type == KEYDOWN:
            if event.key == K_UP:
                direction = "up"
            elif event.key == K_DOWN:
                direction = "down"
            elif event.key == K_RIGHT:
                direction = "right"
            elif event.key == K_LEFT:
                direction = "left"
            elif event.key == K_SPACE:
                direction = "stop"
    
        
    
    ## gameover screen
    if gameOn == False:
        
        ## open the high score file
        score_file = open("score.txt", "r")
        score = score_file.readline()
        score_file.close()
        
        windowSurface.fill(BLACK)
        playAgain_surface = playAgain_font.render("Play Again?", True, YELLOW)
        yes_surface = yes_font.render("YES!", True, PLAYER_GREEN)
        no_surface = no_font.render("No...", True, RED)
        
        ## rectangle for high score
        highScore_surface = playAgain_font.render("High Score : " + str(score), True, LIGHT_BLUE)
        highScore_rect = pygame.Rect(15, 85, 200, 100)
        
        
        ## rectangle for resetting the high score
        reset_rect = pygame.Rect(10, 150, 70, 50)
        reset_text = no_font.render(" R ", True, BLACK)
        
        
        final_time = current_time / 1000.0
        final_time = "%.1f" % final_time
        playerScore_surface = playAgain_font.render("Your Score : " + str(final_time), True, PINK)
        playerScore_rect = pygame.Rect(5, 5, 200, 100)
        
        #pygame.draw.rect(windowSurface, PLAYER_GREEN, playAgain_rect)
        playAgain_surface.convert_alpha()
        windowSurface.blit(playAgain_surface, playAgain_rect)
        #pygame.draw.rect(windowSurface, PLAYER_GREEN, yes_rect)
        yes_surface.convert_alpha()
        windowSurface.blit(yes_surface, yes_rect)
        #pygame.draw.rect(windowSurface, PLAYER_GREEN, no_rect)
        no_surface.convert_alpha()
        windowSurface.blit(no_surface, no_rect)
        
        highScore_surface.convert_alpha()
        windowSurface.blit(highScore_surface, highScore_rect)
        playerScore_surface.convert_alpha()
        windowSurface.blit(playerScore_surface, playerScore_rect)
        
        
        pygame.draw.rect(windowSurface, RED, reset_rect)
        windowSurface.blit(reset_text, reset_rect)
        
        
        mouse_pos = pygame.mouse.get_pos()
        if yes_rect.collidepoint(mouse_pos):
            gameOn = True
            start_time = pygame.time.get_ticks()
            current_time = pygame.time.get_ticks() - start_time
            player_rect = pygame.Rect(200, 200, 30, 30)
            bomb_group.empty()
            bomb2_group.empty()
            bomb_rand1_group.empty()
            bomb_rand2_group.empty()
            bomb_rand3_group.empty()
            
            #direction = "down"
            bullet_group.empty()
            trigger = current_time + 500
            horiz_trigger = current_time + 500
            trigger_rand1 = current_time + 500
            trigger_rand2 = current_time + 500
            trigger_rand3 = current_time + 500
            level = 1
            minTrigger = 500
            maxTrigger = 800
            h_minTrigger = 600
            h_maxTrigger = 900
            shield_hits = 5
            shield_counter = 3
            shield_state = False
            
            ## updating the high score
            if float(final_time) > float(score):
                score_file = open("score.txt", "w")
                score_file.write(final_time)
                score_file.close()
        
                
                
        ## collision detection for resetting the score
        reset = zero / 1000.0
        reset = "%.1f" % reset
        if reset_rect.collidepoint(mouse_pos):
            score_file = open("score.txt", "w")
            score_file.write(reset)
            score_file.close()
        
        
        if no_rect.collidepoint(mouse_pos):
            ## updating the high score
            if float(final_time) > float(score):
                score_file = open("score.txt", "w")
                score_file.write(final_time)
                score_file.close()
            
            pygame.quit()
            sys.exit()
        
        pygame.display.update()
        
        
        
        
            
    else:
        windowSurface.fill(BLACK)
        
        if level >= 4:
            windowSurface.fill(WHITE)
        windowSurface.convert_alpha()
        pygame.draw.rect(windowSurface, GREEN, center_rect, 1)
        pygame.draw.rect(windowSurface, GREEN, external_rect, 1)
        
        top_triangle = pygame.draw.polygon(windowSurface, YELLOW, top_triangle_pointlist)
        right_triangle = pygame.draw.polygon(windowSurface, YELLOW, right_triangle_pointlist)
        bottom_triangle = pygame.draw.polygon(windowSurface, YELLOW, bottom_triangle_pointlist)
        left_triangle = pygame.draw.polygon(windowSurface, YELLOW, left_triangle_pointlist)
        
      
        
        pygame.draw.rect(windowSurface, PURPLE, fire_rect)
      
        
        ## bomb group drawing statements
        bomb_group.update()
        bomb_group.draw(windowSurface)
        
        ## horizontal bomb group drawing statements
        bomb2_group.update()
        bomb2_group.draw(windowSurface)
    
        
        ## random bomb group drawing statements
        bomb_rand1_group.update()
        bomb_rand1_group.draw(windowSurface)
        
        ##
        bomb_rand2_group.update()
        bomb_rand2_group.draw(windowSurface)
        
        ##
        bomb_rand3_group.update()
        bomb_rand3_group.draw(windowSurface)
        
        
        pygame.draw.rect(windowSurface, PLAYER_GREEN, player_rect)
        pygame.draw.circle(windowSurface, RED, player_rect.center, 12)
        
        
        
        
        
        mouse_pos = pygame.mouse.get_pos()
        
        ## shield control
        if fire_rect.collidepoint(mouse_pos):
            shield_state = True
            print ("shield state is on")
        
        if shield_state == True and shield_counter > 0:    
            shield = pygame.draw.circle(windowSurface, BLUE_2, player_rect.center, 30, 5)
            
            for bomb in bomb_group:
                if bomb.rect.colliderect(shield) and shield_hits > 0:
                    
                    bomb_group.remove(bomb)
                    shield_hits = shield_hits - 1
                    
                if shield_hits == 0:
                    shield_counter = shield_counter - 1
                    shield_hits = 5
                    shield_state = False
                    
                if shield_counter <= 0:
                    shield_hits = 0
                    
            
            
            for bomb2 in bomb2_group:
                if bomb2.rect.colliderect(shield) and shield_hits > 0:
                    bomb2_group.remove(bomb2)
                    shield_hits = shield_hits - 1
                    
                if shield_hits == 0:
                    shield_counter = shield_counter - 1
                    shield_hits = 5
                    shield_state = False
                    
            
            for bomb_rand1 in bomb_rand1_group:
                if bomb_rand1.rect.colliderect(shield) and shield_hits > 0:
                    bomb_rand1_group.remove(bomb_rand1)
                    shield_hits = shield_hits - 1
                    
                if shield_hits == 0:
                    shield_counter = shield_counter - 1
                    shield_hits = 5
                    shield_state = False
            
            for bomb_rand2 in bomb_rand2_group:
                if bomb_rand2.rect.colliderect(shield) and shield_hits > 0:
                    bomb_rand2_group.remove(bomb_rand2)
                    shield_hits = shield_hits - 1
                    
                if shield_hits == 0:
                    shield_counter = shield_counter - 1
                    shield_hits = 5
                    shield_state = False
            
            for bomb_rand3 in bomb_rand3_group:
                if bomb_rand3.rect.colliderect(shield) and shield_hits > 0:
                    bomb_rand3_group.remove(bomb_rand3)
                    shield_hits = shield_hits - 1
                    
                if shield_hits == 0:
                    shield_counter = shield_counter - 1
                    shield_hits = 5
                    shield_state = False
                    
                    
                    
        if shield_hits == 4:
            shield = pygame.draw.circle(windowSurface, LIGHT_BLUE, player_rect.center, 30, 5)
        if shield_hits == 3:
            shield = pygame.draw.circle(windowSurface, PLAYER_GREEN, player_rect.center, 30, 5)
        if shield_hits == 2:
            shield = pygame.draw.circle(windowSurface, PINK, player_rect.center, 30, 5)
        if shield_hits == 1:
            shield = pygame.draw.circle(windowSurface, DARK_RED, player_rect.center, 30, 5)
            
        
        warning_surface = timer_font.render("Shields left : " + str(shield_counter), False, RED)
        warning_surface.convert_alpha()
        windowSurface.blit(warning_surface, (280, 2))
                    
                    
        #    bullet_group.add(Bullet(player_rect, direction))
        #
        #bullet_group.update()
        #bullet_group.draw(windowSurface)
        
        

        if top_triangle.collidepoint(mouse_pos):
            direction = "up"
        elif right_triangle.collidepoint(mouse_pos):
            direction = "right"
        elif bottom_triangle.collidepoint(mouse_pos):
            direction = "down"
        elif left_triangle.collidepoint(mouse_pos):
            direction = "left"
        #elif center_rect.collidepoint(mouse_pos):
        #        direction = "stop"
    
        
        
        ## direction controls
        if direction == "up" and player_rect.top >= 0:
            player_rect.top = player_rect.top - 7
        if direction == "down" and player_rect.bottom <= 320:
            player_rect.bottom = player_rect.bottom + 7
        if direction == "right" and player_rect.right <= 480:
            player_rect.right = player_rect.right + 7
        if direction == "left" and player_rect.left >= 0:
            player_rect.left = player_rect.left - 7
            
        
       
    
        
    
        ## bomb drop controls
        current_time = pygame.time.get_ticks() - start_time
        
        if current_time > trigger:
            
            bomb_group.add(Bomb())
            trigger = current_time + random.randrange(minTrigger, maxTrigger, 5)
            
        for bomb in bomb_group:
            
            
            ## collision detection
            if bomb.rect.colliderect(player_rect):
                gameOn = False
                
            if bomb.rect.top > 320:
                
                bomb_group.remove(bomb)
                
        
        ## collision detection for the random bomb groups        
        for bomb_rand1 in bomb_rand1_group:
            if bomb_rand1.rect.colliderect(player_rect):
                gameOn = False
            if bomb_rand1.rect.top > 320:
                bomb_rand1_group.remove(bomb_rand1)
        
        ##        
        for bomb_rand2 in bomb_rand2_group:
            if bomb_rand2.rect.colliderect(player_rect):
                gameOn = False
            if bomb_rand2.rect.top > 320:
                bomb_rand2_group.remove(bomb_rand2)
        
        ##
        for bomb_rand3 in bomb_rand3_group:
            if bomb_rand3.rect.colliderect(player_rect):
                gameOn = False
            if bomb_rand3.rect.right < 0:
                bomb_rand3_group.remove(bomb_rand3)
        
        ## horizontal bomb drop controls
        current_time = pygame.time.get_ticks() - start_time
        if current_time > horiz_trigger and level >= 3:
        # if current_time > horiz_trigger:
            bomb2_group.add(Bomb2())
            horiz_trigger = current_time + random.randrange(h_minTrigger, h_maxTrigger, 5)
            
            
        ## random bomb drop controls
        current_time = pygame.time.get_ticks() - start_time
        if current_time > trigger_rand1:
            bomb_rand1_group.add(Bomb_rand1())
            trigger_rand1 = current_time + random.randrange(minTrigger, maxTrigger, 5)
            
        
        ##
        current_time = pygame.time.get_ticks() - start_time
        if current_time > trigger_rand2 and level >= 2:
            bomb_rand2_group.add(Bomb_rand2())
            trigger_rand2 = current_time + random.randrange(minTrigger, maxTrigger, 5)
            
        ##
        current_time = pygame.time.get_ticks() - start_time
        if current_time > trigger_rand3 and level >= 4:
            bomb_rand3_group.add(Bomb_rand3())
            trigger_rand3 = current_time + random.randrange(h_minTrigger, h_maxTrigger, 5)
        
        
            
        for bomb2 in bomb2_group:
            ## collision detection
            if bomb2.rect.colliderect(player_rect):
                gameOn = False
                end_time = current_time
                
            if bomb2.rect.left < 0:
                
                bomb2_group.remove(bomb2)
                
        
        timer = current_time / 1000.0
        level_timer = int(timer)
        timer = "%.1f" % timer
        timer = str(timer)
        ##print(timer)
        
        timer_surface = timer_font.render("Time : " + str(timer), False, YELLOW)
        timer_surface.convert_alpha()
        windowSurface.blit(timer_surface, (0,0))
        
        
        ## Incrementing the levels

    

        if level == 1 and level_timer > 5.0:
            level = 2
        if level == 2 and level_timer > 10:
            level = 3
        if level == 3 and level_timer > 15:
            level = 4
        if level == 4 and level_timer > 20:
            level = 5
        if level == 5 and level_timer > 25:
            level = 6
        if level == 6 and level_timer > 30:
            level = 7
        # print(level_timer, level)

        
        ## Setting the trigger for the levels
        if level == 2:
            minTrigger = 400
            maxTrigger = 700
        if level == 3:
            minTrigger = 300
            maxTrigger = 600
            
            h_minTrigger = 700
            h_maxTrigger = 1000
        if level == 4:
            minTrigger = 200
            maxTrigger = 500
            
            
        if level == 5:
            minTrigger = 100
            maxTrigger = 400
        if level == 6:
            minTrigger = 50
            maxTrigger = 300
        if level == 7:
            minTrigger = 40
            maxTrigger = 200
        
        
        
        
        
        
        clock.tick(FPS)
        pygame.display.update()

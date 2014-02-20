import pygame, sys
## Statement that allows users to acess pygame specific commands
from pygame.locals import *

try:
    import android
except ImportError:
    android = None

pygame.init()

if android:
    android.init()
    android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

FPS = 30
clock = pygame.time.Clock()


size = (480, 320)
screen = pygame.display.set_mode(size)

# define color using Red, Green, Blue values
# 0 is blank
# 255 is maximum
RED = (255, 0, 0)  # all red. no other color
BLACK = (0, 0, 0)

## set colors for the up/down rectangle
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (247, 41, 234)
YELLOW = (230, 255, 0)


# left edge of rectangle, top, width height
player_rect = pygame.Rect(0, 0, 64, 64)

## Create rectangles that will detect direction
up_rect = pygame.Rect(300, 100, 50, 50)
down_rect = pygame.Rect(300, 180, 50, 50)
right_rect = pygame.Rect(360, 140, 50, 50)
left_rect = pygame.Rect(235, 140, 50, 50)


map = pygame.image.load("Kai_map.png").convert_alpha()
map_rect = pygame.Rect(0, 0, 480, 320)

girl = pygame.image.load("girl.png").convert_alpha()

direction = "down"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        mouse_pos = pygame.mouse.get_pos()
        ## Check if the mouse_pos is within the rectangle
        if up_rect.collidepoint(mouse_pos):
            direction = "up"
        elif down_rect.collidepoint(mouse_pos):
            direction = "down"
        elif right_rect.collidepoint(mouse_pos):
            direction = "right"
        elif left_rect.collidepoint(mouse_pos):
            direction = "left"


    
    screen.blit(map, map_rect)
    
    
    screen.blit(girl, player_rect)
        
    ## draw the rectangles that will detect direction
    pygame.draw.rect(screen, GREEN, up_rect)
    pygame.draw.rect(screen, BLUE, down_rect)
    pygame.draw.rect(screen, YELLOW, right_rect)
    pygame.draw.rect(screen, PINK, left_rect)

    if direction == "down":
        player_rect.centery += 5
    elif direction == "up":
        player_rect.centery -= 5
    if direction == "right":
        player_rect.centerx += 5
    if direction == "left":
        player_rect.centerx -= 5


    if player_rect.bottom > size[1]:
        direction = "up"
    if player_rect.top < 0:
        direction = "down"
    if player_rect.right > size[0]:
        direction = "left"
    if player_rect.left < 0:
        direction = "right"
    
    
    clock.tick(FPS)
    pygame.display.update()

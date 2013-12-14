import pygame, sys

pygame.init()

# Frames Per Second
FPS = 30
clock = pygame.time.Clock()

size = (480, 320)
screen = pygame.display.set_mode(size)

# define color using Red, Green, Blue values
# 0 is blank
# 255 is maximum

RED = (255, 0, 0)  # all red. no other color
BLACK = (0, 0, 0)

# left edge of rectangle, top, width height
player_rect = pygame.Rect(0, 0, 64, 64)

direction = "down"


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if direction == "down":
        player_rect.centery += 1
    elif direction == "up":
        player_rect.centery -= 1

    if player_rect.bottom > size[1]:
        direction = "up"
    if player_rect.top < 0:
        direction = "down"
        

    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, player_rect)
    
    # slow the game down to 30 frames per second
    clock.tick(FPS)
    pygame.display.update()
        

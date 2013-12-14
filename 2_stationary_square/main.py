import pygame, sys

pygame.init()

size = (480, 320)
screen = pygame.display.set_mode(size)

# define color using Red, Green, Blue values
# 0 is blank
# 255 is maximum

RED = (255, 0, 0)  # all red. no other color

# left edge of rectangle, top, width height
player_rect = pygame.Rect(0, 0, 64, 64)
player = pygame.image.load("girl.png")



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.draw.rect(screen, RED, player_rect)

    # screen.blit(player, player_rect)

    
    pygame.display.update()
        

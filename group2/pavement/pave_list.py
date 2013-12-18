import pygame, sys

pygame.init()
screen = pygame.display.set_mode((480, 320))

clock = pygame.time.Clock()

tile = pygame.image.load("pavement.png")

# create an empty list for the pavement
pavement = []

# load 16 elements into the list. 
# each element is a rectangle
for x in range (0, 480 + 32, 32):
    pavement.append(pygame.Rect(x, 288, 32, 32))
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # if the right edge of the rectangle on the list is
    # off the screen, then delete it from the list
    # and add a rectangle on the right
    if pavement[0].right <= 0:
        pavement = pavement[1:]
        pavement.append(pygame.Rect(480, 288, 32, 32))

    for ground in pavement:
        ground.right -= 4
        screen.blit(tile, ground)
    print(len(pavement))
    clock.tick(20)
    pygame.display.update()

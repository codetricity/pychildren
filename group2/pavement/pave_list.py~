import pygame, sys

pygame.init()
screen = pygame.display.set_mode((480, 320))

class Tile(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.bottom = 320
        self.speed = 1


pavement = pygame.sprite.Group()

for x in range (0, 480 + 32, 32):
    tile = Tile("pavement.png")
    tile.rect.left = x
    pavement.add(tile)
    


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pavement.draw(screen)
    pygame.display.update()

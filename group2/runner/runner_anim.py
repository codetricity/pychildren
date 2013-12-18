import pygame, sys

pygame.init()

screen = pygame.display.set_mode((480, 320))

clock = pygame.time.Clock()
FPS = 30

mainsheet = pygame.image.load("walksheet.png")
sheet_size = mainsheet.get_size()
horiz_cells  = 6
vert_cells = 5
cell_width = sheet_size[0] / horiz_cells
cell_height = sheet_size[1] / vert_cells



cell_list = []
for y in range (0, sheet_size[1], cell_height):
    for x in range (0, sheet_size[0], cell_width):
        surface = pygame.Surface((cell_width, cell_height))
        surface.blit(mainsheet, (0,0), 
                     (x ,y, cell_width, cell_height))
        colorkey = surface.get_at((0,0))
        surface.set_colorkey(colorkey)
        cell_list.append(surface)

cell_position = 0

## set up background
background = pygame.image.load("wasteland.png")
bg_width = background.get_rect().right
bg_slice = pygame.Surface((480, 320))
bg_x = 0
bg_speed = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#    screen.fill((0,0,0))


    if bg_x < bg_width - 480:
        bg_x += bg_speed
        bg_slice.blit(background, (0,0), (bg_x, 0, 480, 320))

    screen.blit(bg_slice, (0,0))

    if cell_position < len(cell_list) - 1:

        cell_position += 1
    else:
        cell_position = 0

    screen.blit(cell_list[cell_position], (100, 10))

    clock.tick(FPS)
    pygame.display.update()
        
### http://pychildren.blogspot.com

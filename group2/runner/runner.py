import pygame, sys

class Animation:
    def __init__(self, sprite_file, grid_size):
        self.mainsheet = pygame.image.load(sprite_file)
        self.horiz_cells = grid_size[0]
        self.vert_cells = grid_size[1]
        self.animation_delay = 2
        self.current_delay = self.animation_delay
        self.cell_position = 0
        self.calc_size()
        self.screen_pos = (100, 20)

    def calc_size(self):
        self.sheet_size = self.mainsheet.get_size()        
        self.cell_width = self.sheet_size[0] / self.horiz_cells
        self.cell_height = self.sheet_size[1] / self.vert_cells
        self.rect = pygame.Rect(100, 0, self.cell_width, self.cell_height)
        self.rect.bottom = 320 - 16

    def load(self):
        self.cell_list = []
        for y in range (0, self.sheet_size[1], self.cell_height):
            for x in range(0, self.sheet_size[0], self.cell_width):
                self.surface = pygame.Surface((self.cell_width, self.cell_height))
                self.surface.blit(self.mainsheet, (0,0), 
                                  (x, 
                                  y,
                                  x + self.cell_width,
                                  y + self.cell_height))
                colorkey = self.surface.get_at((0,0))
                self.surface.set_colorkey(colorkey)
                self.surface.convert_alpha()
                self.small_surf = pygame.transform.scale(self.surface, 
                                                         (self.cell_width / 3,
                                                          self.cell_height / 3))
                # self.cell_list.append(self.small_surf)
                self.cell_list.append(self.surface)
        return(self.cell_list)

    def update(self):
        if self.current_delay > 0:
            self.current_delay -= 1
        else:
            self.current_delay = self.animation_delay
            if self.cell_position < len(self.cell_list) - 1:
                self.cell_position += 1
            else:
                self.cell_position = 0
        current_surf = self.cell_list[self.cell_position]
        return(current_surf)

class Counter:
    def __init__(self):
        self.RED = (255, 0, 0)
        self.cell_font = pygame.font.SysFont(None, 32)

    def update(self, cell_position):
        
        cell_number = self.cell_font.render("Frame: " + str(cell_position), True, self.RED)
        cell_number.convert()
        return(cell_number)
        
class Background:
    def __init__(self):
        self.background = pygame.image.load("wasteland.png")
        self.width = self.background.get_rect().right
        self.slice = pygame.Surface((480, 320))
        self.slice.convert()
        self.x = 0
        self.speed = 2


    def update(self):

        if self.x < self.width - 480:
            self.x += self.speed
            self.slice.blit(self.background, (0,0), (self.x, 0, 480+ self.x, 320))
        return (self.slice)

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 26))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.bottom = 320
    

pygame.init()

FPS = 50
clock = pygame.time.Clock()

screen = pygame.display.set_mode((480, 320))
        
runner = Animation("walksheet.png", (6, 5))
runner_list = runner.load()
counter = Counter()

background = Background()

ground_group = pygame.sprite.Group()

for x in range(0, 480, 32):
    ground = Ground()
    ground.rect.left = x
    ground_group.add(ground)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    runner_sprite = runner.update()


    screen.blit(background.update(), (0,0))
    # screen.fill((0,0,0))
    ground_group.draw(screen)
    screen.blit(runner_sprite, runner.rect)

    screen.blit(counter.update(runner.cell_position), (10, 50))

    clock.tick(FPS)
    pygame.display.update()

import pygame, sys, random, glob

def scroll(x, direction):
    if direction == "left":
        x = x - 1
    elif direction == "right":
        x = x + 1
    return (x)

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pavement.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = 320
    def update(self):
        self.rect.left -= 8

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("cactus.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = 288
        self.rect.left = 480

    def update(self):
        self.rect.left -= 8

class Tree(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/home_tree.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = 292
        self.rect.left = 480
        self.speed = 3
    def update(self):
        self.rect.left -= self.speed
    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_position = 0
        self.img_list = glob.glob("img/smurf*.png")
        self.image = pygame.image.load(self.img_list[self.img_position])
        self.rect = self.image.get_rect()
        self.rect.top = 160
        self.rect.left = 180
        self.jump = "stop"
        self.jump_number = 0
    
class innerPlayer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)    
        self.image = pygame.Surface((64, 110))
        self.rect = self.image.get_rect()

def jump_update(y, jump, number):
    jump_speed = 10
    if number == 1:
        if jump == "up" and y < 50:
            jump = "down"
    elif number == 2:
        if jump == "up" and y < -10:
            jump = "down"
    if jump == "down" and y >= 160:
        jump = "stop"
        y = 160
        number = 0
    if jump == "up":
        y = y - jump_speed
    elif jump == "down":
        y = y + jump_speed
    return(y, jump, number)

def nextLevel():
    RED= (255, 0, 0)
    lev_font = pygame.font.Font("basefont.ttf", 38)
    congrats = lev_font.render("Moving to", True, RED)
    level_surface = lev_font.render("Next Level", True, RED)
    surface = pygame.Surface((480, 320))
    surface.fill((0,0,0))
    surface.blit(congrats, (50, 50))
    surface.blit(level_surface, (50, 200))
    return (surface)

def load_pavement(pavement):
    pavement.empty()
    for x in range(0, 544, 32):
        ground = Ground()
        ground.rect.left = x
        pavement.add(ground)
    return(pavement)


pygame.init()
screen = pygame.display.set_mode((480, 320))
clock = pygame.time.Clock()
FPS = 30
BLUE = (0, 0, 255)
SMURF_BLUE = (47, 164, 245)
RED = (255, 0, 0)

background = pygame.image.load("town_pencil_blur.png")
back_rect = background.get_rect()
max_x = back_rect.right - 480
backsurf = pygame.Surface((480, 320))

x = 0

direction = "right"

smurf = Player()
innerSmurf = innerPlayer()


gameOver = False

pavement = pygame.sprite.Group()

ground_counter = 32

pavement = load_pavement(pavement)

forest = pygame.sprite.Group()
tree = Tree()
forest.add(tree)
forest_spawn_delay = 100

cactus = Obstacle()
obstacle_group = pygame.sprite.Group()
obstacle_group.add(cactus)
obstacle_spawn_delay = 20

clock_font = pygame.font.Font("animeace2_bld.ttf", 28)
lives_font = pygame.font.Font("animeace2_bld.ttf", 28)
lives = 3
lives_surf = lives_font.render("LIVES: " + str(lives), True, SMURF_BLUE)
lives_timer_start = pygame.time.get_ticks()

ouch_font = pygame.font.Font("animeace2_bld.ttf", 76)
ouch_surf = ouch_font.render("OUCH!!!", True, RED)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = "right"
            if event.key == pygame.K_LEFT:
                direction = "left"
            if smurf.jump != "up" or smurf.jump != "down":
                if event.key == pygame.K_SPACE:
                    if smurf.jump_number < 2:
                        smurf.jump = "up"
                        smurf.jump_number += 1
#                        print smurf.jump_number
    if x > max_x:
        gameOver = True
    if gameOver:
        nextScreen = nextLevel()
        screen.blit(nextScreen, (0, 0))
    elif not gameOver:
        x = scroll(x, direction)
        backsurf.blit(background, (0,0), (x, 0, 480 + x, 320))            
        screen.blit(backsurf, (0,0))
        for plant in forest:
            if plant.rect.right < 0:
                forest.remove(plant)

        if forest_spawn_delay > 0:
            forest_spawn_delay -= 1
        else:
            forest_spawn_delay = random.randrange(100, 300, 20)
            forest.add(Tree())
        forest.update()
        forest.draw(screen)


        smurf.rect.top, smurf.jump, smurf.jump_number = jump_update(smurf.rect.top, smurf.jump, smurf.jump_number)
        screen.blit(smurf.image, smurf.rect)
        if smurf.img_position < 15:
            smurf.img_position += 1
        else:
            smurf.img_position = 0

        smurf.image = pygame.image.load(smurf.img_list[smurf.img_position])
        if ground_counter > 0:
            pavement.update()
            ground_counter -= 8
        else:
            pavement = load_pavement(pavement)
            ground_counter = 32
        
        pavement.draw(screen)

        for obstacle in obstacle_group:
            if obstacle.rect.right < 0:
                obstacle_group.remove(obstacle)
        
        if obstacle_spawn_delay > 0:
            obstacle_spawn_delay -= 1
        else:
            obstacle_group.add(Obstacle())
            obstacle_spawn_delay = random.randrange(50, 140, 5)
        obstacle_group.update()
        obstacle_group.draw(screen)
        elapsed_time = int(pygame.time.get_ticks() / 1000)
        clock_surf = clock_font.render("Time: " + str(elapsed_time), True, SMURF_BLUE)
        screen.blit(clock_surf, (10, 10))
        screen.blit(lives_surf, (300, 10))


        #print(len(obstacle_group))
        innerSmurf.rect.center = smurf.rect.center
        if pygame.sprite.spritecollideany(innerSmurf, obstacle_group):
#            print("collision")
            screen.blit(ouch_surf, (30, 100))
    clock.tick(FPS)
    pygame.display.update()

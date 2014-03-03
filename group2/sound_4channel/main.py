import pygame, sys
from pygame.locals import *

pygame.init()

try:
    import android
except ImportError:
    android = None

if android:
    android.init()
    android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

try:
    import pygame.mixer as mixer
except ImportError:
    import android.mixer as mixer

LIGHT_BLUE = (51, 255, 255)
RED = (255, 0, 25)
PURPLE = (229, 100, 100)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((480, 320))

clock = pygame.time.Clock()

# load the sound files
# suggest using .wav format, especially for the first test
boom = mixer.Sound("boom.wav")
bang = mixer.Sound("rifle.wav")
crash = mixer.Sound("shake.wav")
jam = mixer.Sound("jam.wav")

# load fonts
font_a = pygame.font.Font("font_a.ttf", 40)
font_sans = pygame.font.Font("FreeSans.ttf", 28)

# make buttons
boom_surf = font_a.render("Boom!", True, BLACK, RED)
boombox = boom_surf.get_rect(left = 100, top = 50)

bang_surf = font_a.render("Bang!", True, BLACK, LIGHT_BLUE)
bangbox = bang_surf.get_rect(left = 300, top = 50)

crash_surf = font_a.render("Crash!", True, BLACK, PURPLE)
crashbox = crash_surf.get_rect(left = 100, top = 220)

jam_surf = font_a.render("Jam!", True, LIGHT_BLUE, RED)
jambox = jam_surf.get_rect(left = 300, top = 220)

# make label
label_surf = font_sans.render("4 channel Pygame Android Sound", True, (200, 200, 200))
labelbox = label_surf.get_rect(left = 10, top= 130)


while True:
    time = clock.tick(30)
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or event.type == pygame.KEYDOWN and  event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if boombox.collidepoint(pos):
                boom.play()
            if bangbox.collidepoint(pos):
                bang.play()
            if crashbox.collidepoint(pos):
                crash.play()
            if jambox.collidepoint(pos):
                jam.play()


    screen.blit(boom_surf, boombox)
    screen.blit(bang_surf, bangbox)
    screen.blit(crash_surf, crashbox)
    screen.blit(jam_surf, jambox)
    screen.blit(label_surf, labelbox)
    pygame.display.update()

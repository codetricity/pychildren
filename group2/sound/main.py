import pygame, sys

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


screen = pygame.display.set_mode((480, 320))

# load the sound file
# suggest using .wav format, especially for the first test
mixer.music.load("boom.wav")

# load fonts
font_a = pygame.font.Font("font_a.ttf", 32)
button_boom = font_a.render("Press Here for Boom", True, (200, 0,0), (0, 200, 0) )
boom_box = button_boom.get_rect(centerx = 100, centery= 120)

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or event.type == pygame.KEYDOWN and  event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mixer.music.play()

    screen.blit(button_boom, boom_box)
    pygame.display.update()

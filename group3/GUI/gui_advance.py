import pygame, sys
from pygame.locals import *

import sgc
from sgc.locals import *

pygame.init()

def next():
    print("Going to next screen")
    
class Save(sgc.Button):
    def on_click(self):
        print(self.gun_type)
        print(self.map_type)
        print(self.limit_type)
        
        ### creating file to store info
        self.file_name = open("Saved Data", "w")
        self.file_name.write("Weapon: " + self.gun_type + "\n")
        self.file_name.write("MapType: " + self.map_type + "\n")
        self.file_name.write("BulletLimit: " + str(self.limit_type) + "\n")
        self.file_name.close()
        

def radio_selected():
    map_selection = "None"
    if radio1.selected == True:
        map_selection = "Forest"
    if radio2.selected == True:
        map_selection = "Ocean"
    if radio3.selected == True:
        map_selection = "Castle"
    
    return(map_selection)

windowSurface = sgc.surface.Screen((480, 320))

clock = pygame.time.Clock()

font = pygame.font.Font("fonts/animeace2_reg.ttf", 24)
font2 = pygame.font.Font("fonts/ASTONISH.TTF", 36)
font3 = pygame.font.Font("fonts/animeace2_reg.ttf", 12)

###
btn = sgc.Button(pos = (340, 250), label = "Next", label_font = font2,
                 label_col = (255, 255, 0))
btn.on_click = next

btn2 = Save(pos = (10, 250), label = "Save", label_font = font)

### combo Box
weapons = ["pistol", "shotgun", "machinegun"]
combo = sgc.Combo(pos = (10, 10), label = "weapons",
                  values = weapons, label_side = "bottom",
                  selection = 0, label_font = font3,
                  label_col = (0, 255, 255))

btn2.gun_type = "pistol"


### Radio Box
radio1 = sgc.Radio(label = "Forest", group = "Map",
                   active = True)
radio2 = sgc.Radio(label = "Ocean", group = "Map")
radio3 = sgc.Radio(label = "Castle", group = "Map")
radio_box = sgc.VBox(pos = (10, 100), widgets = [radio1, radio2, radio3], label = "Map",
                     label_side = "top", label_font = font3,
                     label_col = (0, 255, 0))


### Switch Button
switch = sgc.Switch(pos = (250, 150), label = "limit bullets", label_side = "top",
                    label_font = font3, label_col = (255, 50, 0))


btn.add(0)
combo.add(1)
btn2.add(2)
radio_box.add(3)
switch.add(4)

while True:
    time = clock.tick(30)
    
    for event in pygame.event.get():
        sgc.event(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
            
    btn2.gun_type = (weapons[combo.selection])
    btn2.map_type = radio_selected()
    btn2.limit_type = switch.state
    
    
            
    windowSurface.fill((0, 0, 0))
    sgc.update(time)        
    pygame.display.update()

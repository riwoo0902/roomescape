import pygame
from bedroom import *
from bookcase import *
from door import *
from wardrobe import *
from workplace import *


class screenimg():

    def __init__(self,screen,password):
        self.screen = screen
        self.bedroom = Bedroom(self.screen,password)
        self.bookcase = bookcase(self.screen,password)
        self.door = door(self.screen,password)
        self.wardrobe = wardrobe(self.screen,password)
        self.workplace = workplace(self.screen,password)
        self.screenchangeimg = pygame.image.load('./image/screenchange.png').convert_alpha()
        self.screenchangeimg = pygame.transform.scale(self.screenchangeimg, (self.screen.get_width(),self.screen.get_height()))
        self.roomnumder = 1
        self.lock1 = 0
        
    def click(self):
        if pygame.mouse.get_pressed()[0]:
            if self.lock1 == 0:
                self.lock1 = 1
                pos = pygame.mouse.get_pos()
                if pos[1] > 750:
                    if pos[0] < 170:
                        if self.roomnumder != 1:
                            self.roomnumder -= 1
                    elif pos[0] > 1015:
                        if self.roomnumder != 5:
                            self.roomnumder += 1
        else:
            self.lock1 = 0
        
    def screeninput(self):
        if self.roomnumder == 1:
            self.bedroom.draw()
        elif self.roomnumder == 2:
            self.bookcase.draw()
        elif self.roomnumder == 3:
            self.door.draw()    
        elif self.roomnumder == 4:
            self.wardrobe.draw()
        elif self.roomnumder == 5:
            self.workplace.draw()
    
    
    def draw(self):
        self.click()
        self.screeninput()
        self.screen.blit(self.screenchangeimg,(0,0))
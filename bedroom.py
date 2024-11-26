import pygame
from password import *
class Bedroom():

    def __init__(self,screen,password):
        self.screen = screen
        self.bedroomimg = pygame.image.load('./image/bed.png')
        self.bedroomimg = pygame.transform.scale(self.bedroomimg, (self.screen.get_width(),self.screen.get_height()))
        self.paperimg = pygame.image.load('./image/paper.png')
        self.paperimg = pygame.transform.scale(self.paperimg,(30,24))
        self.password = password
        self.lock = 0
        
    def paperclick(self):
        pos = pygame.mouse.get_pos()
        if  self.paper.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            if self.lock == 0:
                self.lock = 1
                self.password.passwordprint(0)
        else:
            self.lock = 0
    
    def draw(self):
        self.screen.blit(self.bedroomimg,(0,0))
        self.paper = self.screen.blit(self.paperimg,(700,860))
        self.paperclick()


































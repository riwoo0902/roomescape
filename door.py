import pygame
from doorlock import *
class door():

    def __init__(self,screen,password):
        self.screen = screen
        self.password = password
        self.doorimg = pygame.image.load('./image/door.png').convert_alpha()
        self.doorimg = pygame.transform.scale(self.doorimg, (self.screen.get_width(),self.screen.get_height()))
        self.escimg = pygame.image.load('./image/esc.png').convert_alpha()
        self.escimg = pygame.transform.scale(self.escimg, (100,100))
        self.doorlock = doorlock(self.screen,self.password)
        self.lock = 0
        self.doorlockopen = False
        self.esc = self.screen.blit(self.escimg,(1000,50))

    def doorclick(self):
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.lock == 0:
                self.lock = 1
                if 300 < pos[0] < 950:
                    if 100 < pos[1] < 800:
                        self.doorlockopen = True
            if self.esc.collidepoint(pos):
                self.doorlockopen = False
        else:
            self.lock = 0

    def draw(self):
        self.screen.blit(self.doorimg,(0,0))
        self.doorclick()
        if self.doorlockopen:
            self.doorlock.draw()
        if self.doorlockopen == True:
            self.esc = self.screen.blit(self.escimg,(1000,50))
        
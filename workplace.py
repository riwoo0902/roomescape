import pygame

class workplace():

    def __init__(self,screen,password):
        self.screen = screen
        self.workplaceimg = pygame.image.load('./image/workplace.png').convert_alpha()
        self.workplaceimg = pygame.transform.scale(self.workplaceimg, (self.screen.get_width(),self.screen.get_height()))
        self.paperimg = pygame.image.load('./image/paper.png')
        self.paperimg = pygame.transform.scale(self.paperimg,(60,48))
        self.password = password
        self.lock = 0
            
    def paperclick(self):
        pos = pygame.mouse.get_pos()
        if  self.paper.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            if self.lock == 0:
                self.lock = 1
                self.password.passwordprint(3)
        else:
            self.lock = 0
    
    def draw(self):
        self.screen.blit(self.workplaceimg,(0,0))
        self.paper = self.screen.blit(self.paperimg,(930,450))
        self.paperclick()
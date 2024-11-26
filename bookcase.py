import pygame

class bookcase():

    def __init__(self,screen,password):
        self.screen = screen
        self.bookcaseimg = pygame.image.load('./image/bookcase.png').convert_alpha()
        self.bookcaseimg = pygame.transform.scale(self.bookcaseimg, (self.screen.get_width(),self.screen.get_height()))
        self.paperimg = pygame.image.load('./image/paper.png')
        self.paperimg = pygame.transform.scale(self.paperimg,(25,20))
        self.password = password
        self.lock = 0
            
    def paperclick(self):
        pos = pygame.mouse.get_pos()
        if  self.paper.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            if self.lock == 0:
                self.lock = 1
                self.password.passwordprint(1)
        else:
            self.lock = 0
    
    def draw(self):
        self.screen.blit(self.bookcaseimg,(0,0))
        self.paper = self.screen.blit(self.paperimg,(980,410))
        self.paperclick()
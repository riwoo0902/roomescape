import pygame
from password import *
class doorlock():

    def __init__(self,screen,password):
        self.screen = screen
        self.password = password
        self.Font1 = pygame.font.SysFont('malgungothic', 50)
        self.Font2 = pygame.font.SysFont(None, 100)
        self.lock = 0
        self.inputnumder = ''
        
        
    def passwardlick(self):
        pos = pygame.mouse.get_pos()
        self.doornumder = [self.door0,self.door1,self.door2,self.door3,self.door4,self.door5,self.door6,self.door7,self.door8,self.door9,self.door10]
        for i in range(11):
            if self.doornumder[i].collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                if self.lock == 0:
                    self.lock = 1
                    if i!= 10:
                        self.inputnumder += str(i)
                        self.password.passwordchick(self.inputnumder)
                    else:
                        self.inputnumder = ''
                        
        if pygame.mouse.get_pressed()[0] == False:
            self.lock = 0

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen,(127,127,127),[250,100,700,100])
        self.door0 = self.screen.blit(self.Font1.render('0',True,(255,255,255)),(575,800))
        self.door1 = self.screen.blit(self.Font1.render('1',True,(255,255,255)),(375,300))
        self.door2 = self.screen.blit(self.Font1.render('2',True,(255,255,255)),(575,300))
        self.door3 = self.screen.blit(self.Font1.render('3',True,(255,255,255)),(775,300))
        self.door4 = self.screen.blit(self.Font1.render('4',True,(255,255,255)),(375,500))
        self.door5 = self.screen.blit(self.Font1.render('5',True,(255,255,255)),(575,500))
        self.door6 = self.screen.blit(self.Font1.render('6',True,(255,255,255)),(775,500))
        self.door7 = self.screen.blit(self.Font1.render('7',True,(255,255,255)),(375,700))
        self.door8 = self.screen.blit(self.Font1.render('8',True,(255,255,255)),(575,700))
        self.door9 = self.screen.blit(self.Font1.render('9',True,(255,255,255)),(775,700))
        self.door10 = self.screen.blit(self.Font1.render('초기화',True,(255,255,255)),(900,500))
        self.passwardlick()
        self.screen.blit(self.Font2.render(self.inputnumder,True,(255,255,255)),(300,120))
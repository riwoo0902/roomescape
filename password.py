import pygame
import random

class Password():
    
    def __init__(self,screen):
        self.screen = screen
        self.paperimg = pygame.image.load('./image/paper.png')
        self.paperimg = pygame.transform.scale(self.paperimg,(600,450))
        self.password = random.randint(1000,9999)
        print(f'Password:{self.password}')
        self.password2 = list(map(int, str(self.password)))
        self.clicktime = -2000
        self.Font = pygame.font.SysFont(None, 200)
        self.escape = False
        
    def passwordprint(self,passwordnumder):
        self.clicktime = pygame.time.get_ticks()
        self.paperwrite = f'{passwordnumder+1}. {self.password2[passwordnumder]}'
        
        
    def passwordchick(self,inputnumder):
        if int(inputnumder) == self.password:
            self.escape = True
            
            
    def draw(self):
        if pygame.time.get_ticks() - self.clicktime < 1200:
            self.screen.blit(self.paperimg,(300,225))
            self.Text = self.Font.render(self.paperwrite, True, (0,0,0))
            self.screen.blit(self.Text, (490,400))
        return self.escape
        
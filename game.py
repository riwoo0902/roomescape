import pygame
from screenimg import *
from password import *
from ending import *
class Game():
    isActive = True
    screen = (1200,900)
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("codingnow.co.kr")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screen)
        self.password = Password(self.screen)
        self.screenimg = screenimg(self.screen,self.password)
        
    def eventProcess(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.isActive = False
            
    def run(self):
        while self.isActive:
            self.screen.fill((255, 255, 255))
            self.eventProcess()
            self.screenimg.draw()
            if self.password.draw():
                self.isActive = False
            pygame.display.update()
            self.clock.tick(100)

if __name__ == '__main__':
    game = Game()
    end = ending()
    game.run()
    end.draw()
    

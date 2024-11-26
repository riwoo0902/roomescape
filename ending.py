import pygame

class ending():

    def __init__(self):
        self.screen = pygame.display.set_mode((1200,900))
        self.clock = pygame.time.Clock()
        self.Font = pygame.font.SysFont('malgungothic', 100)
        self.font1 = self.Font.render('축하합니다',True,(255,255,255))
        self.font2 = self.Font.render('탈출하였습니다',True,(255,255,255))
        self.fonty = 1
        self.loop = True
        
    def eventProcess(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.loop = False
                
    def draw(self):
        while self.loop:
            self.eventProcess()
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.font1,(350,self.fonty+150))
            self.screen.blit(self.font2,(250,self.fonty))
            self.fonty += 1
            if self.fonty >= 900:
                self.loop = False
            pygame.display.update()
            self.clock.tick(100)
        

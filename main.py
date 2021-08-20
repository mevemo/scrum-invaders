import pygame
from pygame.locals import *
import time

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,500))
        # self.surface.fill((10,10,10)) 
        # pygame.display.flip()
       
    def run(self):
        running = True
        while running:            

            for event in pygame.event.get():
                # Events durch Runterdruecken:
                if event.type == KEYDOWN:
                    # ESC Taste setzt die Variable running auf False
                    if event.key == K_ESCAPE:
                        running = False
                # Durch schließen des Fensters wird running ebenfalls auf False gesetzt
                elif event.type == QUIT:
                    running = False


            time.sleep(0.2)



if __name__ == "__main__":
    game = Game()
    game.run()


    

    
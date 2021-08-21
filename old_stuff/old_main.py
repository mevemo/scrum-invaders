import pygame
from pygame.locals import * 
import time

class Game:
    def __init__(self):
        # Initialisiere PyGame
        pygame.init()

        # Definiere eine Fenstergroesse
        self.surface = pygame.display.set_mode((1200,600))

        # Gib dem Fenster eine Beschriftung
        pygame.display.set_caption("TOLLER NAME UND SO")
        

    def run(self):
        running = True
        while running:            

            for event in pygame.event.get():
                # Events durch Runterdruecken:
                if event.type == KEYDOWN:
                    # ESC Taste setzt die Variable running auf False
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_w:
                        self.surface.fill((255,255,255)) # fuellt mit einer Hintergrundfarbe (weiss)
                        pygame.display.flip()            # Uebertraegt dann die Aenderung auf das Display
                    if event.key == K_b:
                        self.surface.fill((10,10,10))    # fuellt mit einer Hintergrundfarbe (schwarz)
                        pygame.display.flip()            # refresht das Display
       
                # Durch schließen des Fensters wird running ebenfalls auf False gesetzt
                elif event.type == QUIT:
                    running = False


            time.sleep(0.2)



if __name__ == "__main__":
    game = Game()
    game.run()


    

    
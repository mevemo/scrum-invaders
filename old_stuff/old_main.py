import pygame
from pygame.locals import * 
import time

class Menue:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("platzhalter_menue.jpg").convert()
        self.x = 400
        self.y = 100

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()
class Game:
    """ In dieser Klasse befinden sich alle Aufrufe der Objekte und Methoden"""
    def __init__(self):
        # Initialisiere PyGame
        pygame.init()

        # Definiere eine Fenstergroesse
        self.surface = pygame.display.set_mode((1200,600))

        # Gib dem Fenster eine Beschriftung
        pygame.display.set_caption("TOLLER NAME UND SO")

        self.menue = Menue(self.surface)
        

    def run(self):
        running = True
        while running:            

            for event in pygame.event.get():
                # Events durch Runterdruecken:
                if event.type == KEYDOWN:
                    # ESC Taste setzt die Variable running auf False
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_m:
                        self.menue.draw()                # Ruft die draw() Funktion von Menue auf
                        pygame.display.flip()            # Uebertraegt dann die Aenderung auf das Display
                    if event.key == K_w:
                        self.surface.fill((255,255,255)) # fuellt mit einer Hintergrundfarbe (weiss)
                        pygame.display.flip()            # Uebertraegt dann die Aenderung auf das Display
                    if event.key == K_s:
                        self.surface.fill((10,10,10))    # fuellt mit einer Hintergrundfarbe (schwarz)
                        pygame.display.flip()            # refresht das Display
       
                # Und Wenn das Event "QUIT" also Fensterschließen eintritt, geht running auch auf False
                elif event.type == QUIT:
                    running = False


            time.sleep(0.2)



if __name__ == "__main__":
    game = Game()
    game.run()


    

    
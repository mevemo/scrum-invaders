import pygame
from pygame.locals import *
import time

# Hier definieren wir feste Groessen für das Gesamte Spiel
BREITE = 1280
HOEHE = 720
TITEL = "Spieltitel"
SPACESHIP_WIDTH = 50
SPACESHIP_HEIGHT = 50
START_X = 500
START_Y = 500
VEL = 5

# Spieltitel und Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

Spielername = input("Bitte Spielername eingeben: ") # Marcin Chris, Eingabe des Spielernames

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((BREITE,HOEHE))
        spieler = pygame.Rect(START_X, START_Y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) # Erzeugt ein Viereck das die Position und Groesse des SPACESHIP speichert
	
	    # Gibt dem Fenster eine Beschriftung
        # pygame.display.set_caption(TITEL)
        # self.surface.fill((10,10,10)) # Würde eine Hintergrundfarbe bestimmen
        
	    # pygame.display.flip()         # Uebertraegt dann die Aenderung auf das Display

    
       
    def run(self):
        running = True
        while running:            

            for event in pygame.event.get():
                # Events durch Runterdruecken:
                if event.type == KEYDOWN:
                    # ESC Taste setzt die Variable running auf False
                    if event.key == K_ESCAPE:
                        running = False
                        
                keys_pressed = pygame.key.get_pressed()
                
                # Events durch gedrueckthalten
                if keys_pressed[pygame.K_LEFT]: 
	                spieler.x -= VEL
                if keys_pressed[pygame.K_RIGHT]:
	                spieler.x += VEL
                    
                # Durch schließen des Fensters wird running ebenfalls auf False gesetzt
                elif event.type == QUIT:
                    running = False


            time.sleep(0.2)



if __name__ == "__main__":
    game = Game()
    game.run()


    

#hallo mike

import pygame
from pygame.locals import *
import time

pygame.mixer.init()		# Brauchen wir fuer Sound

# Hier definieren wir feste Groessen für das Gesamte Spiel
BREITE = 1280
HOEHE = 720
TITEL = "Spieltitel"
SPACESHIP_WIDTH = 50
SPACESHIP_HEIGHT = 50
START_X = 500
START_Y = 500
VEL = 10
START_MUSIC = pygame.mixer.Sound('start_music.mp3')
SPACESHIP = pygame.transform.scale(pygame.image.load('ship.png'), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
FPS = 60

# Spieltitel und Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Löst das Abspielen der Musik aus
START_MUSIC.play()
Spielername = input("Bitte Spielername eingeben: ") # Marcin Chris, Eingabe des Spielernames


"""
class Ship:
     Hier wird die ship-klasse definiert 
    def __init__(self, parent_screen):
        # Erzeugt ein Viereck das die Position und Groesse des SPACESHIP speichert
        self.spieler = pygame.Rect(START_X, START_Y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
        self.parent_screen = parent_screen
        self.image = pygame.image.load("ship.png").convert()

    def draw(self):
        self.parent_screen.blit(self.image, (self.spieler.x, self.spieler.y))
        pygame.display.flip()

"""

class Gegner:
    pass

class Game:
    def __init__(self):
        # Initialisiert Pygame:
        pygame.init()

        # Legt Breite und Höhe des Spielfensters fest
        self.surface = pygame.display.set_mode((BREITE,HOEHE))
        
        #self.ship = Ship(self.surface)

        # Erzeugt ein Viereck das die Position und Groesse des SPACESHIP speichert
        self.spieler = pygame.Rect(START_X, START_Y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) 

	    # Gibt dem Fenster eine Beschriftung
        # pygame.display.set_caption(TITEL)
        # self.surface.fill((10,10,10)) # Würde eine Hintergrundfarbe bestimmen
        
	    # pygame.display.flip()         # Uebertraegt dann die Aenderung auf das Display

       
    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:            
            clock.tick(FPS)
            for event in pygame.event.get():
                # Events durch Runterdruecken:
                if event.type == KEYDOWN:
                    # ESC Taste setzt die Variable running auf False
                    if event.key == K_ESCAPE:
                        running = False
                        
                keys_pressed = pygame.key.get_pressed()
                
                # Events durch gedrueckthalten
                if keys_pressed[pygame.K_LEFT]: 
	                self.spieler.x -= VEL
                if keys_pressed[pygame.K_RIGHT]:
	                self.spieler.x += VEL
                    
                # Durch schließen des Fensters wird running ebenfalls auf False gesetzt
                elif event.type == QUIT:
                    running = False

            # Male das alte Bild über
            self.surface.fill((10,10,10)) # Würde eine Hintergrundfarbe bestimmen

            self.ship.draw()

            # Zeichne das SPACESHIP
            self.surface.blit(SPACESHIP, (self.spieler.x, self.spieler.y))

            # RESRESH
            pygame.display.flip()

            # Mach ma Halblang
            # time.sleep(0.2)



if __name__ == "__main__":
    game = Game()
    game.run()


    

#hallo mike

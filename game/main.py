import pygame
from pygame.locals import *
import time

pygame.mixer.init()		# Brauchen wir fuer Sound

# Hier definieren wir feste Groessen für das Gesamte Spiel
BREITE = 1280
HOEHE = 720
TITEL = "Space Invaders"
SPACESHIP_WIDTH = 50
SPACESHIP_HEIGHT = 50
<<<<<<< HEAD
START_X = 500
START_Y = 500
VEL = 10
=======
GEGNER_WIDTH = 50
GEGNER_HEIGHT = 50
START_X =  (BREITE - SPACESHIP_WIDTH) / 2
START_Y =HOEHE - SPACESHIP_HEIGHT -20
BLUE = (100, 100, 100)

VEL = 5
>>>>>>> 5b64eba2822022fe080ac14efec276457fb2fdd7
START_MUSIC = pygame.mixer.Sound('start_music_StarWars.mp3')
SPACESHIP = pygame.transform.scale(pygame.image.load('ship.png'), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
FPS = 60

# Spieltitel und Icon
pygame.display.set_caption(TITEL)
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Löst das Abspielen der Musik aus
#START_MUSIC.play()

# Eingabe des Spielernamens
Spielername = input("Bitte Spielername eingeben: ") # Marcin Chris, Eingabe des Spielernames


# Ab hier von MAIK
class Ship:
    """ Hier wird die ship-klasse definiert """
    def __init__(self, parent_screen):
	    # """ Diese Methode wird immer dann ausgeführt, wenn ein neues Ship erschaffen wird"""
        # Erzeugt ein Viereck das die Position und Groesse des SPACESHIP speichert
        self.spieler = pygame.Rect(START_X, START_Y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
	
	    # Ordnet den mitangegebenen parent_screen einer eigenen variablen zu
        self.parent_screen = parent_screen
	
	    # Weist dem Ship eine Variable image zu
        self.image = SPACESHIP
	
	    # Setzt die Schrittweite (Die Bewegung des Schiffs) am Anfang auf Null
        self.step = 0

    def draw(self):
	    # """ Mit dieser Methode kann ein Schiff sich auf dem zugeordneten Bildschirm zeichnen"""
        # Das Bild wird dem Screen hinzugefügt
	    self.parent_screen.blit(self.image, (self.spieler.x, self.spieler.y))
        # pygame.display.flip()


    def walk(self):
        """ Hier ist festgelegt wie sich das Ship bewegen darf """
        if self.spieler.x + self.step > BREITE:
            self.spieler.x = 0
        elif self.spieler.x + self.step < 0:
            self.spieler.x = BREITE - SPACESHIP_WIDTH
        else:
            self.spieler.x += self.step

        self.draw()
# bis hier von MAIK


class Gegner:
    def __init__(self, parent_screen):
        # self.list = [ [1, 5, 300], [1, 5, 500] , [1, 5, 700], [1, 5, 900] ]
        self.list= []
        for i in range(50):
            if i < 12:
                self.list.append([1, pygame.Rect(50 + (i * 100), 5, GEGNER_WIDTH, GEGNER_HEIGHT)])
            elif i < 24:
                self.list.append([1, pygame.Rect(50 + ((i-12) * 100), 105, GEGNER_WIDTH, GEGNER_HEIGHT)])
            elif i < 36:
                self.list.append([1, pygame.Rect(50 + ((i-24) * 100), 205, GEGNER_WIDTH, GEGNER_HEIGHT)])
        
        self.step = 1
        self.parent_screen = parent_screen
        self.image = SPACESHIP
        self.count = 0
    
    def walk(self):
        
        if self.count //10 % 2 == 0:
            for ding in self.list:
                ding[1].x += self.step
                ding[1].y += self.step

        else:
            for ding in self.list:
                ding[1].x -= self.step
                ding[1].y += self.step

        
            self.count += 1
        
        self.draw()
    
    def draw(self):
        for ding in self.list:
            # self.parent_screen.blit(self.image, (ding[1], ding[2]))
            pygame.draw.rect(self.parent_screen,BLUE,(ding[1].x, ding[1].y, GEGNER_WIDTH, GEGNER_HEIGHT,))



class Game:
    def __init__(self):
        # Initialisiert Pygame:
        pygame.init()

        # Legt Breite und Höhe des Spielfensters fest
        self.surface = pygame.display.set_mode((BREITE,HOEHE))
        
        self.ship = Ship(self.surface)
        self.gegner = Gegner(self.surface)

        # WEGEN NEU NOT NEEDED
        # Erzeugt ein Viereck das die Position und Groesse des SPACESHIP speichert
        # self.spieler = pygame.Rect(START_X, START_Y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) 

	    
        # self.surface.fill((10,10,10)) # Würde eine Hintergrundfarbe bestimmen
        
	    # pygame.display.flip()         # Uebertraegt dann die Aenderung auf das Display

    #Bullets Variablen
    BULLET = pygame.image.load("bullet1.png")
    BULLET_X = 0
    BULLET_Y = 50
    
    #Bullets Klasse 
    class Bullet():
        
            
    
    
       
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
                    # Linker Pfeil verursacht Bewegung nach links
                    if event.key == K_LEFT:
                        self.ship.step = -VEL
                    # Rechter Pfeil verursacht Bewegung nach links
                    if event.key == K_RIGHT:
                        self.ship.step = VEL    
                    # Bullets schiessen
                    if event.key == K_SPACE:
                        bullet = pygame.Rect(SPACESHIP_HEIGHT, SPACESHIP_WIDTH)
                        bullet.append('bullet1.png')
                       
                        
<<<<<<< HEAD
   
                # keys_pressed = pygame.key.get_pressed()

                # NEU NOT NEEDED
                
                # Events durch gedrueckthalten
                # if keys_pressed[pygame.K_LEFT]: 
	            #     self.spieler.x -= VEL
                # if keys_pressed[pygame.K_RIGHT]:
	            #     self.spieler.x += VEL
                
=======
                if event.type == KEYUP:
                    if event.key == K_LEFT:
                        self.ship.step = 0
                    if event.key == K_RIGHT:
                        self.ship.step = 0


>>>>>>> 5b64eba2822022fe080ac14efec276457fb2fdd7
                    
                # Durch schließen des Fensters wird running ebenfalls auf False gesetzt
                elif event.type == QUIT:
                    running = False

            # Male das alte Bild über
            self.surface.fill((10,10,10)) # Würde eine Hintergrundfarbe bestimmen

            self.ship.walk() # von MAIK

            self.gegner.walk() # von Maik

            # dann kommt später:
            # self.gegner.walk()

            # RESRESH
            pygame.display.flip()

            # Mach ma Halblang wurde durch FPW ersetzt
            # time.sleep(0.2)



if __name__ == "__main__":
    game = Game()
    game.run()




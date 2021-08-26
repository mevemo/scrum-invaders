import pygame
from pygame.locals import *
import time
import random

pygame.mixer.init()		# Brauchen wir fuer Sound

# Hier definieren wir feste Groessen für das Gesamte Spiel
BREITE = 1280
HOEHE = 720
TITEL = "Space Invaders"
SPACESHIP_WIDTH = 50
SPACESHIP_HEIGHT = 50
GEGNER_WIDTH = 50
GEGNER_HEIGHT = 50
START_X =  (BREITE - SPACESHIP_WIDTH) / 2
START_Y =HOEHE - SPACESHIP_HEIGHT -20
BLUE = (100, 100, 100)
bg = pygame.image.load('bg.png')
BULLET_VEL = 10
VEL = 5
START_MUSIC = pygame.mixer.Sound('start_music_StarWars.mp3')
SPACESHIP = pygame.transform.scale(pygame.image.load('ship.png'), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
BULLET = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('bullet1.png'), (20,20)), 45)
FPS = 60
bullets = []
# gegner_speed = 1

# Spieltitel und Icon
pygame.display.set_caption(TITEL)
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Löst das Abspielen der Musik aus
#START_MUSIC.play()

# Eingabe des Spielernamens
Spielername = input("Bitte Spielername eingeben: ") # Marcin Chris, Eingabe des Spielernames

def draw_bg(parent_screen):
    parent_screen.blit(bg, (0, 0))

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

        self.hp = 3

    def draw(self):
	    # """ Mit dieser Methode kann ein Schiff sich auf dem zugeordneten Bildschirm zeichnen"""
        # Das Bild wird dem Screen hinzugefügt
	    self.parent_screen.blit(self.image, (self.spieler.x, self.spieler.y))
        # pygame.display.flip()


    def walk(self):
        """ Hier ist festgelegt wie sich das Ship bewegen darf """
        if self.spieler.x + self.step > BREITE - 50:
            self.spieler.x = 0
        elif self.spieler.x + self.step < 0:
            self.spieler.x = BREITE - SPACESHIP_WIDTH
        else:
            self.spieler.x += self.step

        self.draw()


class Gegner:
    def __init__(self, parent_screen, speed):
       
        for i in range(50):
            if i < 12:
                self.list.append([1, pygame.Rect(50 + (i * 100), 5, GEGNER_WIDTH, GEGNER_HEIGHT)])
            elif i < 24:
                self.list.append([1, pygame.Rect(50 + ((i-12) * 100), 105, GEGNER_WIDTH, GEGNER_HEIGHT)])
            elif i < 36:
                self.list.append([1, pygame.Rect(50 + ((i-24) * 100), 205, GEGNER_WIDTH, GEGNER_HEIGHT)])
		
        self.image = pygame.image.load('gegner' + str(random.randint(0, 5)) + '.png')
        self.step = speed
        self.parent_screen = parent_screen
        self.count = 0
    
    def walk(self):
        
        # aaaaaalso:  Wenn es noch nicht am rechten Rand ist und y weniger als 55 pixel gelaufen ist (also rest nach y/100), wandert es x plus einen step also nach rechts
        # da es % 100 gerechnet wird zählt es jeweils für bis 55, bis 155, bis 255, ect
        if self.list[11][1].x < BREITE - 50 and self.list[11][1].y % 100 < 55:
            for ding in self.list:
                ding[1].x += self.step

        # wenn es dann noch nicht 55 pixel weit runter gegangen ist geht es immer y plus einen step nach unten
        # da es % 100 gerechnet wird zählt es für bis 55, bis 155, bis 255, ect
        elif self.list[11][1].y % 100 < 55:
            for ding in self.list:
                ding[1].y += self.step

        # wenn es dann noch nicht am linken rand ist, wandert es dann immer x minus einen step, also nach links
        elif self.list[0][1].x > 0:
            for ding in self.list:
                ding[1].x -= self.step

        # sonst wandert es nach unten
        else:
            for ding in self.list:
                ding[1].y += self.step
        # ab y = 101 ist wieder die oberste bedingung erfüllt und es geht von forne los
        
        self.count += 1
        
        self.draw()
    
    def draw(self):
        for ding in self.list:
            # self.parent_screen.blit(self.image, (ding[1], ding[2]))
            if ding[0] != 0:
                pygame.draw.rect(self.parent_screen,BLUE,(ding[1].x, ding[1].y, GEGNER_WIDTH, GEGNER_HEIGHT,))



class Game:
    def __init__(self):
        # Initialisiert Pygame:
        pygame.init()

        # Legt Breite und Höhe des Spielfensters fest
        self.surface = pygame.display.set_mode((BREITE,HOEHE))
        
        self.gegner_speed = 1

        self.ship = Ship(self.surface)
        self.gegner = Gegner(self.surface, self.gegner_speed)
       

        # WEGEN NEU NOT NEEDED
        # Erzeugt ein Viereck das die Position und Groesse des SPACESHIP speichert
        # self.spieler = pygame.Rect(START_X, START_Y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) 

	    
        # self.surface.fill((10,10,10)) # Würde eine Hintergrundfarbe bestimmen
        
	    # pygame.display.flip()         # Uebertraegt dann die Aenderung auf das Display

    # def handle_bullets(self):
    #     for bullet in self.bullets:
    #         bullet.x += BULLET_VEL
    #         if red.colliderect(bullet):
    #             pygame.event.post(pygame.event.Event(RED_HIT))
    #             yellow_bullets.remove(bullet)
    #         elif bullet.x > WIDTH:
    #             yellow_bullets.remove(bullet)

    
           
    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running: 
            clock.tick(FPS)
            draw_bg(self.surface)
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
                    # Leertaste schiesst Kugeln
                    if event.key == K_SPACE:
                        bulletSound = pygame.mixer.Sound("laser.wav")
                        bulletSound.play()
                        bullet = pygame.Rect(self.ship.spieler.x +12 , self.ship.spieler.y, 10, 10)
                        bullets.append(bullet)
                        
                if event.type == KEYUP:
                    if event.key == K_LEFT:
                        self.ship.step = 0
                    if event.key == K_RIGHT:
                        self.ship.step = 0
                

                    
                # Durch schließen des Fensters wird running ebenfalls auf False gesetzt
                elif event.type == QUIT:
                    running = False

            # Schiffbewegung wird ausgelöst
            self.ship.walk() 

            # Gegnerbewegung wird ausgelöst
            self.gegner.walk()

            for bullet in bullets:
                # pygame.draw.rect(self.surface, BLUE, bullet)
                if bullet.y - BULLET_VEL > 0:
                    bullet.y -= BULLET_VEL  
                else: 
                    bullets.remove(bullet)
                
                for jener_gegner in self.gegner.list:
                    if jener_gegner[1].colliderect(bullet) and jener_gegner[0] > 0:
                        explosionSound = pygame.mixer.Sound("explosion.wav")
                        explosionSound.play()
                        # pygame.event.post(pygame.event.Event(RED_HIT))
                        bullets.remove(bullet)
                        jener_gegner[0] = 0
                self.surface.blit(BULLET, (bullet.x, bullet.y))
            #alles neu macht der mai
            alive = False

            # Hier checken wir ob ein gegner das schiff trifft und machen dann was damit:
            for jener_gegner in self.gegner.list:
                
                if jener_gegner[1].colliderect(self.ship.spieler) and jener_gegner[0] > 0:

                    jener_gegner[0] -= 1
                   
                    if self.ship.hp == 1:
                        running = False    
                    else:
                        self.ship.hp = 1   
                
                if jener_gegner[1].y > HOEHE - GEGNER_HEIGHT:
                    running = False

                if jener_gegner[0] > 0:
                    alive = True
                
            if alive == False:
                self.gegner_speed += 2
                game.gegner = Gegner(self.surface, self.gegner_speed)




                
            # dann kommt später:
            # self.gegner.walk()

            # RESRESH
            pygame.display.flip()

            # Mach ma Halblang wurde durch FPW ersetzt
            # time.sleep(0.2)



if __name__ == "__main__":
    game = Game()
    game.run()




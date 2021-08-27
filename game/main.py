import pygame
from pygame.locals import *
import time
import random
import sys
import turtle
from turtle import textinput

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
COLORS = [(255,0,0), (255,165,0), (0,255,0) ]
bg = pygame.image.load('bg.png')
BULLET_VEL = 10
VEL = 5
AMMO = 30
         # ↓ Wird für Startmenu gebraucht ↓
DISPLAY = pygame.display.set_mode((BREITE, HOEHE))
START_MUSIC = pygame.mixer.Sound('start_music_StarWars.mp3')
SPACESHIP = pygame.transform.scale(pygame.image.load('ship.png'), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
BONUSSHIP = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('bonus_space-ship.png'), (65, 65)), 22.5)
BULLET = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('bullet1.png'), (20,20)), 45)
#game_over = pygame.image.load('gameover.png')
game_over = pygame.transform.scale(pygame.image.load('gameover.png'), (BREITE, HOEHE))
FPS = 60
bullets = []
gegner_bullets = []
# gegner_speed = 1

# Spieltitel und Icon
pygame.display.set_caption(TITEL)
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Eingabe des Spielernamens
Spielername = textinput("Name", "Bitte Spielername eingeben: ") # Marcin Chris, Eingabe des Spielernames (Modifiziert)
# Score

# score_value = 0
# font = pygame.font.Font('freesansbold.ttf', 32)

# textX = 10
# testY = 10



# def show_score(x, y):
#     score = pygame.font.render("Score : " + str(score_value), True, (255, 255, 255))
#     screen.blit(score, (x, y))
	
	# ↓ Damit können wir etwas schreiben ↓
def draw_text(surface, text, size, x, y, color):
    font = pygame.font.Font(pygame.font.match_font('impact'), size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)
	
# ↓ DIMI START MENU ↓
def menu():
    turtle.bye()
    title = pygame.image.load('startmenutitel.png').convert_alpha()
    title = pygame.transform.scale(title, (BREITE, 81 * 2))


    arrow_keys = pygame.image.load('move.png').convert_alpha()
    arrow_keys = pygame.transform.scale(arrow_keys, (150, 85))
    spacebar = pygame.image.load('shoot.png').convert_alpha()
    spacebar = pygame.transform.scale(spacebar, (150, 50))
 
    DISPLAY.blit(title, (0,20))
    DISPLAY.blit(arrow_keys, ((BREITE/2) - 80, 490))
    DISPLAY.blit(spacebar, ((BREITE/2) - 80, 610))
    draw_text(DISPLAY, "WILLKOMMEN " + Spielername, 50, BREITE/2, (HOEHE/2) - 140, (30,144,255))
    draw_text(DISPLAY, "DRUCK ENTER", 90, BREITE/2, (HOEHE/2) - 50, (30,144,255))
    draw_text(DISPLAY, "Q TO QUIT", 40, BREITE/2, (HOEHE/2) + 305, (30,144,255))

    draw_text(DISPLAY, "MOVE:", 35, BREITE/2, 495, (30,144,255))
    draw_text(DISPLAY, "SHOOT:", 35, BREITE/2, 575, (30,144,255))
 
    pygame.display.update()
 
    while True:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                break
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        elif event.type == QUIT:
            pygame.quit()
            sys.exit() 
 # ↑ DIMI START MENU ↑	



# Löst das Abspielen der Musik aus
#START_MUSIC.play()



def draw_bg(parent_screen):
    parent_screen.blit(bg, (0, 0))

class Ship:
    """ Hier wird die ship-klasse definiert """
    def __init__(self, parent_screen, ammo):
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

        self.ammo = ammo

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

#Bonus Schiff
class Bonus_Ship:
    def __init__(self, parent_screen):
        self.step = 2
        self.hp = 0
        self.surface = parent_screen
        self.list = [0, pygame.Rect(0, 0, 65, 65)]
    
    def walk(self):
        if self.list[1].x + 35 + self.step > BREITE:
            self.list[1].x = 0
        else:
            self.list[1].x += self.step        
        self.draw()
        
    def draw(self):
        self.surface.blit(BONUSSHIP, (self.list[1].x, self.list[1].y))

class Gegner:
    def __init__(self, parent_screen, speed):
        self.list = []
        for i in range(50):
            if i < 12:
                self.list.append([1, pygame.Rect(50 + (i * 100), 5, GEGNER_WIDTH, GEGNER_HEIGHT), (pygame.image.load('gegner' + str(random.randint(0, 5)) + '.png'))])
            # elif i < 24:
            #     self.list.append([1, pygame.Rect(50 + ((i-12) * 100), 105, GEGNER_WIDTH, GEGNER_HEIGHT), (pygame.image.load('gegner' + str(random.randint(0, 5)) + '.png'))])
            # elif i < 36:
            #     self.list.append([1, pygame.Rect(50 + ((i-24) * 100), 205, GEGNER_WIDTH, GEGNER_HEIGHT), (pygame.image.load('gegner' + str(random.randint(0, 5)) + '.png'))])
		
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
        # ab y = 101 ist wieder die oberste bedingung erfüllt und es geht von vorne los
        
        self.count += 1

        if self.count % 40 == 0:
            bulletSound = pygame.mixer.Sound("laser.wav")
            bulletSound.play()
            # Wüfelt so lange bis ein ballermann rauskommt der am leben ist
            while True:
                ballermann = random.randint(1, len(self.list)-1)
                if self.list[ballermann][0] > 0:
                    break


            bullet = pygame.Rect(self.list[ballermann][1].x + 25 , self.list[ballermann][1].y +50, 10, 10)
            gegner_bullets.append(bullet)
        # self.kurz_image = pygame.image.load('gegner' + str(random.randint(0, 5)) + '.png')

        # if self.count % 2 == 0:
        #     self.kurz_image = pygame.image.load('gegner' + str(random.randint(0, 5)) + '.png')

        self.draw()
    
    def draw(self):
        for ding in self.list:
            # self.parent_screen.blit(self.image, (ding[1], ding[2]))
            if ding[0] != 0:
                # pygame.draw.rect(self.parent_screen,BLUE,(ding[1].x, ding[1].y, GEGNER_WIDTH, GEGNER_HEIGHT,))
                
                self.parent_screen.blit(ding[2], (ding[1].x, ding[1].y))

class Deckung:
    def __init__(self, parent_screen):
        self.list = []
        self.list.append([3, pygame.Rect(128, 500, 256, 100)])
        self.list.append([3, pygame.Rect(512, 500, 256, 100)])
        self.list.append([3, pygame.Rect(914, 500, 256, 100)])
        self.parent_screen = parent_screen

    def draw(self):
        for ding in self.list:
            if ding[0] == 1:
                pygame.draw.rect(self.parent_screen,COLORS[0],(ding[1].x, ding[1].y, 256, 100))
            elif ding[0] == 2:
                pygame.draw.rect(self.parent_screen,COLORS[1],(ding[1].x, ding[1].y, 256, 100))
            elif ding[0] == 3:
                pygame.draw.rect(self.parent_screen,COLORS[2],(ding[1].x, ding[1].y, 256, 100))


class Game:
    def __init__(self):
        # Initialisiert Pygame:
        pygame.init()
        
        # Legt Breite und Höhe des Spielfensters fest
        self.surface = pygame.display.set_mode((BREITE,HOEHE))
        
        # Erschafft ein Bonus Shuip mit 0 HP im Hintergrund für später
        self.bonus = Bonus_Ship(self.surface)
        
        self.gegner_speed = 1

        self.ship = Ship(self.surface, AMMO)
        self.gegner = Gegner(self.surface, self.gegner_speed)
        self.deckung = Deckung(self.surface)
       
        self.score_value = 0
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
        show_menu = True

        while running: 
            clock.tick(FPS)
            draw_bg(self.surface)
	# ↓ DIMI MENU While run Loop ↓ 
            if show_menu:
               menu()
               pygame.time.delay(1500)
               show_menu = False		 
        # ↑ DIMI MENU While run Loop ↑
				 
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
                    if event.key == K_SPACE and len(bullets) <= self.ship.ammo:
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

            # Deckung malen:
            self.deckung.draw()
            
            # Bonus Schiff kommt in's Spiel 
            if self.score_value % 9 == 0 and self.score_value != 0:
                self.bonus.hp = 1

            # Bonus Schiff Malen
            if self.bonus.hp > 0:

                self.bonus.walk()


            # Hier handeln wir die fliegenden Bullets vom random-gegner ballermann
            for bullet in gegner_bullets:
            
                # Prüfung ob sie in die Deckung knallt
                for element in self.deckung.list:
                    if element[1].colliderect(bullet) and element[0] > 0:
                        explosionSound = pygame.mixer.Sound("explosion.wav")
                        explosionSound.play()
                        gegner_bullets.remove(bullet)
                        element[0] -= 1

                # Wenn die gegner_bullet das schiff trifft
                if self.ship.spieler.colliderect(bullet):
                        explosionSound = pygame.mixer.Sound("explosion.wav")
                        explosionSound.play()
                        self.ship.hp -= 1
                        gegner_bullets.remove(bullet)

                # Wenn sie noch inm Spielfeld bleibt, fliegt sie weiter
                if bullet.y + BULLET_VEL < HOEHE:
                    bullet.y += BULLET_VEL  
                elif bullet.y + BULLET_VEL >= HOEHE: 
                    gegner_bullets.remove(bullet)

                # Zeichne die Kugel
                self.surface.blit(BULLET, (bullet.x, bullet.y))

            # Hier handeln wir die fliegenden Bullets vom SPACESHIP
            for bullet in bullets:
                # Bewege die Bullet 
                if bullet.y - BULLET_VEL > 0:
                    bullet.y -= BULLET_VEL  
                else: 
                    bullets.remove(bullet)
                
                # Prüft ob die Bullet des Schiffs einen Gegner trifft
                for jener_gegner in self.gegner.list:
                    if jener_gegner[1].colliderect(bullet) and jener_gegner[0] > 0:
                        explosionSound = pygame.mixer.Sound("explosion.wav")
                        explosionSound.play()
                        self.score_value += 1
                        # pygame.event.post(pygame.event.Event(RED_HIT))
                        bullets.remove(bullet)
                        jener_gegner[0] = 0

                # Prüft ob eine Bullet des Schiffs die eigene Deckung trifft
                for element in self.deckung.list:
                    if element[1].colliderect(bullet) and element[0] > 0:
                        explosionSound = pygame.mixer.Sound("explosion.wav")
                        explosionSound.play()
                        bullets.remove(bullet)
                        element[0] -= 1

                #Prüfe ob eine Bullet das Bonusship trifft
                if self.bonus.list[1].colliderect(bullet) and self.bonus.hp > 0:
                    self.ship.hp += 1
                    self.bonus.hp = 0


                # Zeichne die Bullet
                self.surface.blit(BULLET, (bullet.x, bullet.y))
            
            # Einführen einer gegner_alive Variable um später zu checken ob alle Gegner tot sind
            gegner_alive = False


            # Hier checken wir ob ein gegner das Schiff trifft und machen dann was damit:
            for jener_gegner in self.gegner.list:
                
                if jener_gegner[1].colliderect(self.ship.spieler) and jener_gegner[0] > 0:
                    # print (self.ship.hp)
                    bulletSound = pygame.mixer.Sound("explosion.wav")
                    bulletSound.play()
                    self.ship.hp = 0
                    # print(f"Die Restlichen HP sind: {self.ship.hp}")  


                for element in self.deckung.list:
                    if jener_gegner[1].colliderect(element[1]) and jener_gegner[0] > 0 and element[0] > 0:
                        element[0] -= 1
                        jener_gegner[0] -= 1
                        bulletSound = pygame.mixer.Sound("explosion.wav")
                        bulletSound.play()

                if jener_gegner[1].y > HOEHE - GEGNER_HEIGHT and jener_gegner[0] > 0:
                    self.surface.blit(game_over, (0, 0))

                if jener_gegner[0] > 0:
                    gegner_alive = True

            # Abfrage ob alle gegner im aktuellen Level tot sind   
            if gegner_alive == False:
                # Hier wird der Gegner mit schneller
                self.gegner_speed += 1
                # Hier wird die AMMO größer
                self.ship.ammo += 3
                self.deckung = Deckung(self.surface)
                game.gegner = Gegner(self.surface, self.gegner_speed)

            if self.ship.hp <= 0:
                
                self.surface.blit(game_over, (0, 0))

            
                
            # dann kommt später:
            # self.gegner.walk()
            # show_score(textX, testY)
            # RESRESH
            pygame.display.flip()

            # Mach ma Halblang wurde durch FPS ersetzt
            # time.sleep(0.2)



if __name__ == "__main__":
    game = Game()
    game.run()




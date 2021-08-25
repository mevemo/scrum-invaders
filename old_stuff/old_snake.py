import pygame
from pygame.locals import *
import time
"""
SIZE = 30

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("fruit.jpg").convert()
        self.x = SIZE * 10
        self.y = SIZE * 10

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("snake_head.jpg").convert()
        self.x = [SIZE] * length      # Position x
        self.y = [SIZE] * length      # Position y
        self.step = 30    # größe eines Schrittes
        self.direction = 'right'

    def draw(self):
        self.parent_screen.fill((10,10,10))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()
        
    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'left':
            self.x[0] -= self.step

        if self.direction == 'right':
            self.x[0] += self.step
        
        if self.direction == 'up':
            self.y[0] -= self.step

        if self.direction == 'down':
            self.y[0] += self.step

        self.draw()
"""

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,500))
        self.surface.fill((10,10,10)) 
        # self.snake = Snake(self.surface, 1)
        # self.snake.draw()
        # self.apple = Apple(self.surface)
        # self.apple.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    elif event.key == K_UP:
                        self.snake.move_up()
                    elif event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                
                if event.type == KEYUP:
                    


                elif event.type == QUIT:
                    running = False

            self.snake.walk()
            self.apple.draw()
            time.sleep(0.2)



if __name__ == "__main__":
    game = Game()
    game.run()


    

    
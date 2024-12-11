import pygame
WINDOW_WIDTH = 1024

class Duck():
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load("sprites/duck.png")
        self.rect  = self.image.get_rect(topleft=(self.x, self.y))

    def move(self): 
        self.x += self.speed
        if self.x > WINDOW_WIDTH or self.x < 0:
            self.speed = -self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.rect)

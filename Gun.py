import pygame

class Gun():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = -10
        self.rect = pygame.Rect(self.x, self.y, 5, 10)

    def move(self):
        self.y += self.speed

    def draw(self, SCREEN):
        pygame.draw.rect(SCREEN, 'BLACK', self.rect)
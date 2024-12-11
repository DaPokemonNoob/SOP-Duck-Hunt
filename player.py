import pygame

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768

class Player():
    def __init__(self):
        self.crosshair = pygame.image.load('sprites/crosshair.png')
        self.rect = self.crosshair.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.score = 0

    def move(self):
        self.rect.center = mouse_pos

    def draw(self):
        SCREEN.blit(self.crosshair, self.rect)
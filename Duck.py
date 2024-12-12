import pygame

WINDOW_WIDTH = 1024

class Duck():
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load("sprites/duck.png")  # Original sprite
        self.flipped_image = pygame.transform.flip(self.image, True, False)  # Flippet version
        self.current_image = self.image  # Den nuværende sprite, der vises
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        if self.speed < 0:
            self.current_image = self.flipped_image

    def move(self):
        self.x += self.speed

        # Tjek for kant og skift retning
        if self.x + self.rect.width > WINDOW_WIDTH:
            self.speed = -self.speed
            self.current_image = self.flipped_image  # Skift til flippet sprite
        if self.x < 0:
            self.speed = -self.speed
            self.current_image = self.image  # Skift tilbage til original sprite

        self.rect.topleft = (self.x, self.y)

    def draw(self, SCREEN):
        SCREEN.blit(self.current_image, self.rect)  # Tegn den aktuelle sprite
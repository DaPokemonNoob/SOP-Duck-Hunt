import pygame, sys
import random
from pygame import mixer
from duck import Duck
from gun import Gun
from player import Player

class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

pygame.init()

FPS = 30
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
running = True

BG = pygame.image.load("sprites/background.png")

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Duck Hunt")

ducks = [Duck(random.randint(0, WINDOW_WIDTH - 150), random.randint(50, 300), random.choice([-8, 8])) for _ in range(5)]
player = Player()
bullets = []

def main_menu():
    global running
    while running:
        SCREEN.blit(BG,(0,0))

        mouse_pos = pygame.mouse.get_pos()
        player.move(mouse_pos)
        
        for duck in ducks:
            duck.move()
            duck.draw(SCREEN)

        for bullet in bullets:
            bullet.move()
            bullet.draw(SCREEN)

        for bullet in bullets:
            for duck in ducks:
                if duck.rect.colliderect(bullet.rect):
                    duck.remove(duck)
                    bullets.remove(bullet)
                    player.score += 10
                    break

        player.draw(SCREEN)

        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bullets.append(Gun(player.rect.centerx, player.rect.centery))

        

SCREEN.fill("White")
main_menu()
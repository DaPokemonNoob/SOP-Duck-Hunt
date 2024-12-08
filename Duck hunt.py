import pygame, sys
from pygame import mixer

class color:
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

BG = pygame.image.load("sprites/background.png")

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Duck Hunt")

def main_menu():
    while True:
        SCREEN.blit(BG,(0,0))
        pygame.display.flip()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
SCREEN.fill("White")
main_menu()
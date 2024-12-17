import pygame
import random
from duck import Duck
from player import Player
import serial

pygame.init()

arduino = serial.Serial('COM6', 9600, timeout=1)

FPS = 30
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 718
running = True
mapped_x = 0
mapped_y = 0

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
BG = pygame.image.load("sprites/background.png")
pygame.display.set_caption("Duck Hunt")

ducks = [Duck(random.randint(0, WINDOW_WIDTH - 150), random.randint(25, 250), random.choice([-8, 8])) for _ in range(5)]
player = Player()
hit_ducks = {}
def respawn_ducks():
    global ducks
    ducks = [Duck(random.randint(0, WINDOW_WIDTH - 150), random.randint(25, 250), random.choice([-8, 8])) for _ in range(5)]

# Flash variables
flash_active = False
flash_start_time = 0
FLASH_DURATION = 0.05  # Flash duration in seconds

def main_menu():
    global running, flash_active, flash_start_time, mapped_x, mapped_y
    while running:
        if flash_active:
            # Flash the screen white
            SCREEN.fill('WHITE')
            # Check if flash duration has passed
            if pygame.time.get_ticks() - flash_start_time > FLASH_DURATION * 1000:
                flash_active = False
        else:
            # Draw the background
            SCREEN.blit(BG, (0, 0))
            '''
            SCORE_TEXT = pygame.font.Font("sprites/font.ttf").render(player.score, True, "#FFFFFF")
            SCORE_RECT = SCORE_RECT.get_rect(center=(800, 500))
            '''
            # Move and draw ducks
            for duck in ducks:
                duck.move()
                duck.draw(SCREEN)

            # Draw the player (crosshair)
            pygame.mouse.set_pos(mapped_x, mapped_y)
            mouse_pos = pygame.mouse.get_pos()
            player.move(mouse_pos)
            player.draw(SCREEN)

        # remove the ducks that are hit by the crosshair
        current_time = pygame.time.get_ticks()
    
        for duck, hit_time in list(hit_ducks.items()):
            if current_time - hit_time > FLASH_DURATION * 1000:
                ducks.remove(duck)
                del hit_ducks[duck]

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    respawn_ducks()
                    
        if arduino.in_waiting > 0:
            line = arduino.readline().decode('utf-8').strip()
            if line == 'SHOT':
                flash_active = True
                flash_start_time = pygame.time.get_ticks()
                for duck in ducks:
                    if player.rect.colliderect(duck.rect) and duck not in hit_ducks:
                        hit_ducks[duck] = pygame.time.get_ticks()
                        player.score += 500

            if "accelerations are" in line:
                coords = line.split(":")[-1].strip().split()

                x, y, z= map(int, coords)
                mapped_x = (x-400)/220 * 980
                mapped_y = (y-390)/220 * 640

# Start the game
main_menu()
pygame.quit()
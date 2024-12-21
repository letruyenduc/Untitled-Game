import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
player = pygame.Rect(50, 50, 50, 50)
clock = pygame.time.Clock()


# Les couleurs
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player)  # Dessine le joueur en tant que rectangle rouge
    pygame.display.flip()  # Rafraîchit l'écran

    clock.tick(60)  # Limite le jeu à 60 images par seconde

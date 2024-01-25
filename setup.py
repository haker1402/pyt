import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Définition des constantes
WIDTH, HEIGHT = 800, 600
FPS = 60

# Couleurs
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Création de la fenêtre du jeu
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")

# Création du joueur
player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 50, 50, 50)

# Création de l'ennemi
enemy = pygame.Rect(random.randint(0, WIDTH - 50), 0, 50, 50)
enemy_speed = 5

# Clock pour définir le FPS
clock = pygame.time.Clock()

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mouvement du joueur
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.x < WIDTH - 50:
        player.x += 5

    # Mouvement de l'ennemi
    enemy.y += enemy_speed
    if enemy.y > HEIGHT:
        enemy.y = 0
        enemy.x = random.randint(0, WIDTH - 50)

    # Collision entre joueur et ennemi
    if player.colliderect(enemy):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # Effacer l'écran
    screen.fill(WHITE)

    # Dessiner le joueur et l'ennemi
    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, WHITE, enemy)

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Limiter le nombre d'images par seconde
    clock.tick(FPS)

import pygame
import sys
import time

print("Startuję main.py...")

pygame.init()
print("pygame.init OK")

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Leonardo's Workshop - Prototype")

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 40))

    pygame.display.flip()
    clock.tick(2)  # 2 FPS, żeby spam w konsoli nie był dziki
    print("tick")

pygame.quit()
print("pygame.quit()")
sys.exit()
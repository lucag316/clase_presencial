import pygame
import sys
import random

from config import *
from nave import Nave
from asteroide import Asteroide


def generar_asteroides(grupo_asteroides, grupo_sprites, cantidad):
    if len(grupo_asteroides) == 0:
        for i in range(cantidad):
            posicion = (random.randrange(20, WIDTH - 20),
                        random.randrange(-500, HEIGHT // 2))
            asteroide = Asteroide("./images/asteroide.png", SIZE_ASTERIOD, posicion, SPEED_ASTEROIDE)
            grupo_asteroides.add(asteroide)
            grupo_sprites.add(asteroide)

sprites.add(nave)

while True:

    generar_asteroides(asteroides, sprites, MAX_ASTEROIDES)

    sprites.update()

    if nave.rect.left <= 0:
        nave.rect.left = 0
    elif nave.rect.right >= WIDTH:
        nave.rect.right = WIDTH
    if nave.rect.top <= 0:
        nave.rect.top = 0
    elif nave.rect.bottom >= HEIGHT:
        nave.rect.bottom = HEIGHT

    for asteroide in asteroides:
        if asteroide.rect.bottom >= HEIGHT:
            asteroide.kill()
        lista = pygame.sprite.spritecollide(nave, asteroides, True)


    for laser in lasers:
        if laser.rect.top <= 0:
            laser.kill()
        
            lista = pygame.sprite.spritecollide(laser, asteroides, True) # identado
        if len(lista):
            laser.kill()

    screen.blit(fondo, ORIGIN)

    sprites.draw(screen)

    pygame.display.flip()

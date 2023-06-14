import pygame
import sys
import random

from config import *
from nave import Nave
from asteroide import Asteroide

sprites.add(nave)

while True:

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
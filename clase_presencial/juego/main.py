import pygame, sys
from config import *

reloj = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode(SIZE_SCREEN)

fondo = pygame.image.load("./assets/images/background.jpg").convert()
fondo = pygame.transform.scale(fondo, SIZE_SCREEN)


while True:
    reloj.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    
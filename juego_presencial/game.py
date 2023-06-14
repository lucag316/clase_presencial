import pygame
import sys

from config import *
from nave import Nave
from asteroide import Asteroide

class Game:
    def __init__(self) -> None:
        self.pygame.init()
        self.reloj = pygame.time.Clock()
        self.sonido = pygame.mixer.Sound("./sounds/laser.mp3")
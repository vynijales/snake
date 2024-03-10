import pygame
import random

from utils.constants import *
from components.manager import Manager
from components.snake import Snake


class Apple:
    def __init__(self):
        self.x = random.randint(1, 18) * SIZE
        self.y = random.randint(3, 18) * SIZE

    def respawn(self):
        while True:
            self.x = random.randint(1, 18) * SIZE
            self.y = random.randint(3, 18) * SIZE
            for s in Manager.group:
                if Manager.checkColision(self, s):
                    continue
            break
        Manager.grow()

    def draw(self, window):
        if self.x == Manager.group[-1].x and self.y == Manager.group[-1].y:
            self.respawn()
        return pygame.draw.rect(window, COLORS['RED'], (self.x, self.y, SIZE, SIZE))

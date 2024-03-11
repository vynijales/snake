import pygame
import random

from utils.base import resource_path
from utils.constants import *
from components.controller import Controller


class Apple:
    def __init__(self):
        self.x = random.randint(1, 18) * SIZE
        self.y = random.randint(3, 18) * SIZE

    def respawn(self):
        while True:
            self.x = random.randint(1, 18) * SIZE
            self.y = random.randint(3, 18) * SIZE
            for s in Controller.group:
                if Controller.checkColision(self, s):
                    continue
            break
        Controller.grow()

    def draw(self, window):

        food = pygame.mixer.Sound(resource_path('assets/sounds/food.wav'))
        food.set_volume(0.5)

        if Controller.checkColision(self, Controller.group[-1]):
            food.play()
            self.respawn()
        return pygame.draw.rect(window, COLORS['RED'], (self.x, self.y, SIZE, SIZE))

import pygame

from utils.constants import *

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = SIZE
        self.speed = SPEED

    def draw(self, window):
        return pygame.draw.rect(window, COLORS['GREEN'], (self.x, self.y, self.size, self.size))
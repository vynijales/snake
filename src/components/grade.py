import pygame

from utils.constants import *

def grade(window):
    for line in range(2, 24):
        pygame.draw.line(window, COLORS['GRADE'],
                         (0, line*SIZE), (HEIGHT, line*SIZE), 1)
    for row in range(0, 24):
        pygame.draw.line(
            window, COLORS['GRADE'], (row * SIZE, SIZE * 2), (row * SIZE, WIDTH), 1)
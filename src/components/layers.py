import pygame

from utils.base import message_display
from utils.constants import *
from components.controller import Controller
from components.grade import grade


def background(window):
    pygame.draw.rect(window, COLORS['WHITE'],
                     (0, SIZE * 2, WIDTH, HEIGHT - SIZE * 2))
    return grade(window)


def menu(window):
    Controller.score = len(Controller.group)-1
    message_display(f'{Controller.highscore:03}',
                    COLORS['GOLD'], 50, 25, 0, window)
    message_display(f'{Controller.score:03}',
                    COLORS['WHITE'], 50, WIDTH-100, 0, window)
    
    if Controller.pause:
        message_display('PAUSED', COLORS['WHITE'], 50, 220, 0, window)


def restartFrame(window):
    window.fill(COLORS['BACKGROUND'])
    message_display('PRESS  R  TO  RESTART',
                    COLORS['WHITE'], 40, 125, 250, window)

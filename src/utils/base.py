import pygame
import os, sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def message_display(text, color, size, x, y, window):
    font = pygame.font.Font('assets/fonts/ARCADECLASSIC.ttf', size)
    text = font.render(text, True, color)
    window.blit(text, (x, y))
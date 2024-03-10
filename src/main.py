import pygame
import random

from utils.base import *
from utils.constants import *
from components.manager import Manager
from components.snake import Snake
from components.apple import Apple
from components.grade import grade

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Snake')

Manager.reset()

def controller():
    Manager.keepInWindow()
    
    if Manager.alive:
        Manager.group[-1].draw(window)
        Manager.renderBody(window)
        Manager.move()
        Manager.snakeColision()

    else:
        Manager.setHighscore()
        window.fill(COLORS['BACKGROUND'])
        message_display('PRESS  R  TO  RESTART', COLORS['WHITE'], 40, 125, 250, window)

def isPaused():
    if not Manager.pause:
        COLORS['WHITE'] = (255, 255, 255)
        COLORS['GREEN'] = (36, 183, 36)
        COLORS['RED'] = (239, 39, 39)
        COLORS['GRADE'] = (200, 200, 200)
    else:
        message_display('PAUSED', COLORS['WHITE'], 50, 220, 0, window)
        COLORS['GREEN'] = (16, 83, 16)
        COLORS['RED'] = (209, 12, 12)
        COLORS['WHITE'] = COLORS['BACK']
        COLORS['GRADE'] = (150, 150, 150)


apple = Apple()
while not Manager.crashed:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            Manager.crashed = True
        if e.type == pygame.KEYDOWN:
            Manager.keyboard(e)
            if not Manager.pause and Manager.alive:
                if e.key == pygame.K_z:
                    Manager.grow()

            if e.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

    window.fill(COLORS['BACKGROUND'])

    isPaused()

    pygame.draw.rect(window, COLORS['WHITE'], (0, 50, WIDTH, HEIGHT-50))
    grade(window)
    apple.draw(window)
    controller()
    Manager.score = len(Manager.group)-1
    message_display(f'{Manager.highscore:03}', COLORS['GOLD'], 50, 25, 0, window)
    message_display(f'{Manager.score:03}', COLORS['WHITE'], 50, WIDTH-100, 0, window)
    pygame.display.update()
    Manager.timer.tick(FPS+(len(Manager.group)*0.1))

pygame.quit()

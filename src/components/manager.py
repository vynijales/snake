import pygame

from utils.constants import *
from components.snake import Snake


class Manager:
    alive = True
    timer = pygame.time.Clock()
    score = 0
    highscore = 0
    pause = False
    collision = False
    direction = None
    crashed = False
    size = SIZE
    speed = SPEED
    group = []

    @staticmethod
    def keepInWindow():
        if Manager.group[-1].y >= HEIGHT:
            Manager.group[-1].y = SIZE * 2
        elif Manager.group[-1].x >= WIDTH:
            Manager.group[-1].x = 0
        elif Manager.group[-1].x < 0:
            Manager.group[-1].x = WIDTH
        elif Manager.group[-1].y < SIZE * 2:
            Manager.group[-1].y = HEIGHT

    @staticmethod
    def renderBody(window):
        if len(Manager.group) == 1:
            Manager.group[0].draw(window)
        else:
            for s in range(len(Manager.group)-1):
                Manager.group[s].draw(window)
                if not Manager.pause:
                    Manager.group[s].x = Manager.group[s+1].x
                    Manager.group[s].y = Manager.group[s+1].y

    @staticmethod
    def keyboard(event):
        if not Manager.pause:
            Manager.arrows(event)

        if event.key == pygame.K_SPACE and Manager.alive:
            Manager.pause = not Manager.pause
        if event.key == pygame.K_r:
            Manager.reset()

    @staticmethod
    def arrows(event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and Manager.direction != 'DOWN':
                Manager.direction = 'UP'
            elif event.key == pygame.K_DOWN and Manager.direction != 'UP':
                Manager.direction = 'DOWN'
            elif event.key == pygame.K_LEFT and Manager.direction != 'RIGHT':
                Manager.direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and Manager.direction != 'LEFT':
                Manager.direction = 'RIGHT'

    @staticmethod
    def move():
        if not Manager.pause:
            if Manager.direction == 'UP':
                Manager.group[-1].y -= Manager.group[-1].speed
            elif Manager.direction == 'DOWN':
                Manager.group[-1].y += Manager.group[-1].speed
            elif Manager.direction == 'LEFT':
                Manager.group[-1].x -= Manager.group[-1].speed
            elif Manager.direction == 'RIGHT':
                Manager.group[-1].x += Manager.group[-1].speed

    @staticmethod
    def grow():
        if len(Manager.group) == 0:
            Manager.group.append(Snake(300, 275))
        else:
            Manager.group.insert(0, Snake(Manager.group[0].x, Manager.group[0].y))


    @staticmethod
    def checkColision(entity1, entity2):
        if entity1.x == entity2.x and entity1.y == entity2.y:
            return True
        return False

    @staticmethod
    def snakeColision():
        for s in range(len(Manager.group)-1):
            if Manager.checkColision(Manager.group[-1], Manager.group[s]):
                Manager.setHighscore()
                Manager.alive = False
    
    @staticmethod
    def setHighscore():
        if Manager.score > Manager.highscore:
            Manager.highscore = Manager.score

    @staticmethod
    def reset():
        Manager.group.clear()
        Manager.grow()
        Manager.alive = True
        Manager.score = 0
        Manager.pause = False
        Manager.collision = False
        Manager.direction = None
        Manager.crashed = False

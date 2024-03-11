import pygame

from utils.constants import *
from components.snake import Snake

class Controller:
    running = True
    alive = True
    timer = pygame.time.Clock()
    score = 0
    highscore = 0
    pause = False
    swappable = True
    collision = False
    direction = None
    size = SIZE
    speed = SPEED
    group = []

    @staticmethod
    def keyboard(event):
        if not Controller.pause:
            Controller.arrows(event)

        if event.key == pygame.K_SPACE and Controller.alive:
            Controller.pause = not Controller.pause
        if event.key == pygame.K_r:
            Controller.reset()

    @staticmethod
    def arrows(event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and Controller.direction != 'DOWN':
                Controller.direction = 'UP'
                Controller.swappable = False
            elif event.key == pygame.K_DOWN and Controller.direction != 'UP':
                Controller.direction = 'DOWN'
                Controller.swappable = False
            elif event.key == pygame.K_LEFT and Controller.direction != 'RIGHT':
                Controller.direction = 'LEFT'
                Controller.swappable = False
            elif event.key == pygame.K_RIGHT and Controller.direction != 'LEFT':
                Controller.direction = 'RIGHT'
                Controller.swappable = False

    @staticmethod
    def move():
        if not Controller.pause:
            if Controller.direction == 'UP':
                Controller.group[-1].y -= Controller.group[-1].speed
            elif Controller.direction == 'DOWN':
                Controller.group[-1].y += Controller.group[-1].speed
            elif Controller.direction == 'LEFT':
                Controller.group[-1].x -= Controller.group[-1].speed
            elif Controller.direction == 'RIGHT':
                Controller.group[-1].x += Controller.group[-1].speed

    @staticmethod
    def grow():
        if len(Controller.group) == 0:
            Controller.group.append(Snake(300, 275))
        else:
            Controller.group.insert(0, Snake(Controller.group[0].x, Controller.group[0].y))

    @staticmethod
    def checkColision(entity1, entity2):
        if entity1.x == entity2.x and entity1.y == entity2.y:
            return True
        return False

    @staticmethod
    def snakeColision():
        for s in range(len(Controller.group)-1):
            if Controller.checkColision(Controller.group[-1], Controller.group[s]):
                Controller.setHighscore()
                Controller.alive = False
    
    @staticmethod
    def setHighscore():
        if Controller.score > Controller.highscore:
            Controller.highscore = Controller.score

    @staticmethod
    def reset():
        Controller.group.clear()
        Controller.grow()
        Controller.alive = True
        Controller.score = 0
        Controller.pause = False
        Controller.collision = False
        Controller.direction = None

    @staticmethod
    def isPaused():
        if not Controller.pause:
            COLORS['WHITE'] = (255, 255, 255)
            COLORS['GREEN'] = (36, 183, 36)
            COLORS['RED'] = (239, 39, 39)
            COLORS['GRADE'] = (200, 200, 200)
        else:
            COLORS['GREEN'] = (16, 83, 16)
            COLORS['RED'] = (209, 12, 12)
            COLORS['WHITE'] = COLORS['BACK']
            COLORS['GRADE'] = (150, 150, 150)

    @staticmethod
    def keepInWindow():
        if Controller.group[-1].y >= HEIGHT:
            Controller.group[-1].y = SIZE * 2
        elif Controller.group[-1].x >= WIDTH:
            Controller.group[-1].x = 0
        elif Controller.group[-1].x < 0:
            Controller.group[-1].x = WIDTH
        elif Controller.group[-1].y < SIZE * 2:
            Controller.group[-1].y = HEIGHT

    @staticmethod
    def renderBody(window):
        Controller.group[-1].draw(window)
        
        for s in range(len(Controller.group)-1):
            Controller.group[s].draw(window)
            if not Controller.pause:
                Controller.group[s].x = Controller.group[s+1].x
                Controller.group[s].y = Controller.group[s+1].y

import pygame

from utils.base import *
from utils.constants import *
from components.controller import Controller
from components.apple import Apple
from components.grade import grade
from components.layers import menu, restartFrame


def main():
    pygame.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption('Snake')

    pygame.mixer.music.load(resource_path("assets/sounds/default.mp3"))
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1, 0.0)

    Controller.reset()

    apple = Apple()
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                break
            if e.type == pygame.KEYDOWN:
                if not Controller.pause and Controller.alive:
                    if e.key == pygame.K_z:
                        Controller.grow()

                Controller.keyboard(e)

                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    break

        window.fill(COLORS['BACKGROUND'])

        Controller.isPaused()

        pygame.draw.rect(window, COLORS['WHITE'],
                         (0, SIZE * 2, WIDTH, HEIGHT - SIZE * 2))
        grade(window)
        apple.draw(window)

        Controller.keepInWindow()

        if Controller.alive:
            Controller.renderBody(window)
            Controller.move()
            Controller.snakeColision()

        else:
            Controller.setHighscore()
            restartFrame(window)

        menu(window)
        Controller.swappable = True
        pygame.display.update()
        Controller.timer.tick(FPS+(len(Controller.group)*0.1))


if __name__ == "__main__":
    main()

from pygame import *
from random import *

size_window = 600

init()

window = display.set_mode((size_window, size_window))
title = display.set_caption('Snake')
crashed = False
pause = False
timer = time.Clock()

green = (36, 183, 36)
red = (239, 22, 22)
background = (7, 12, 25)
back = (225, 225, 225)
white = (250, 250, 250)
gold = (249, 166, 2)
color_grade = (200, 200, 200)

group = []
direction = 'none'
life = True
checking = False
can_swap = True

record = 0
score = 0


def message_display(text, color, size, x, y):
    fnt = font.Font("fonts\ARCADECLASSIC.ttf", size)
    text = fnt.render(text, True, color)
    window.blit(text, (x, y))


def controller():
    global life
    global score
    global record
    global pause
    global checking
    global can_swap

    if group[-1].y >= size_window:
        group[-1].y = 50
    if group[-1].x >= size_window:
        group[-1].x = 0
    if group[-1].x < 0:
        group[-1].x = size_window
    if group[-1].y < 50:
        group[-1].y = size_window

    if life:

        draw.rect(window, green, (group[-1].x, group[-1].y, group[-1].size, group[-1].size))
        if checking:
            life = False
        for s in range(len(group)-1):
            draw.rect(window, green, (group[s].x, group[s].y, group[s].size, group[s].size))
            if not pause:
                group[s].x = group[s+1].x
                group[s].y = group[s+1].y
        if not pause:
            if direction == 'up' and direction != 'down':
                group[-1].y -= group[-1].speed
            elif direction == 'down' and direction != 'up':
                group[-1].y += group[-1].speed
            elif direction == 'left' and 'right':
                group[-1].x -= group[-1].speed
            elif direction == 'right' and direction != 'left':
                group[-1].x += group[-1].speed
            for s in range(len(group)-1):
                if group[s].x == group[-1].x and group[s].y == group[-1].y:
                    checking = True
            if not can_swap:
                can_swap = True
    else:
        if record < score:
            record = score
        window.fill(background)
        message_display("PRESS  R  TO  RESTART", white, 40, 125, 250)


def grade():

    for line in range(2, 24):
        draw.line(window, color_grade, (0, line*25), (size_window, line*25), 1)
    for row in range(0, 24):
        draw.line(window, color_grade, (row * 25, 50), (row * 25, size_window), 1)


class Snake:
    def __init__(self):
        self.x = 300
        self.y = 275
        self.size = 25
        self.speed = 25
        group.insert(0, self)


head = Snake()


class Apple:
    def __init__(self):
        self.size = 25
        self.x = randint(1, 18) * self.size
        self.y = randint(3, 18) * self.size

    def respawn(self):
        x_y = (self.x, self.y)

        while True:
            self.x = randint(1, 18) * self.size
            self.y = randint(3, 18) * self.size
            for s in group:
                if self.x == s.x and self.y == s.y:
                    continue
            break
        body = Snake()
        body.x, body.y = x_y[0], x_y[1]

    def draw(self):
        if self.x == group[-1].x and self.y == group[-1].y:
            self.respawn()
        draw.rect(window, red, (apple.x, apple.y, apple.size, apple.size))


apple = Apple()
while not crashed:
    for e in event.get():
        if e.type == QUIT:
            crashed = True
        if e.type == KEYDOWN:
            if not pause and can_swap:
                if (e.key == K_w or e.key == K_UP) and direction != 'down' and group[-1].x % 25 == 0:
                    direction = 'up'
                    can_swap = not can_swap
                if (e.key == K_a or e.key == K_LEFT) and direction != 'right' and group[-1].y % 25 == 0:
                    direction = 'left'
                    can_swap = not can_swap
                if (e.key == K_s or e.key == K_DOWN) and direction != 'up' and group[-1].x % 25 == 0:
                    direction = 'down'
                    can_swap = not can_swap
                if (e.key == K_d or e.key == K_RIGHT) and direction != 'left' and group[-1].y % 25 == 0:
                    direction = 'right'
                    can_swap = not can_swap
            if e.key == K_r:
                group.clear()
                head = Snake()
                direction = 'None'
                life = True
                checking = False
                can_swap = False
                pause = False
            if e.key == K_SPACE and life:
                pause = not pause
            if e.key == K_z:
                body = Snake()

    window.fill(background)
    if not pause:
        color = (200, 200, 200)
        white = (255, 255, 255)
        green = (36, 183, 36)
        red = (239, 39, 39)
        color_grade = (200, 200, 200)
    else:
        message_display("PAUSED", white, 50, 220, 0)
        green = (16, 83, 16)
        red = (209, 12, 12)
        white = back
        color_grade = (150, 150, 150)

    draw.rect(window, white, (0, 50, size_window, size_window-50))
    grade()
    apple.draw()
    controller()
    score = len(group)-1
    message_display(f"{record:03}", gold, 50, 25, 0)
    message_display(f"{score:03}", white, 50, size_window-100, 0)
    display.update()
    timer.tick(10+(len(group)*0.1))

quit()

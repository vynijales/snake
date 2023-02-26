from pygame import *
from random import *

class GameState:
    def __init__(self):
        self.life = True
        self.timer = time.Clock()
        self.score = 0
        self.record = 0
        self.pause = False
        self.collision = False
        self.can_swap = True
        self.direction = None
        self.crashed = False
        self.segment_size = 10
        self.segment_speed = 10
        self.segment_positions = [(0, 0), (10, 0), (20, 0)]

manager = GameState()

init()

size_window = 600 # Tamanho da tela
window = display.set_mode((size_window, size_window)) # Setando largura e altura para o display
title = display.set_caption('Snake') # Setando o título

colors = {
    'green': (36, 183, 36),
    'red' : (239, 22, 22),
    'background' : (7, 12, 25),
    'back' : (225, 225, 225),
    'white' : (250, 250, 250),
    'gold' : (249, 166, 2),
    'color_grade' : (200, 200, 200)
}

group = []

def message_display(text, color, size, x, y):
    fnt = font.Font('fonts\ARCADECLASSIC.ttf', size)
    text = fnt.render(text, True, color)
    window.blit(text, (x, y))

def setInWindow():
    if group[-1].y >= size_window:
        group[-1].y = 50
    elif group[-1].x >= size_window:
        group[-1].x = 0
    elif group[-1].x < 0:
        group[-1].x = size_window
    elif group[-1].y < 50:
        group[-1].y = size_window

def controller():
    setInWindow()

    if manager.life:
        draw.rect(window, colors['green'], (group[-1].x, group[-1].y, group[-1].size, group[-1].size))
        
        if manager.collision: manager.life = False

        for s in range(len(group)-1):
            draw.rect(window, colors['green'], (group[s].x, group[s].y, group[s].size, group[s].size))
            if not manager.pause: # Se não estiver pausado, siga as cordenadas da instância seguinte da lista
                group[s].x = group[s+1].x
                group[s].y = group[s+1].y
            
            # if group[s].x == group[-1].x and group[s].y == group[-1].y: # Checa se algum seguimento colidiu com a cabeça da cobra
            #     manager.collision = True

        if not manager.pause: # Se não estiver pausado, move a cobra seguindo as restrições.
            if manager.direction == 'UP' and manager.direction != 'DOWN': group[-1].y -= group[-1].speed
            elif manager.direction == 'DOWN' and manager.direction != 'UP': group[-1].y += group[-1].speed
            elif manager.direction == 'LEFT' and 'RIGHT': group[-1].x -= group[-1].speed
            elif manager.direction == 'RIGHT' and manager.direction != 'LEFT': group[-1].x += group[-1].speed
               
            if not manager.can_swap:
                manager.can_swap = True
            
            for s in range(len(group)-1):
                if group[s].x == group[-1].x and group[s].y == group[-1].y: # Checa se algum seguimento colidiu com a cabeça da cobra
                    manager.collision = True

    else:
        if manager.record < score: manager.record = score
        window.fill(colors['background'])
        message_display('PRESS  R  TO  RESTART', colors['white'], 40, 125, 250)


def grade(): # Desenhando as grades do mapa
    for line in range(2, 24):
        draw.line(window, colors['color_grade'], (0, line*25), (size_window, line*25), 1)
    for row in range(0, 24):
        draw.line(window, colors['color_grade'], (row * 25, 50), (row * 25, size_window), 1)


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
        draw.rect(window, colors['red'], (apple.x, apple.y, apple.size, apple.size))

def isPaused():
    if not manager.pause:
        colors['white'] = (255, 255, 255)
        colors['green'] = (36, 183, 36)
        colors['red'] = (239, 39, 39)
        colors['color_grade'] = (200, 200, 200)
    else:
        message_display('PAUSED', colors['white'], 50, 220, 0)
        colors['green'] = (16, 83, 16)
        colors['red'] = (209, 12, 12)
        colors['white'] = colors['back']
        colors['color_grade'] = (150, 150, 150)


apple = Apple()
while not manager.crashed:
    for e in event.get():
        if e.type == QUIT:
            manager.crashed = True
        if e.type == KEYDOWN:
            if not manager.pause and manager.can_swap:
                if (e.key == K_w or e.key == K_UP) and manager.direction != 'DOWN' and group[-1].x % 25 == 0: # CIMA
                    manager.direction = 'UP'
                    manager.can_swap = not manager.can_swap
                if (e.key == K_a or e.key == K_LEFT) and manager.direction != 'RIGHT' and group[-1].y % 25 == 0: # ESQUERDA
                    manager.direction = 'LEFT'
                    manager.can_swap = not manager.can_swap
                if (e.key == K_s or e.key == K_DOWN) and manager.direction != 'UP' and group[-1].x % 25 == 0: # BAIXO
                    manager.direction = 'DOWN'
                    manager.can_swap = not manager.can_swap
                if (e.key == K_d or e.key == K_RIGHT) and manager.direction != 'LEFT' and group[-1].y % 25 == 0: # ESQUERDA
                    manager.direction = 'RIGHT'
                    manager.can_swap = not manager.can_swap
            if e.key == K_r: # RESET
                group.clear()
                head = Snake()
                manager.direction = None
                manager.life = True
                manager.collision = False
                manager.can_swap = False
                manager.pause = False
                # for i in (manager.collision, manager.can_swap, manager.pause): i = False # Resetando valores
            if e.key == K_SPACE and manager.life: manager.pause = not manager.pause # PAUSE
            if e.key == K_ESCAPE: quit()
            if e.key == K_z: body = Snake() # (Z) CHEAT DESENVOLVEDOR

    window.fill(colors['background'])
    
    isPaused()

    draw.rect(window, colors['white'], (0, 50, size_window, size_window-50))
    grade()
    apple.draw()
    controller()
    score = len(group)-1
    message_display(f'{manager.record:03}', colors['gold'], 50, 25, 0)
    message_display(f'{score:03}', colors['white'], 50, size_window-100, 0)
    display.update()
    manager.timer.tick(10+(len(group)*0.1))

quit()

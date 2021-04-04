import pygame
import config as cfg
from dot import Dot 

class Snake:

    def __init__(self, window, color):
        self.window = window
        self.len = 4
        self.dots = []
        self.color = color

        # init default dots
        for i in range(self.len):
            x =  - i * cfg.C_S
            y = 0
            d = Dot(self.window, x, y, self.color)
            self.dots.append(d)

            # for dot in self.dots:
            #     print('[{},{}]'.format(dot.x, dot.y))

    def draw(self):
        for dot in self.dots:
            dot.draw()

    def move(self, xDirection, yDirection, eatApple = False):
        # xDirection and yDirection will determine the direction of the snake
        
        # move snake
        for i in range(len(self.dots) - 1, 0, -1):
            self.dots[i].x = self.dots[i - 1].x
            self.dots[i].y = self.dots[i - 1].y

        self.dots[0].x += cfg.C_S * xDirection
        self.dots[0].y += cfg.C_S * yDirection

        # when the snake touches the edges
        if self.dots[0].x >= cfg.W:
            self.dots[0].x = 0
        
        if self.dots[0].x < 0:
            self.dots[0].x = cfg.W - cfg.C_S

        if self.dots[0].y >= cfg.H:
            self.dots[0].y = 0
        
        if self.dots[0].y < 0:
            self.dots.y = cfg.H - cfg.C_S
        

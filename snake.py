import pygame
import config as cfg
from dot import Dot 

class Snake:

    def __init__(self, window, color):
        self.window = window
        self.len = 4
        self.pos = []
        self.dots = []
        self.color = color

        # init default dots
        for i in range(self.len):
            x = - i
            y = 0
            d = Dot(self.window, x, y, self.color)
            self.dots.append(d)
import pygame
import config as cfg

class Dot:

    def __init__(self, window, x, y, color):
        self.window = window
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        width = cfg.C_S - 2 * cfg.LINE_W
        height = cfg.C_S - 2 * cfg.LINE_W
        x = self.x + 2 * cfg.LINE_W
        y = self.y + 2 * cfg.LINE_W

        pygame.draw.rect(self.window, self.color, pygame.Rect(x, y, width, height))
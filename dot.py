import pygame
import config as cf

class Dot:

    def __init__(self, surface, x, y, color):
        self.x, self.y = x, y
        self.surface = surface
        self.color = color
    
    def draw(self):
        pygame.draw.rect(self.surface, self.color, pygame.Rect(self.x, self.y, cf.CELL_SIZE, cf.CELL_SIZE))
import pygame
import config as cf

class Dot:

    def __init__(self, surface, x, y):
        self.x, self.y = x, y
        self.surface = surface
    
    def draw(self):
        pygame.draw.rect(self.surface, cf.SNAKE_COLOR, pygame.Rect(self.x, self.y, cf.CELL_SIZE, cf.CELL_SIZE))
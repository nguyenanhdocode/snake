import pygame
import config as cf
import random
from dot import Dot

class Food:

    def __init__(self, surface):
        self.color = cf.FOOD_COLOR
        self.x, self.y = 0, 0
        self.surface = surface


    def genFood(self):
        foodX = (random.randint(0, cf.COLS - 1)) * cf.CELL_SIZE
        foodY = (random.randint(0, cf.ROWS - 1)) * cf.CELL_SIZE
        self.x = foodX
        self.y = foodY

    def draw(self):
        dot = Dot(self.surface, self.x, self.y, cf.FOOD_COLOR)
        dot.draw()
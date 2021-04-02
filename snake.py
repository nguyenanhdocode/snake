import config as cf
from dot import Dot


class Snake:

    def __init__(self, surface):

        self.pos = [cf.CELL_SIZE * 2, 0]
        self.snakeBoy = [
            [0, 0],
            [cf.CELL_SIZE, 0],
            [cf.CELL_SIZE * 2, 0]
        ]
        self.currentDir = cf.RIGHT
        self.chDir = cf.RIGHT
        self.surface = surface

    def draw(self):
        for dot in self.snakeBoy:
            d = Dot(self.surface, dot[0], dot[1])
            d.draw()
import config as cf
from dot import Dot


class Snake:

    def __init__(self, surface):

        self.pos = [cf.CELL_SIZE * 2, 0]
        self.snakeBody = [
            [0, 0],
            [cf.CELL_SIZE, 0],
            [cf.CELL_SIZE * 2, 0]
        ]
        self.currentDir = cf.RIGHT
        self.chDir = cf.RIGHT
        self.surface = surface

    def draw(self):
        for dot in self.snakeBody:
            d = Dot(self.surface, dot[0], dot[1])
            d.draw()

    def move(self):
        if self.currentDir == cf.RIGHT:
            self.pos[0] += cf.CELL_SIZE
        elif self.currentDir == cf.DOWN:
            self.pos[1] += cf.CELL_SIZE
        elif self.currentDir == cf.LEFT:
            self.pos[0] -= cf.CELL_SIZE
        elif self.currentDir == cf.UP:
            self.pos[1] -= cf.CELL_SIZE

        newPos = self.pos.copy()
        self.snakeBody.append(newPos)
        self.snakeBody.pop(0)

    def changeDirTo(self, to):
        if to == cf.RIGHT and self.currentDir != cf.LEFT:
            self.currentDir = cf.RIGHT
        
        elif to == cf.UP and self.currentDir != cf.DOWN:
            self.currentDir = cf.UP

        elif to == cf.LEFT and self.currentDir != cf.RIGHT:
            self.currentDir = cf.LEFT
        
        elif to == cf.DOWN and self.currentDir != cf.UP:
            self.currentDir = cf.DOWN
        
            
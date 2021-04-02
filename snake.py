import config as cf
from dot import Dot
from food import Food

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
            d = Dot(self.surface, dot[0], dot[1], cf.SNAKE_COLOR)
            d.draw()

    def move(self, foodIsAte = False):
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

        if not foodIsAte:
            self.snakeBody.pop(0)

        if self.isHitRight() and self.currentDir == cf.RIGHT:
            self.pos[0] = -cf.CELL_SIZE

        elif self.isHitLeft() and self.currentDir == cf.LEFT:
            self.pos[0] = cf.WINDOW_WIDTH

        elif self.isHitTop() and self.currentDir == cf.UP:
            self.pos[1] = cf.WINDOW_HEIGHT

        elif self.isHitBottom() and self.currentDir == cf.DOWN:
            self.pos[1] = -cf.CELL_SIZE

    def foodIsAte(self, foodX, foodY):
        if self.pos[0] == foodX and self.pos[1] == foodY:
            return True
        return False

    def changeDirTo(self, to):
        if to == cf.RIGHT and self.currentDir != cf.LEFT:
            self.currentDir = cf.RIGHT
        
        elif to == cf.UP and self.currentDir != cf.DOWN:
            self.currentDir = cf.UP

        elif to == cf.LEFT and self.currentDir != cf.RIGHT:
            self.currentDir = cf.LEFT
        
        elif to == cf.DOWN and self.currentDir != cf.UP:
            self.currentDir = cf.DOWN
    
    def isHitRight(self):
        if self.pos[0] >= cf.WINDOW_WIDTH:
            return True
        return False

    def isHitLeft(self):
        if self.pos[0] <= 0:
            return True
        return False

    def isHitTop(self):
        if self.pos[1] <= 0:
            return True
        return False

    def isHitBottom(self):
        if self.pos[1] >= cf.WINDOW_HEIGHT:
            return True
        return False
            
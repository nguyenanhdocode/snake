import config as cf

class Snake:

    def __init__(self):

        self.pos = [cf.CELL_SIZE * 2, 0]
        self.snakeBoy = [
            [0, 0],
            [cf.CELL_SIZE, 0],
            [cf.CELL_SIZE * 2, 0]
        ]
        self.currentDir = cf.RIGHT
        self.chDir = cf.RIGHT

    def draw(self):
        for dot in self.snakeBoy:
            pass 
        
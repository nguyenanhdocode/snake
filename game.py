# snake game using oop
# I have referenced at page: https://python-forum.io/Thread-PyGame-Basic-Snake-game-using-OOP
# 4 April, 2021
# My enail: nguyenanhdo200213@gmail.com

import pygame
import config as cfg
from snake import Snake

pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode(cfg.WND_SIZE)
pygame.display.set_caption("Snake")



# create snake
snake = Snake(window, cfg.SNAKE_COLOR)

# x, y direction
# x = 0 (not move), x = 1 (move right), x = -1 (move left)
# y = 0 (mot move), y = 1 (move down), y = -1 (move up)
xDirection = 1
yDirection = 0

# DRAW GRID LINES
def drawGird():
    for i in range(cfg.R):
        pygame.draw.line(window, cfg.GRAY, (0, i * cfg.C_S), (cfg.W, i * cfg.C_S), cfg.LINE_W)

    for i in range(cfg.C):
        pygame.draw.line(window, cfg.GRAY, (i * cfg.C_S, 0), (i * cfg.C_S, cfg.H), cfg.LINE_W)

# main loop
while True:

    # fill windows color
    window.fill(cfg.BLACK)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()

        # control the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and yDirection != 1:
                yDirection = -1
                xDirection = 0
                break
                
            
            elif event.key == pygame.K_RIGHT and xDirection != -1:
                xDirection = 1
                yDirection = 0
                break

            elif event.key == pygame.K_LEFT and xDirection != 1:
                xDirection = -1
                yDirection = 0
                break

            elif event.key == pygame.K_DOWN and yDirection != -1:
                yDirection = 1
                xDirection = 0
                break


    # draw snake
    snake.draw()

    # move
    snake.move(xDirection, yDirection, False)

    # draw grid
    drawGird()
    
    pygame.display.flip()
    clock.tick(cfg.FRAME_RATE)


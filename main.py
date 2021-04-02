import pygame
import os
import config as cf
from snake import Snake

pygame.init()

surface = pygame.display.set_mode((cf.WINDOW_WIDTH, cf.WINDOW_HEIGHT))

# new snake
snake = Snake(surface)

# key status


while (True):

    pygame.time.delay(cf.DELAY)

    surface.fill(cf.BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.changeDirTo(cf.DOWN)
            
            elif event.key == pygame.K_RIGHT:
                snake.changeDirTo(cf.RIGHT)
            
            elif event.key == pygame.K_LEFT:
                snake.changeDirTo(cf.LEFT)

            elif event.key == pygame.K_UP:
                snake.changeDirTo(cf.UP)

    # draw snake
    snake.draw()

    # move snake
    snake.move()

    pygame.display.flip()
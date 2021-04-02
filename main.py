import pygame
import os
import config as cf
from snake import Snake

pygame.init()

surface = pygame.display.set_mode((cf.WINDOW_WIDTH, cf.WINDOW_HEIGHT))

# new snake
snake = Snake(surface)

while (True):

    surface.fill(cf.BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # draw snake
    snake.draw()

    pygame.display.flip()
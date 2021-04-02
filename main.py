import pygame
import os
import config as cf

pygame.init()

surface = pygame.display.set_mode((cf.WINDOW_WIDTH, cf.WINDOW_HEIGHT))

while (True):

    surface.fill(cf.BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()
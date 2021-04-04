import pygame
import config as cfg
from snake import Snake

pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode(cfg.WND_SIZE)
pygame.display.set_caption("Snake")

# DRAW GRID LINES
for i in range(cfg.R):
    pygame.draw.line(window, cfg.GRAY, (0, i * cfg.C_S), (cfg.W, i * cfg.C_S), cfg.LINE_W)

for i in range(cfg.C):
    pygame.draw.line(window, cfg.GRAY, (i * cfg.C_S, 0), (i * cfg.C_S, cfg.H), cfg.LINE_W)

# create snake
snake = 

while True:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()

    
    pygame.display.flip()
    clock.tick(cfg.FRAME_RATE)


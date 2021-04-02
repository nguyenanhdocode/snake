import pygame
import os
import config as cf
from snake import Snake
from food import Food

pygame.init()

surface = pygame.display.set_mode((cf.WINDOW_WIDTH, cf.WINDOW_HEIGHT))

# new snake
snake = Snake(surface)

# new food
food = Food(surface)
food.genFood()


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

    #draw food
    food.draw()

    # draw snake
    snake.draw()

    # move snake
    isFoodAte = snake.foodIsAte(food.x, food.y)
    if isFoodAte:
        snake.move(isFoodAte)
        food.genFood()
    else:
        snake.move()

    pygame.display.flip()
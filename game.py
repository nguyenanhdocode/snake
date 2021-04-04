# snake game using oop
# I have referenced at page: https://python-forum.io/Thread-PyGame-Basic-Snake-game-using-OOP
# 4 April, 2021
# My enail: nguyenanhdo200213@gmail.com

import os
import pygame
import config as cfg
from snake import Snake
from apple import Apple


pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode(cfg.WND_SIZE)

pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# game font
font = pygame.font.SysFont("courier new", 20)
font2 = pygame.font.SysFont("courier new", 30)

# game sounds
beep = pygame.mixer.Sound(os.path.join('sounds','beep.mp3'))
gameover = pygame.mixer.Sound(os.path.join('sounds','gameover.mp3'))


eatApple = False
isDie = False
isWin = False
score = cfg.SNAKE_DEFAULT_LENGTH
level = 1
 # to set level
count = 0
isStart = False

# x, y direction
# x = 0 (not move), x = 1 (move right), x = -1 (move left)
# y = 0 (mot move), y = 1 (move down), y = -1 (move up)
xDirection = 1
yDirection = 0

# create snake
snake = Snake(window, cfg.SNAKE_COLOR)

# create apple
apple = Apple(window, cfg.APPLE_COLOR, snake.dots)

# draw grid
def drawGird():
    for i in range(cfg.R + 1):
        pygame.draw.line(window, cfg.GRAY, (0, i * cfg.C_S), (cfg.W - cfg.RIGHT_SPACE, i * cfg.C_S), cfg.LINE_W)

    for i in range(cfg.C + 1):
        pygame.draw.line(window, cfg.GRAY, (i * cfg.C_S, 0), (i * cfg.C_S, cfg.H), cfg.LINE_W)

def control():
    global xDirection
    global yDirection
    global isStart
    global isDie
    global snake
    global score
    global level

    for event in pygame.event.get():
            
        if event.type == pygame.QUIT:
            pygame.quit()

        # control the snake
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                isStart = True
                isDie = False
                isWin = False
                snake = Snake(window, cfg.SNAKE_COLOR)
                score = cfg.SNAKE_DEFAULT_LENGTH
                level = 0
                xDirection = 1
                yDirection =0
                break

            if event.key == pygame.K_UP and yDirection != 1:
                yDirection = 0
                yDirection = -1
                xDirection = 0
                break              
            
            elif event.key == pygame.K_RIGHT and xDirection != -1:
                xDirection = 0
                xDirection = 1
                yDirection = 0
                break

            elif event.key == pygame.K_LEFT and xDirection != 1:
                xDirection = 0
                xDirection = -1
                yDirection = 0
                break

            elif event.key == pygame.K_DOWN and yDirection != -1:
                yDirection = 0
                yDirection = 1
                xDirection = 0
                break    

# display point and other text
def displayScore():
    global isStart
    global isDie
     # display score
    s = font.render('Your score:', True, cfg.GREEN)
    window.blit(s, (cfg.C * cfg.C_S + 10, 10))
    s = font.render('Level:', True, cfg.GREEN)
    window.blit(s, (cfg.C * cfg.C_S + 10, 120))

    # draw box
    pygame.draw.rect(window, cfg.RED, [cfg.C * cfg.C_S + 10, 35, 150, 50], 2)
    pygame.draw.rect(window, cfg.RED, [cfg.C * cfg.C_S + 10, 145, 150, 50], 2)

    s = font2.render(str(score), True, cfg.WHITE)
    window.blit(s, (cfg.C * cfg.C_S + 18, 43))

    s = font2.render(str(level), True, cfg.WHITE)
    window.blit(s, (cfg.C * cfg.C_S + 18, 152))

    if not isStart:
        s = font2.render('Press space to start...', True, cfg.GREEN)
        window.blit(s, (80, 265))
    if isDie:
        s= font2.render('You died!', True, cfg.RED)
        window.blit(s, (200, 265))
        s = font2.render('Press space to start again...', True, cfg.GREEN)
        window.blit(s, (60, 300))

    if isWin:
        s= font2.render('You win!', True, cfg.RED)
        window.blit(s, (200, 265))
        s = font2.render('Press space to start again...', True, cfg.GREEN)
        window.blit(s, (60, 300))

def drawImage():
    imgSnake = pygame.transform.scale(pygame.image.load(os.path.join('imgs','snake.png')), (200, 200))
    window.blit(imgSnake, (cfg.C * cfg.C_S + 10, 400))

# main loop
while True:
   
    # fill windows color
    window.fill(cfg.BLACK)

    control()

    # draw snake
    snake.draw()

    # draw apple
    apple.draw()

    # Check whether the snake has eaten the apple or not
    if (snake.dots[0].x == apple.x and snake.dots[0].y == apple.y):
       
        eatApple = True
        # crate new apple
        apple = Apple(window, cfg.APPLE_COLOR, snake.dots)
        score += 1
        count += 1
        
        # set level
        if count == 10:
            pygame.mixer.Sound.play(beep)
            level += 1
            count = 0
    
    # check die
    isDie = snake.checkDie()

    # check win
    isWin = snake.checkWin()
        
    # move snake
    if not isDie and isStart and not isWin:
        # eatApple is True so snake.move() will append new dot to dots
        snake.move(xDirection, yDirection, eatApple)
    # Now we reset eatApple
    eatApple = False
    

    # draw grid
    drawGird()

    # display score
    displayScore()

    # draw snake imgage
    drawImage()
    
    pygame.display.flip()

    clock.tick(cfg.FRAME_RATE)


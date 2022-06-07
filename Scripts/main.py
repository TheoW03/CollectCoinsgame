from time import time
import pygame
from main_Character import mainChar
from pygame.locals import *
import random

import os

pygame.init()
WIN_HEIGHT, WIN_WIDTH = 400, 400
WIN = pygame.display.set_mode((WIN_HEIGHT, WIN_WIDTH))
FPS = 60
VEL = 2

# random globals
die = False
arr = []
timeElaspsed = 0
highscore = 0
# maincharacter

player = pygame.image.load(os.path.join('Sprites', 'sprite1.PNG'))
playerObj = pygame.transform.scale(player, (30, 30))
sRect = pygame.Rect(100, 100, 30, 30)
m = mainChar(sRect)

# coin

coin = pygame.image.load(os.path.join('Sprites', 'Coins.PNG'))
coinObj = pygame.transform.scale(coin, (20, 20))
coinRect = pygame.Rect(200, 100, 20, 20)
coins = [mainChar(coinRect, coinObj)]

# coinRect = pygame.Rect(200, 100, 50, 40)
# coins = mainChar(coinRect)

# text
score = 0
font = pygame.font.Font('freesansbold.ttf', 16)
text = font.render('score: {}'.format(score), True, (0, 0, 0), (255, 255, 255))

"""
draw sprites
"""
def draw_sprites():
    global sRect, m, coins, score, die, timeElaspsed, FPS, highscore
    clock = pygame.time.Clock()
    clock.tick(FPS)
    r = random.randrange(0, 4000)
    
    if r < 10:
        coins.append(mainChar(pygame.Rect(random.randrange(3, 300), random.randrange(3, 300), 20, 20), coinObj))

    color = (50.2, 50.2, 50.2)
    WIN.fill(color)
    WIN.blit(playerObj, m.getVector())
    for i in range(len(coins)):
        WIN.blit(coins[i].getScale(), coins[i].getVector())

    text = font.render('score: {}'.format(score), True,
                       (0, 0, 0), (255, 255, 255))
    timeText = font.render('time: {}'.format(
        timeElaspsed), True, (0, 0, 0), (255, 255, 255))
    highscoreText = font.render('highssocre: {}'.format(highscore), True,(0, 0, 0), (255, 255, 255))
    # print(timeElaspsed)
    #if die
    if score <= -1:
        color = (255, 0, 0)
        WIN.fill(color)
        dieFont = pygame.font.Font('freesansbold.ttf', 30)
        dieText = dieFont.render("YOU DIED LOL", True, (0, 0, 0), (255, 255, 255))
        WIN.blit(dieText, (100, 200))
        die = True
    WIN.blit(timeText, (300, 12))
    WIN.blit(text, (12, 12))
    WIN.blit(highscoreText, (12, 360))
    pygame.display.update()


"""
on collide method
"""


def doStuff():
    global m, coins, WIN_HEIGHT, WIN_WIDTH, score,highscore
    for i in range(len(coins)):
        if coins[i].getRectangle().colliderect(sRect):
            coins[i].setVector(random.randrange(
                50, WIN_HEIGHT), random.randrange(50, WIN_WIDTH))
            ranInt = random.randrange(0, 2)
            if ranInt == 1:
                score += 1
            else:
                score -= 1
            if score > highscore:
                highscore = score

    # if clearLast:
    #     coins.pop()

    # if(.colliderect(sRect)):
    #     coins.setVector(random.randrange(50, WIN_HEIGHT),random.randrange(50, WIN_WIDTH))
    #


"""
key events
"""


def events():
    global m, VEL, die
    if die:
        return
    m.setVelocity(VEL)
    keys_pressed = pygame.key.get_pressed()
    if(keys_pressed[pygame.K_a]):
        m.move_left()
    if(keys_pressed[pygame.K_d]):
        m.move_right()
    if(keys_pressed[pygame.K_w]):
        m.move_up()
    if(keys_pressed[pygame.K_s]):
        m.move_down()


"""
main loop
"""


def main():
    global sRect, m, FPS, timeElaspsed, die
    clock = pygame.time.Clock()
    i = 0

    close = True
    while close:
        clock.tick(FPS)
        if i >= 60 and i != 0 and die == False:
            i = 0
            timeElaspsed += 1
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                close = False
        i += 1
        draw_sprites()
        doStuff()
        events()

    pygame.quit()


if __name__ == '__main__':
    main()

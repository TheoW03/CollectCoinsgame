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
# maincharacter

player = pygame.image.load(os.path.join('Sprites', 'sprite1.PNG'))
playerObj = pygame.transform.scale(player, (30, 30))
sRect = pygame.Rect(100, 100, 50, 40)
m = mainChar(sRect)

# coin
coin = pygame.image.load(os.path.join('Sprites', 'Coins.PNG'))
coinObj = pygame.transform.scale(coin, (20, 20))
coinRect = pygame.Rect(200, 100, 50, 40)
coins = mainChar(coinRect)

#text
score = 0
font = pygame.font.Font('freesansbold.ttf', 16)
text = font.render('score: {}'.format(score), True, (0,0,0), (255,255,255))

"""
draw sprites
"""
def draw_sprites():
    global sRect, m, coins,score
    color = (50.2, 50.2, 50.2)
    WIN.fill(color)
    WIN.blit(playerObj, m.getVector())
    WIN.blit(coinObj, coins.getVector())
    text = font.render('score: {}'.format(score), True, (0,0,0), (255,255,255))
    WIN.blit(text, (12,12))
    pygame.display.update()


def doStuff():
    global m, coins, WIN_HEIGHT, WIN_WIDTH,score

    if(sRect.colliderect(coinRect)):
        coins.setVector(random.randrange(50, WIN_HEIGHT),random.randrange(50, WIN_WIDTH))
        score += 1       

def events():
    global m, VEL
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


def main():
    global sRect, m, FPS
    clock = pygame.time.Clock()

    close = True
    while close:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                close = False
        draw_sprites()
        doStuff()
        events()

    pygame.quit()


if __name__ == '__main__':
    main()

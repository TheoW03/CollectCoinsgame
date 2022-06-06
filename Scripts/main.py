import pygame
from main_Character import mainChar
from pygame.locals import *

import os

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


def draw_sprites():
    global sRect, m, coins
    color = (50.2, 50.2, 50.2)
    WIN.fill(color)
    WIN.blit(playerObj, m.getVector())
    WIN.blit(coinObj, coins.getVector())
    pygame.display.update()


def events():
    global m,VEL
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
        events()
    pygame.quit()


if __name__ == '__main__':
    main()

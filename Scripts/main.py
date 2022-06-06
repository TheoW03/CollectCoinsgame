import pygame
from main_Character import mainChar
from pygame.locals import *

import os

WIN_HEIGHT, WIN_WIDTH = 400, 400
WIN = pygame.display.set_mode((WIN_HEIGHT, WIN_WIDTH))


# sprites
player = pygame.image.load(os.path.join('Sprites', 'sprite1.PNG'))
playerObj = pygame.transform.scale(player, (50, 40))
sRect = pygame.Rect(100, 100, 50, 40)
m = mainChar(sRect)


def draw_sprites():
    global sRect, m
    color = (50.2, 50.2, 50.2)
    WIN.fill(color)
    WIN.blit(playerObj, m.getVector())
    pygame.display.update()
def main():
    global sRect,m
    close = True
    while close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = False
        draw_sprites()
    pygame.quit()


if __name__ == '__main__':
    main()

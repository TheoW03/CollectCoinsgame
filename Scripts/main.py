import pygame
from main_Character import mainChar

WIN_HEIGHT, WIN_WIDTH = 400, 400
WIN = pygame.display.set_mode((WIN_HEIGHT, WIN_WIDTH))


def main():
    close = True
    while close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = False
    pygame.quit()


if __name__ == '__main__':
    main()

import pygame
from config import *


def bound(screen, color: tuple):

    pygame.draw.rect(screen, color, (0, 55, Config.SCREEN_WIDTH, 20))
    pygame.draw.rect(screen, color, (0, 55, 20, (Config.SCREEN_HEIGHT - 55)))
    pygame.draw.rect(
        screen, color, ((Config.SCREEN_WIDTH - 20), 55, 20, (Config.SCREEN_HEIGHT - 55))
    )
    pygame.draw.rect(
        screen, color, (20, (Config.SCREEN_HEIGHT - 20), (Config.SCREEN_WIDTH - 40), 20)
    )

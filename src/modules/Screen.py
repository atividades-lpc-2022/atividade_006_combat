import pygame

from modules.Dimension import Dimension


class Screen:
    def __init__(self, dimension: Dimension, background: pygame.sprite.Sprite):
        self.background = background
        self.dimension = dimension

    def draw(self):  # TODO: Draw screen
        print("Drawing screen!")

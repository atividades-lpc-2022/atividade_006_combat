import pygame
from config import Config

from modules.Dimension import Dimension


class Screen:
    def __init__(self, dimension: Dimension):
        self.surface = pygame.display.set_mode((dimension.width, dimension.height))
        self.dimension = dimension

    def draw(self):  # TODO: Draw screen
        self.surface.fill((Config.COLORS["BLACK"]))

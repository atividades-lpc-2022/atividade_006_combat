import pygame
from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.Screen import Screen


class Brick:
    def __init__(self, coordinate: Coordinate, dimension: Dimension, color: tuple):
        self.coordinate = coordinate
        self.dimension = dimension
        self.image = pygame.Surface((self.dimension.width, self.dimension.height))
        self.rect = self.image.get_rect()
        self.image.fill(color)

    def draw(self, screen: Screen):
        self.rect.center = (self.coordinate.x, self.coordinate.y)
        screen.surface.blit(self.image, self.rect)

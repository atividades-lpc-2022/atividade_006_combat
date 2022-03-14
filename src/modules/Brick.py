import pygame
from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.Screen import Screen


class Brick:
    def __init__(self, coordinate: Coordinate, dimension: Dimension, color: tuple):
        self.coordinate = coordinate
        self.dimension = dimension
        self.color = color
        self.rect = None

    def draw(self, screen: Screen):
        self.rect = pygame.draw.rect(screen.surface, self.color, (self.coordinate.x, self.coordinate.y, self.dimension.width, self.dimension.height))

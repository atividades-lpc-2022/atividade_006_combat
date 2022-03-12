import pygame
from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.Screen import Screen


class Brick:
    def __init__(self, coordinate: Coordinate, dimension: Dimension):
        self.coordinate = coordinate
        self.rect = pygame.Rect(
            coordinate.x, coordinate.y, dimension.width, dimension.height
        )

    def draw(self, screen: Screen):
        pygame.draw.rect(screen.surface, (0, 0, 0), self.rect)

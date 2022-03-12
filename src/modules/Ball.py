import pygame
from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.Screen import Screen


class Ball:
    def __init__(self, coordinate: Coordinate, color: tuple):
        self.coordinate = coordinate
        self.image = pygame.Surface((5, 5))
        self.rect = self.image.get_rect()
        self.image.fill(color)
        self.hits = 0  # number of hits on the wall
        self.velocity = 1.0  # ball velocity

    def fires_at(
        self, screen: Screen
    ):  # TODO: Fires at a coordinate
        self.rect.center = (self.coordinate.x, self.coordinate.y)
        screen.surface.blit(self.image, self.rect)

            

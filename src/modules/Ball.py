import pygame
from modules.Brick import Brick
from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.Screen import Screen


class Ball:
    def __init__(self, coordinate: Coordinate, color: tuple):
        self.coordinate = coordinate
        self.image = pygame.Surface((5, 5))
        self.rect = self.image.get_rect()
        self.dimension = Dimension(self.rect.width, self.rect.height)
        self.image.fill(color)
        self.hits = 0  # number of hits on the wall
        self.x_velocity = 1.0  # ball velocity
        self.y_velocity = 1.0  # ball velocity

    def change_direction(self, brick: Brick): # TODO: Add ball collision with the bricks to undo this comment
        if self.coordinate.x == brick.coordinate.x:
            percents = (self.coordinate.y - brick.coordinate.y)/ brick.dimension.height

            if percents > 0.5:
                self.x_velocity *= -1
                self.y_velocity = 1
            elif percents < 0.5:
                self.x_velocity *= -1
                self.y_velocity = -1

        elif self.coordinate.y == brick.coordinate.y:
            percents = (self.coordinate.x - brick.coordinate.x)/ brick.dimension.width

            if percents > 0.5:
                self.x_velocity = -1
                self.y_velocity *= -1
            elif percents < 0.5:
                self.x_velocity = 1
                self.y_velocity *= -1


    def fires_at(
        self, screen: Screen
    ):  # TODO: Fires at a coordinate
        self.rect.center = (self.coordinate.x, self.coordinate.y)
        screen.surface.blit(self.image, self.rect)

            

import pygame
from modules.Coordinate import Coordinate
from modules.Screen import Screen


class Brick:
    def __init__(self, coordinate: Coordinate, sprite: pygame.sprite.Sprite):
        self.coordinate = coordinate
        self.sprite = sprite

    def draw(self, screen: Screen):  # TODO: Draw brick on screen
        print("Drawing Brick!")

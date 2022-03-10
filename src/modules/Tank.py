import pygame
from modules.Coordinate import Coordinate
from modules.Screen import Screen


class Tank:
    def __init__(self, coordinate: Coordinate, sprite: pygame.sprite.Sprite):
        self.coordinate = coordinate
        self.sprite = sprite
        self.velocity = 1.0  # Default tank velocity
        self.angle = 0  # Default tank angle

    def rotate(self, new_angle: float):  # Set a new angle
        self.angle = new_angle

    def use_controls():  # TODO: Define tank controls
        print("Setting tank controls...")

    def draw(self, screen: Screen):  # TODO: Draw a tank
        self.use_controls()
        print("Drawing a tank!")

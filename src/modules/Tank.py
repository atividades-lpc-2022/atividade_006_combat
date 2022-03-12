import pygame
from modules.Coordinate import Coordinate
from modules.Screen import Screen


class Tank(pygame.sprite.Sprite):

    def __init__(self, coordinate: Coordinate, sprite_path: str):

        super(Tank, self).__init__()
        self.image = pygame.image.load(sprite_path)
        self.rect = self.image.get_rect()
        self.coordinate = coordinate

        self.velocity = 1.0  # Default tank velocity
        self.angle = 0  # Default tank angle

    def rotate(self, new_angle: float):  # Set a new angle
        self.angle = new_angle

    def use_controls(self):  # TODO: Define tank controls
        print("Setting tank controls...")

    def draw(self, screen: Screen):  # TODO: Draw a tank
        self.rect.center = (self.coordinate.x, self.coordinate.y)
        self.use_controls()
        screen.surface.blit(self.image, self.rect)

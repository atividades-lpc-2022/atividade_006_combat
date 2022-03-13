from random import randint
from secrets import choice
from typing import Sequence
import pygame
from config import Config
from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.Screen import Screen

BRICK_POSITIONS = [
    [400, 180, 35, 80],
    [400, 475, 35, 80],
    [230, 325, 80, 30],
    [570, 325, 80, 30],
    [120, 325, 7, 110],
    [103, 278, 17, 17],
    [103, 371, 17, 17],
    [680, 325, 7, 110],
    [697, 278, 17, 17],
    [697, 371, 17, 17]   
]

class Tank(pygame.sprite.Sprite):
    def __init__(self, coordinate: Coordinate, sprite_path: str):

        super(Tank, self).__init__()
        self.image = pygame.image.load(sprite_path)
        self.rect = self.image.get_rect()
        self.coordinate = coordinate
        self.dimension = Dimension(self.rect.width, self.rect.height)
        self.range_allowed_x = list(range(21, Config.SCREEN_WIDTH - self.dimension.width + 1))
        self.range_allowed_y = list(range(76, Config.SCREEN_HEIGHT - self.dimension.height + 1))
        self.velocity = 1.0  # Default tank velocity
        self.angle = 0  # Default tank angle

    def rotate(self, new_angle: float):  # Set a new angle 
        self.image = pygame.transform.rotate(self.image, new_angle)
        rot_rect = self.image.get_rect(center=(self.rect.center))
        
    def change_position(self): # TODO: Add tank collision with the ball to undo this comment
        new_x = choice(self.range_allowed_x)
        new_y = choice(self.range_allowed_y)

        for brick_position in BRICK_POSITIONS:
            brick_x, brick_y, brick_width, brick_height = brick_position
            surface_colliding = (brick_x - self.dimension.width <= new_x <= brick_x + brick_width) and (brick_y - self.dimension.height <= new_y <= brick_y + brick_height)
            if surface_colliding: return self.change_position()

        self.coordinate.x = new_x
        self.coordinate.y = new_y

    def use_controls(self):  # TODO: Define tank controls
        print("Setting tank controls...")

    def draw(self, screen: Screen):  # TODO: Draw a tank
        self.rect.center = (self.coordinate.x, self.coordinate.y)
        self.use_controls()
        screen.surface.blit(self.image, self.rect)

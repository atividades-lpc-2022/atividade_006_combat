import pygame
from config import Config
from modules.Brick import Brick
from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.Screen import Screen


class Ball:
    def __init__(self, coordinate: Coordinate, dimension: Dimension, angle: float, player: int):
        self.coordinate = coordinate
        self.dimension = dimension
        self.hits = 0  # number of hits on the wall
        self.player = player # Who fire the ball
        self.angle = angle
        self.x_velocity = 1.0  # ball velocity
        self.y_velocity = 1.0  # ball velocity
        self.init_velocity()


    def init_velocity(self):
        if self.angle == 0.0 or self.angle == 360:
            self.x_velocity = 0
            self.y_velocity = -1
        elif self.angle == 45:
            self.y_velocity = -1
            self.x_velocity = -1
        elif self.angle == 90:
            self.x_velocity = -1
            self.y_velocity = 0
        elif self.angle == 135:
            self.x_velocity = -1
            self.y_velocity = 1
        elif self.angle == 180:
            self.x_velocity = 0
            self.y_velocity = 1
        elif self.angle == 225:
            self.x_velocity = 1
            self.y_velocity = 1
        elif self.angle == 270:
            self.x_velocity = 1
            self.y_velocity = 0
        elif self.angle == 315:
            self.x_velocity = 1
            self.y_velocity = -1

    def change_direction(self, brick: Brick): # TODO: Add ball collision with the bricks to undo this comment
        if self.coordinate.x == brick.coordinate.x:
            percents = (self.coordinate.y - brick.coordinate.y)/ brick.dimension.height

            if percents > 0.5:
                self.x_velocity *= -1
                self.y_velocity = 1
            elif percents < 0.5:
                self.x_velocity *= -1
                self.y_velocity *= -1
            else:
                self.x_velocity = 0
                self.y_velocity *= -1

        elif self.coordinate.y == brick.coordinate.y:
            percents = (self.coordinate.x - brick.coordinate.x)/ brick.dimension.width

            if percents > 0.5:
                self.x_velocity *= -1
                self.y_velocity *= -1
            elif percents < 0.5:
                self.x_velocity = 1
                self.y_velocity *= -1
            else:
                self.x_velocity = 0
                self.y_velocity *= -1

    def is_colliding(self, coordinate: Coordinate, dimension: Dimension) -> bool:
        x_colision = coordinate.x <= self.coordinate.x <= coordinate.x + dimension.width
        y_colision = coordinate.y <= self.coordinate.y <= coordinate.y + dimension.height
        return x_colision and y_colision

    def draw(self, screen: Screen):  # TODO: Fires at a coordinate
        from pygame import mixer
        mixer.init()

        colision_1 = pygame.mixer.Sound("src/sounds/Ball_to_wall/ball_wall1.wav")
        colision_2 = pygame.mixer.Sound("src/sounds/Ball_to_wall/ball_wall2.wav")
        colision_3 = pygame.mixer.Sound("src/sounds/Ball_to_wall/ball_wall3.wav")
        colision_4 = pygame.mixer.Sound("src/sounds/Ball_to_wall/ball_wall4.wav")
        colision_5 = pygame.mixer.Sound("src/sounds/Ball_to_wall/ball_wall5.wav")

        self.coordinate.x += Config.BALL_DRAW_VELOCITY * self.x_velocity
        self.coordinate.y += Config.BALL_DRAW_VELOCITY * self.y_velocity
        pygame.draw.rect(screen.surface, Config.COLORS["BLACK"], (self.coordinate.x, self.coordinate.y, self.dimension.width, self.dimension.height))

        if self.coordinate.y >= 572:
            self.y_velocity *= -1
            self.hits += 1

            if self.hits == 1:
                colision_1.play()
            if self.hits == 2:
                colision_2.play()
            if self.hits == 3:
                colision_3.play()
            if self.hits == 4:
                colision_4.play()
            if self.hits == 5:
                colision_5.play()

        if self.coordinate.y <= 75:
            self.y_velocity *= -1
            self.hits += 1

            if self.hits == 1:
                colision_1.play()
            if self.hits == 2:
                colision_2.play()
            if self.hits == 3:
                colision_3.play()
            if self.hits == 4:
                colision_4.play()
            if self.hits == 5:
                colision_5.play()

        if self.coordinate.x <= 20:
            self.x_velocity *= -1
            self.hits += 1

            if self.hits == 1:
                colision_1.play()
            if self.hits == 2:
                colision_2.play()
            if self.hits == 3:
                colision_3.play()
            if self.hits == 4:
                colision_4.play()
            if self.hits == 5:
                colision_5.play()

        if self.coordinate.x >= 772:
            self.x_velocity *= -1
            self.hits += 1

            if self.hits == 1:
                colision_1.play()
            if self.hits == 2:
                colision_2.play()
            if self.hits == 3:
                colision_3.play()
            if self.hits == 4:
                colision_4.play()
            if self.hits == 5:
                colision_5.play()

        


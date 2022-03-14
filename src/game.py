from typing import Sequence
import pygame
from modules.Brick import Brick
from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.HUD import HUD
from modules.Score import Score
from modules.Tank import Tank
from modules.Screen import Screen
from modules.Boundaries import *
from modules.Ball import Ball
from config import Config


class Game:
    def __init__(self):
        self.is_running = True
        self.player_1_score = Score()
        self.player_2_score = Score()

    def stop(self):  # Stop game
        self.is_running = False

    def reset(self):  # Reset all status
        self.player_1_score.reset()
        self.player_2_score.reset()

    def use_global_events(self):  # TODO: Set global events (exit the game, ...)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def play(
        self,
    ):  # TODO: Implement game loop (draw all elements (Screen, HUD, Tanks, Bricks))

        # Initializze pygame inside game loop
        pygame.init()

        # Create screen
        screen = Screen(Dimension(Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
        pygame.display.set_caption("TANK PONG")
        clock = pygame.time.Clock()

        balls: Sequence[Ball] = []

        # Players
        tank_1 = Tank(
            Coordinate(70, 325), sprite_path=(Config.SPRITES_PATH["PLAYER_1"])
            )
        tank_2 = Tank(
            Coordinate(730, 325), sprite_path=(Config.SPRITES_PATH["PLAYER_2"])
        )

        # HUD
        hud = HUD()
        
        # Bricks
        brick_center_1 = Brick(Coordinate(400, 180), Dimension(35, 80), Config.COLORS["T_ORANGE"])
        brick_center_2 = Brick(Coordinate(400, 475), Dimension(35, 80), Config.COLORS["T_ORANGE"])
        brick_center_3 = Brick(Coordinate(230, 325), Dimension(80, 30), Config.COLORS["T_ORANGE"])
        brick_center_4 = Brick(Coordinate(570, 325), Dimension(80, 30), Config.COLORS["T_ORANGE"])

        brick_left_1 = Brick(Coordinate(120, 325), Dimension(17, 110), Config.COLORS["T_ORANGE"])
        brick_left_2 = Brick(Coordinate(103, 278), Dimension(17, 17), Config.COLORS["T_ORANGE"])
        brick_left_3 = Brick(Coordinate(103, 371), Dimension(17, 17), Config.COLORS["T_ORANGE"])

        brick_right_1 = Brick(Coordinate(680, 325), Dimension(17, 110), Config.COLORS["T_ORANGE"])
        brick_right_2 = Brick(Coordinate(697, 278), Dimension(17, 17), Config.COLORS["T_ORANGE"])
        brick_right_3 = Brick(Coordinate(697, 371), Dimension(17, 17), Config.COLORS["T_ORANGE"])

        while self.is_running:
            self.use_global_events()

            screen.draw()
            tank_1.draw(screen)
            tank_2.draw(screen)

            hud.draw(
                screen,
                self.player_1_score,
                self.player_2_score,
                Config.COLORS["RED"],
                Config.COLORS["BLUE"],
            )

            for ball in balls:
                if ball.hits == Config.MAX_BALL_HITS:
                    balls.remove(ball)
                ball.draw(screen)

            brick_center_1.draw(screen)
            brick_center_2.draw(screen)
            brick_center_3.draw(screen)
            brick_center_4.draw(screen)

            brick_left_1.draw(screen)
            brick_left_2.draw(screen)
            brick_left_3.draw(screen)

            brick_right_1.draw(screen)
            brick_right_2.draw(screen)
            brick_right_3.draw(screen)

            bound(screen.surface, color=(Config.COLORS["T_ORANGE"]))

            # Tank 1's movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                tank_1.move_up()
                if tank_1.coordinate.y >= 550:
                    tank_1.coordinate.y = 550 - 20
                if tank_1.coordinate.y <= 75:
                    tank_1.coordinate.y = 75 + 20

                if tank_1.coordinate.x <= 20:
                    tank_1.coordinate.x = 20 + 20
                if tank_1.coordinate.x >= 750:
                    tank_1.coordinate.x = 750 - 20

            if keys[pygame.K_a]:
                tank_1.rotate(45)
                pygame.time.delay(60)
            if keys[pygame.K_d]:
                tank_1.rotate(-45)
                pygame.time.delay(60)
            if keys[pygame.K_f]:
                ball = tank_1.fire(1)
                balls.append(ball)
                pygame.time.delay(30)


            # Tank 2's movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                tank_2.move_up()
                if tank_2.coordinate.y >= 550:
                    tank_2.coordinate.y = 550 - 20
                if tank_2.coordinate.y <= 75:
                    tank_2.coordinate.y = 75 + 20

                if tank_2.coordinate.x <= 20:
                    tank_2.coordinate.x = 20 + 20
                if tank_2.coordinate.x >= 750:
                    tank_2.coordinate.x = 750 - 20

            if keys[pygame.K_LEFT]:
                tank_2.rotate(45)
                pygame.time.delay(60)
            if keys[pygame.K_RIGHT]:
                tank_2.rotate(-45)
                pygame.time.delay(60)
            if keys[pygame.K_SPACE]:
                ball = tank_2.fire(2)
                balls.append(ball)
                pygame.time.delay(30)

            pygame.display.update()
            clock.tick(60)

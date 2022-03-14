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

        # Initialize mixer
        pygame.mixer.init()
        shot = pygame.mixer.Sound("src/sounds/shot.wav")

        # Create screen
        screen = Screen(Dimension(Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
        pygame.display.set_caption("TANK PONG")
        clock = pygame.time.Clock()

        balls: Sequence[Ball] = []

        # Players
        tank_1 = Tank(Coordinate(Config.SCREEN_WIDTH * (0.1), 320), Config.SPRITES_PATH["PLAYER_1"], 1)
        tank_2 = Tank(Coordinate(Config.SCREEN_WIDTH * (0.9), 320), Config.SPRITES_PATH["PLAYER_2"], 2)

        # HUD
        hud = HUD()
        
        # Bricks
        brick_center_1 = Brick(Coordinate(Config.SCREEN_WIDTH / 2 - 17.5, 180), Dimension(35, 80), Config.COLORS["T_ORANGE"])
        brick_center_2 = Brick(Coordinate(Config.SCREEN_WIDTH / 2 - 17.5, 425), Dimension(35, 80), Config.COLORS["T_ORANGE"])
        brick_center_3 = Brick(Coordinate(Config.SCREEN_WIDTH * (0.4) - 80, 325), Dimension(80, 30), Config.COLORS["T_ORANGE"])
        brick_center_4 = Brick(Coordinate(Config.SCREEN_WIDTH * (0.6), 325), Dimension(80, 30), Config.COLORS["T_ORANGE"])

        brick_left_1 = Brick(Coordinate(120, 270), Dimension(17, 110), Config.COLORS["T_ORANGE"])
        brick_left_2 = Brick(Coordinate(103, 253), Dimension(34, 17), Config.COLORS["T_ORANGE"])
        brick_left_3 = Brick(Coordinate(103, 380), Dimension(34, 17), Config.COLORS["T_ORANGE"])

        brick_right_1 = Brick(Coordinate(680, 270), Dimension(17, 110), Config.COLORS["T_ORANGE"])
        brick_right_2 = Brick(Coordinate(680, 253), Dimension(34, 17), Config.COLORS["T_ORANGE"])
        brick_right_3 = Brick(Coordinate(680, 380), Dimension(34, 17), Config.COLORS["T_ORANGE"])

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

                if ball.is_colliding(tank_2.coordinate, tank_2.dimension):
                    if ball.player == 1:
                        self.player_1_score.increment()
                        balls.remove(ball)
                        tank_2.change_position()

                if ball.is_colliding(tank_1.coordinate, tank_1.dimension):
                    if ball.player == 2:
                        self.player_2_score.increment()
                        balls.remove(ball)
                        tank_1.change_position()

                if (ball.is_colliding(brick_left_1.coordinate, brick_left_1.dimension) 
                    or ball.is_colliding(brick_left_2.coordinate, brick_left_2.dimension) 
                    or ball.is_colliding(brick_left_3.coordinate, brick_left_3.dimension)
                    or ball.is_colliding(brick_right_1.coordinate, brick_right_1.dimension)
                    or ball.is_colliding(brick_right_2.coordinate, brick_right_2.dimension)
                    or ball.is_colliding(brick_right_3.coordinate, brick_right_3.dimension)
                    or ball.is_colliding(brick_center_1.coordinate, brick_center_1.dimension)
                    or ball.is_colliding(brick_center_2.coordinate, brick_center_2.dimension)
                    or ball.is_colliding(brick_center_3.coordinate, brick_center_3.dimension)
                    or ball.is_colliding(brick_center_4.coordinate, brick_center_4.dimension)
                ):
                    ball.y_velocity = -1
                    ball.x_velocity = -1

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
                if (tank_1.is_colliding(brick_left_1.coordinate, brick_left_1.dimension) 
                    or tank_1.is_colliding(brick_left_2.coordinate, brick_left_2.dimension) 
                    or tank_1.is_colliding(brick_left_3.coordinate, brick_left_3.dimension)
                    or tank_1.is_colliding(brick_right_1.coordinate, brick_right_1.dimension)
                    or tank_1.is_colliding(brick_right_2.coordinate, brick_right_2.dimension)
                    or tank_1.is_colliding(brick_right_3.coordinate, brick_right_3.dimension)
                    or tank_1.is_colliding(brick_center_1.coordinate, brick_center_1.dimension)
                    or tank_1.is_colliding(brick_center_2.coordinate, brick_center_2.dimension)
                    or tank_1.is_colliding(brick_center_3.coordinate, brick_center_3.dimension)
                    or tank_1.is_colliding(brick_center_4.coordinate, brick_center_4.dimension)
                ):
                    tank_1.coordinate.x -= 1.1
                    tank_1.coordinate.y -= 1.1
                else:
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
                has_ball = False
                for ball in balls:
                    if ball.player == 1:
                        has_ball = True
                if not has_ball:
                    new_ball = tank_1.fire()
                    balls.append(new_ball)
                    shot.play()


            # Tank 2's movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                if (tank_2.is_colliding(brick_left_1.coordinate, brick_left_1.dimension) 
                    or tank_2.is_colliding(brick_left_2.coordinate, brick_left_2.dimension) 
                    or tank_2.is_colliding(brick_left_3.coordinate, brick_left_3.dimension)
                    or tank_2.is_colliding(brick_right_1.coordinate, brick_right_1.dimension)
                    or tank_2.is_colliding(brick_right_2.coordinate, brick_right_2.dimension)
                    or tank_2.is_colliding(brick_right_3.coordinate, brick_right_3.dimension)
                    or tank_2.is_colliding(brick_center_1.coordinate, brick_center_1.dimension)
                    or tank_2.is_colliding(brick_center_2.coordinate, brick_center_2.dimension)
                    or tank_2.is_colliding(brick_center_3.coordinate, brick_center_3.dimension)
                    or tank_2.is_colliding(brick_center_4.coordinate, brick_center_4.dimension)
                ):
                    tank_2.coordinate.x += 1.1
                    tank_2.coordinate.y -= 1.1
                else:
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
                has_ball = False
                for ball in balls:
                    if ball.player == 2:
                        has_ball = True
                if not has_ball:
                    new_ball = tank_2.fire()
                    balls.append(new_ball)
                    shot.play()

            pygame.display.update()
            clock.tick(60)

import pygame
from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.HUD import HUD
from modules.Score import Score
from modules.Tank import Tank
from modules.Screen import Screen
from modules.Boundaries import *
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

        # Players
        tank_1 = Tank(
            Coordinate(100, 300), sprite_path=(Config.SPRITES_PATH["PLAYER_1"])
        )
        tank_2 = Tank(
            Coordinate(700, 300), sprite_path=(Config.SPRITES_PATH["PLAYER_2"])
        )

        # HUD
        hud = HUD()

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
            bound(screen.surface, color=(Config.COLORS["T_ORANGE"]))

            pygame.display.update()
            clock.tick(60)

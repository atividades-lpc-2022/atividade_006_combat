import pygame
from config import Config
from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.Score import Score
from modules.Screen import Screen
from modules.Tank import Tank


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
        print("Setting global events")

    def play(
        self,
    ):  # TODO: Implement game loop (draw all elements (Screen, HUD, Tanks, Bricks))
        pygame.init()
        
        clock = pygame.time.Clock()
        screen = Screen(Dimension(Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
        
        while self.is_running: # Game loop
            
            screen.draw()

            pygame.display.update()
            clock.tick(60)
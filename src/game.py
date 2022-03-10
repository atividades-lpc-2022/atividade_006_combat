from modules.Coordinate import Coordinate
from modules.Score import Score
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
        while self.is_running:
            print("Game is running!")
        print("Game is not running!")

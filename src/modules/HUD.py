from modules.Score import Score
from modules.Screen import Screen


class HUD:
    def draw(
        self, screen: Screen, player_1_score: Score, player_2_score: Score
    ):  # TODO: Draw HUD (players score)
        print("Drawing HUD")

import pygame
from config import Config
from modules.Coordinate import Coordinate
from modules.Score import Score
from modules.Screen import Screen


class HUD:
    def draw_label(
        self, screen: Screen, label: str, coordinate: Coordinate, color: tuple
    ):
        font = pygame.font.Font(Config.FONT_PATH, Config.FONT_SIZE)
        text = font.render(label, True, color)
        text_rect = text.get_rect()
        text_rect.center = (coordinate.x, coordinate.y)
        screen.surface.blit(text, text_rect)

    def draw(
        self,
        screen: Screen,
        player_1_score: Score,
        player_2_score: Score,
        player_1_color: tuple,
        player_2_color: tuple,
    ):  # TODO: Draw HUD (players score)
        x_player_1_score = screen.dimension.width * (0.25)
        x_player_2_score = screen.dimension.width * (0.75)
        y_players_score = screen.dimension.height * (0.05)

        self.draw_label(
            screen,
            str(player_1_score.points),
            Coordinate(x_player_1_score, y_players_score),
            player_1_color,
        )
        self.draw_label(
            screen,
            str(player_2_score.points),
            Coordinate(x_player_2_score, y_players_score),
            player_2_color,
        )

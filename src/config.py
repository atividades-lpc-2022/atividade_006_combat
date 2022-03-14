from pygame import Color


class Config:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    CURRENT_LEVEL = 1
    MAX_PLAYER_POINTS = 4
    MAX_BALL_HITS = 5
    BALL_DRAW_VELOCITY = 8
    FONT_SIZE = 32
    FONT_PATH = "src/fonts/PressStart2P.ttf"

    SPRITES_PATH = {
        # Put all paths of sprites here. Default path `src/sprites/<SPRITE_NAME>.png`
        "SPRITE_NAME": "src/sprites/example.png",
        "PLAYER_1": "src/sprites/player_1.png",
        "PLAYER_2": "src/sprites/player_2.png",
    }

    SOUNDS_PATH = {
        # Put all paths of sounds here. Default path `src/sounds/<SOUND_NAME>.wav`
        "SOUND_NAME": "src/sounds/example.wav"
    }

    COLORS = {
        "BLACK": Color(0, 0, 0),
        "WHITE": Color(255, 255, 255),
        "RED": Color(255, 0, 0),
        "BLUE": Color(0, 0, 255),
        "T_ORANGE": Color(239, 154, 81),
        "T_GREEN": Color(140, 150, 64),
    }

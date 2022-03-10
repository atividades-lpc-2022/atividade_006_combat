from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.Screen import Screen


class Ball:
    def __init__(self, coordinate: Coordinate, dimension: Dimension):
        self.coordinate = coordinate
        self.dimension = dimension
        self.hits = 0  # number of hits on the wall
        self.velocity = 1.0  # ball velocity

    def fires_at(
        self, coordinate: Coordinate, screen: Screen
    ):  # TODO: Fires at a coordinate
        print("Fire!")

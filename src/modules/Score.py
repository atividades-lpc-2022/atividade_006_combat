class Score:
    def __init__(self):
        self.points = 0

    def increment(self, points=1):
        self.points += points

    def reset(self):
        self.points = 0

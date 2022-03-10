class Score:
    def __init__(self):
        self.points = 0

    def increment(self):
        self.points += 1

    def reset(self):
        self.points = 0


class Player:
    def __init__(self, name):
        self.name = name
        self.total_points = 0
        self.round_points = 0

    def add_round_points(self, points):
        self.round_points += points

    def current_points(self, points):
        self.total_points += points
        return self.total_points

    def current_points_adjust(self):
        self.total_points -= self.round_points
        return self.total_points

    def reset_round_points(self):
        self.round_points = 0

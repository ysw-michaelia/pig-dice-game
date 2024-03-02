import random


class Dice:
    def __init__(self, probability=None):
        self.probability = probability

    def computer_roll(self):
        return random.choice(self.probability)

    def player_roll(self):
        return random.randint(1, 6)

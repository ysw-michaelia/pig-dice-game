import random


class Dice:
    def __init__(self, probability=None):
        self.probability = probability

    def roll(self):
        if self.probability:
            return random.choice(self.probability)
        else:
            return random.randint(1, 6)

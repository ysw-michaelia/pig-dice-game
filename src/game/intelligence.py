from random import random


class Intelligence:
    def __init__(self, probability, strategy):
        self.probability = probability
        self.strategy = strategy

    def dice_probability(self):
        if self.probability == 1:
            return [1, 2, 3, 4, 5, 6]
        elif self.probability == 2:
            return [1, 1, 2, 3, 4, 5, 6, 6]
        elif self.probability == 3:
            return [1, 1, 2, 2, 3, 4, 5, 5, 6, 6]
        elif self.probability == 4:
            return [1, 1, 1, 2, 2, 3, 4, 5, 6, 6, 6]
        elif self.probability == 5:
            return [1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 6]

    def choose_action(self):
        if self.strategy == 1:
            return "roll" if random() > self.probability / 6 else "hold"
        elif self.strategy == 2:
            return "roll" if random() > self.probability / 6 else "hold"
        elif self.strategy == 3:
            return "roll" if random() > self.probability / 6 else "hold"
        elif self.strategy == 4:
            return "roll" if random() > self.probability / 6 else "hold"
        elif self.strategy == 5:
            return "roll" if random() > self.probability / 6 else "hold"

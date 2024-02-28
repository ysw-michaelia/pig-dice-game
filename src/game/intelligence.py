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

    def choose_action(self, computer_round_points):
        if self.strategy == 1:
            if computer_round_points < 3:
                return "roll"
            elif random() > self.probability / 6:
                return "roll"
            else:
                return "hold"
        elif self.strategy == 2:
            if computer_round_points < 5:
                return "roll"
            elif computer_round_points > 10:
                return "hold"
            elif random() > self.probability / 6:
                return "roll"
            else:
                return "hold"
        elif self.strategy == 3:
            if computer_round_points < 7:
                return "roll"
            elif computer_round_points > 12:
                return "hold"
            elif random() > self.probability / 6:
                return "roll"
            else:
                return "hold"
        elif self.strategy == 4:
            if computer_round_points < 9:
                return "roll"
            elif computer_round_points > 14:
                return "hold"
            elif random() > self.probability / 6:
                return "roll"
            else:
                return "hold"
        elif self.strategy == 5:
            if computer_round_points < 11:
                return "roll"
            elif computer_round_points > 16:
                return "hold"
            elif random() > self.probability / 6:
                return "roll"
            else:
                return "hold"

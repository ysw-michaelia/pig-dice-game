"""
This module contains the Intelligence class.

It represents the intelligence or decision-making logic for
computer-controlled players in a game.
"""

import random


class Intelligence:
    """
    Represents the decision-making logic for computer-controlled players.

    Attributes:
        probability (int): The level of probability of dice only for computer.
        strategy (int): The strategy level used for computer's decision-making.
    """

    def __init__(self, probability, strategy):
        """
        Initialize the Intelligence object.

        Args:
            probability (int): The level of probability of dice rolls for
            the computer.
            strategy (int): The strategy level used for computer's
            decision-making.
        """
        self.probability = probability
        self.strategy = strategy

    def dice_probability(self):
        """
        Determine the probability distribution of dice rolls.

        The higher the probability level, the harder it is for the player to
        beat the computer.

        Returns:
            list: A list representing the possible outcomes of dice rolls.
        """
        if self.probability == 1:
            return [1, 2, 3, 4, 5, 6]
        if self.probability == 2:
            return [1, 1, 2, 3, 4, 5, 6, 6]
        if self.probability == 3:
            return [1, 1, 2, 2, 3, 4, 5, 5, 6, 6]
        if self.probability == 4:
            return [1, 1, 1, 2, 2, 3, 4, 5, 6, 6, 6]
        if self.probability == 5:
            return [1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 6]
        return []

    def choose_action(self, computer_round_points):
        """
        Determine the action (roll or hold) to be taken by the computer.

        Args:
            computer_round_points (int): The current points accumulated by the
            computer player in the round. Used as a key element to decide what
            to do next for the computer.

        Returns:
            str: The action to be taken by computer(either 'roll' or 'hold').
        """
        strategy_thresholds = {1: 3, 2: 5, 3: 7, 4: 9, 5: 11}

        threshold = strategy_thresholds.get(self.strategy)

        if computer_round_points < threshold:
            return "roll"
        if computer_round_points > threshold + 5:
            return "hold"
        if random.random() > self.probability / 6:
            return "roll"
        return "hold"

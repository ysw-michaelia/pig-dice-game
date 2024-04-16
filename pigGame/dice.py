"""This module provides a Dice class for simulating dice rolls in a game."""
import random


class Dice:
    """
    Represents a dice object with methods for rolling.

    Attributes:
        probability (list or None): A list representing the possible outcomes
            of the dice roll. Only PvC needs it since it is part of computer
            intelligence settings, it contains the weighted probabilities of
            each outcome.
    """

    def __init__(self, probability=None):
        self.probability = probability

    def computer_roll(self):
        """
        Simulates a computer dice roll based on the provided probability.

        Returns:
            int: The outcome of the dice roll based on the provided
                probability distribution.
        """
        return random.choice(self.probability)

    def player_roll(self):
        """
        Simulates a player dice roll with fair probabilities.

        Returns:
            int: The outcome of the dice roll with fair probabilities.
        """
        return random.randint(1, 6)

"""This module provides a Dice class for simulating dice rolls in a game."""

import random


class Dice:
    """
    Represent a dice object with methods for rolling.

    Attributes:
        probability (list or None): A list representing the possible outcomes
            of the dice roll. Only PvC needs it since it is part of computer
            intelligence settings, it contains the weighted probabilities of
            each outcome.
    """

    def __init__(self, probability=None):
        """
        Initialize a Dice object with optional weighted probabilities.

        Args:
            probability (list or None, optional): A list representing the
                possible outcomes of the dice roll. This parameter is used
                only for PvC (Player vs Computer) games where weighted
                probabilities are part of computer intelligence settings.
                Each element in the list represents the weighted probability
                of a specific outcome. Defaults to None, indicating that fair
                probabilities are used for the dice roll.

        Attributes:
            probability (list or None): A list representing the possible
                outcomes of the dice roll. If provided, it contains the
                weighted probabilities of each outcome.

        Example:
            # Initialize a Dice object with fair probabilities
            dice = Dice()

            # Initialize a Dice object with custom probabilities
            custom_probabilities = [0.1, 0.2, 0.3, 0.2, 0.1, 0.1]
            dice = Dice(probability=custom_probabilities)
        """
        self.probability = probability

    def computer_roll(self):
        """
        Simulate a computer dice roll based on the provided probability.

        Returns:
            int: The outcome of the dice roll based on the provided
                probability distribution.
        """
        return random.choice(self.probability)

    def player_roll(self):
        """
        Simulate a player dice roll with fair probabilities.

        Returns:
            int: The outcome of the dice roll with fair probabilities.
        """
        return random.randint(1, 6)

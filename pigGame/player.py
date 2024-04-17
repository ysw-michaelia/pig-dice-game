"""This module contains the Player class representing a player in a game."""


class Player:
    """
    Represents a player in a game.

    Attributes:
        name (str): The name of the player.
        total_points (int): The total points accumulated by the player.
        round_points (int): The points accumulated in the current round.
    """

    def __init__(self, name):
        """
        Initialize a Player object with the given name.

        It sets initial total points and round points to zero.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.total_points = 0
        self.round_points = 0

    def add_round_points(self, points):
        """
        Add points to the player's round score and returns the updated one.

        Args:
            points (int): The points to be added to the player's round score.

        Returns:
            int: The updated round score of the player.
        """
        self.round_points += points
        return self.round_points

    def current_points(self, points):
        """
        Add points to the player's total score and returns the updated one.

        Args:
            points (int): The points to be added to the player's total score.

        Returns:
            int: The updated total score of the player.
        """
        self.total_points += points
        return self.total_points

    def current_points_adjust(self):
        """
        Adjust the player's total score.

        It subtracts the round score when player got 1 in the game.

        Returns:
            int: The updated total score of the player after adjustment.
        """
        self.total_points -= self.round_points
        return self.total_points

    def reset_round_points(self):
        """Reset the player's round score to zero."""
        self.round_points = 0

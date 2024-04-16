import unittest
from pigGame.dice import Dice


class TestDice(unittest.TestCase):
    """Test cases for the Dice class."""

    def test_init_with_probability(self):
        """Test initialization with provided probability."""
        probabilities = [1, 2, 3, 4, 5, 6]
        dice = Dice(probability=probabilities)
        self.assertEqual(dice.probability, probabilities)

    def test_init_without_probability(self):
        """Test initialization without provided probability."""
        dice = Dice()
        self.assertIsNone(dice.probability)

    def test_player_roll(self):
        """Test player_roll method."""
        dice = Dice()
        result = dice.player_roll()
        self.assertTrue(1 <= result <= 6)
        # Ensure the result is within the range [1, 6]

    def test_computer_roll(self):
        """Test computer_roll method."""
        probabilities = [1, 2, 3, 4, 5, 6]
        dice = Dice(probability=probabilities)
        result = dice.computer_roll()
        self.assertIn(result, probabilities)
        # Ensure the result is one of the provided probabilities


if __name__ == '__main__':
    unittest.main()

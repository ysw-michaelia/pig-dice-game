import unittest
from dice import Dice


class TestDice(unittest.TestCase):

    def test_init_with_probability(self):
        probabilities = [1, 2, 3, 4, 5, 6]
        dice = Dice(probability=probabilities)
        self.assertEqual(dice.probability, probabilities)

    def test_init_without_probability(self):
        dice = Dice()
        self.assertIsNone(dice.probability)

    def test_player_roll(self):
        dice = Dice()
        result = dice.player_roll()
        self.assertTrue(1 <= result <= 6)  
        # Ensure the result is within the range [1, 6]


if __name__ == '__main__':
    unittest.main()

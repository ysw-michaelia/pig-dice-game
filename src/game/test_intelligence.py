"""unite test for intelligence"""
import unittest
from unittest.mock import patch
from intelligence import Intelligence


class TestIntelligence(unittest.TestCase):
    """Test Intelligence"""

    def test_dice_probability_probability_1(self):
        intelligence = Intelligence(probability=1, strategy=1)
        self.assertEqual(intelligence.dice_probability(), [1, 2, 3, 4, 5, 6])

    def test_dice_probability_probability_2(self):
        intelligence = Intelligence(probability=2, strategy=1)
        self.assertEqual(intelligence.dice_probability(), [1, 1, 2, 3, 4,
                                                           5, 6, 6])

    def test_dice_probability_probability_3(self):
        intelligence = Intelligence(probability=3, strategy=1)
        self.assertEqual(intelligence.dice_probability(), [1, 1, 2, 2, 3, 4,
                                                           5, 5, 6, 6])

    def test_dice_probability_probability_4(self):
        intelligence = Intelligence(probability=4, strategy=1)
        self.assertEqual(intelligence.dice_probability(), [1, 1, 1, 2, 2, 3,
                                                           4, 5, 6, 6, 6])

    def test_dice_probability_probability_5(self):
        intelligence = Intelligence(probability=5, strategy=1)
        self.assertEqual(intelligence.dice_probability(), [1, 1, 1, 2, 2, 3,
                                                           3, 4, 5, 5, 6, 6,
                                                           6])

    def test_dice_probability_probability_other(self):
        intelligence = Intelligence(probability=6, strategy=1)
        self.assertEqual(intelligence.dice_probability(), [])

    def test_choose_action_roll(self):
        intelligence = Intelligence(probability=1, strategy=1)
        self.assertEqual(intelligence.choose_action(2), "roll")

    def test_choose_action_hold(self):
        intelligence = Intelligence(probability=1, strategy=1)
        self.assertEqual(intelligence.choose_action(10), "hold")

    @patch('random.random', return_value=0.9)
    def test_choose_action_roll_random(self, mock_random):
        intelligence = Intelligence(probability=2, strategy=1)
        self.assertEqual(intelligence.choose_action(7), "roll")

    def test_choose_action_hold_random(self):
        with patch('random.random', return_value=0.1):
            intelligence = Intelligence(probability=2, strategy=1)
            self.assertEqual(intelligence.choose_action(7), "hold")


if __name__ == "__main__":
    unittest.main()

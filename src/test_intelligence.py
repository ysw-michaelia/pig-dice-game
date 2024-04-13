"""unite test for intelligence"""
import unittest
from unittest.mock import patch
from intelligence import Intelligence

class TestIntelligence(unittest.TestCase):
    """TestIntelligence"""

    def test_dice_probability(self):
        """test_dice_probability"""
        intelligence = Intelligence(3, 2)
        expected_outcomes = [1, 1, 2, 2, 3, 4, 5, 5, 6, 6]
        self.assertEqual(intelligence.dice_probability(), expected_outcomes)

@patch('intelligence.random')
def test_choose_action(self, mock_random):
    """test_choose_action"""
    intelligence = Intelligence(3, 2)

    # Set up mock return values for different scenarios
    mock_random.side_effect = [0.5, 0.2]  # Adjusted mock return values

    # Test scenarios
    self.assertEqual(intelligence.choose_action(6), "roll")  # Should roll

if __name__ == "__main__":
    unittest.main()

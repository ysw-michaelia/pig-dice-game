import unittest
from player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Test Player")

    def test_add_round_points(self):
        self.assertEqual(self.player.add_round_points(10), 10)
        self.assertEqual(self.player.add_round_points(5), 15)

    def test_current_points(self):
        self.assertEqual(self.player.current_points(20), 20)
        self.assertEqual(self.player.current_points(15), 35)

    def test_current_points_adjust(self):
        self.player.add_round_points(10)
        self.player.current_points(20)
        self.assertEqual(self.player.current_points_adjust(), 10)

    def test_reset_round_points(self):
        self.player.add_round_points(10)
        self.player.reset_round_points()
        self.assertEqual(self.player.round_points, 0)


if __name__ == '__main__':
    unittest.main()
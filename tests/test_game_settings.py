"""unit testing for game_settings.py"""

from unittest.mock import patch, call
import unittest
from pigGame.game_settings import GameSettings
from pigGame.score import Score


class testGameSettings(unittest.TestCase):
    """test the class"""

    def setUp(self):
        self.score = Score()
        self.game_setting = GameSettings(self.score)

    def tearDown(self):
        pass

    @patch('pigGame.game.Game.start_game')
    @patch('pigGame.game_settings.GameSettings.get_player_name')
    @patch('pigGame.game_settings.GameSettings.get_difficulty')
    @patch('builtins.input', side_effect=['2', '3', 'Player1'])
    def test_against_computer(self, mock_input, mock_get_diff,
                              mock_get_player_name, mock_start_game):
        self.game_setting.against_computer()

        mock_get_diff.assert_has_calls([call(1), call(2)])
        mock_get_player_name.assert_called_with(1)
        mock_start_game.assert_called_once()

    @patch('pigGame.game.Game.start_game')
    @patch('pigGame.game_settings.GameSettings.get_player_name',
           side_effect=['Player1', 'Player2'])
    def test_against_player(self, mock_get_player_name,
                            mock_start_game):
        self.game_setting.against_player()

        mock_get_player_name.assert_has_calls([call("Player 1"),
                                               call("Player 2")])
        mock_start_game.assert_called_once()

    @patch('builtins.input', side_effect=['randomStuff', '3'])
    def test_get_difficulty_probability_3(self, mock_input):
        difficulty = self.game_setting.get_difficulty(1)
        self.assertEqual(difficulty, '3')

    @patch('builtins.input', side_effect=['randomStuff', '5'])
    def test_get_difficulty_strategy_5(self, mock_input):
        difficulty = self.game_setting.get_difficulty(2)
        self.assertEqual(difficulty, '5')

    @patch('builtins.input', side_effect=['randomStuff', '5'])
    def test_get_difficulty_probability_5(self, mock_input):
        difficulty = self.game_setting.get_difficulty(1)
        self.assertEqual(difficulty, '5')

    @patch('builtins.input', side_effect=['randomStuff', '3'])
    def test_get_difficulty_strategy_3(self, mock_input):
        difficulty = self.game_setting.get_difficulty(2)
        self.assertEqual(difficulty, '3')

    @patch('builtins.input', side_effect=['computer', 'testPlayer',
                                          'Player1'])
    def test_get_player_name_pvc(self, mock_input):
        player = self.game_setting.get_player_name(1)
        self.assertEqual(player.name, 'Player1')

    @patch('builtins.input', side_effect=['testPlayer', 'Player2'])
    def test_get_player_name_pvp(self, mock_input):
        player = self.game_setting.get_player_name('Player 2')
        self.assertEqual(player.name, 'Player2')


if __name__ == "__main__":
    unittest.main()

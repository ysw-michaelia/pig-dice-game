"""unit testing for game_settings.py"""

from unittest.mock import patch, call
import unittest
from game_settings import GameSettings
from score import Score


class testGameSettings(unittest.TestCase):
    """test the class"""

    @patch('game.Game.start_game')
    @patch('game_settings.GameSettings.get_player_name')
    @patch('game_settings.GameSettings.get_difficulty')
    @patch('builtins.input', side_effect=['2', '3', 'Player1'])
    def test_against_computer(self, mock_input, mock_get_diff,
                              mock_get_player_name, mock_start_game):
        score = Score()
        game_setting = GameSettings(score)
        game_setting.against_computer()

        mock_get_diff.assert_has_calls([call(1), call(2)])
        mock_get_player_name.assert_called_with(1)
        mock_start_game.assert_called_once()

    @patch('game.Game.start_game')
    @patch('game_settings.GameSettings.get_player_name',
           side_effect=['Player1', 'Player2'])
    # @patch('dice.Dice')
    def test_against_player(self, mock_get_player_name,
                            mock_start_game):
        score = Score()
        game_settings = GameSettings(score)
        game_settings.against_player()

        mock_get_player_name.assert_has_calls([call("Player 1"), call("Player 2")])
        # mock_dice.assert_called()
        # mock_dice.assert_called_once_with(probability=None)
        # self.assertTrue(mock.called)
        mock_start_game.assert_called_once()

    @patch('builtins.input', side_effect=['3'])
    def test_get_difficulty_probability(self, mock_input):
        score = Score()
        game_setting = GameSettings(score)
        difficulty = game_setting.get_difficulty(1)
        self.assertEqual(difficulty, '3')
        mock_input.assert_called_once_with()

    @patch('builtins.input', side_effect=['5'])
    def test_get_difficulty_strategy(self, mock_input):
        game_settings = GameSettings(None)
        difficulty = game_settings.get_difficulty(2)
        self.assertEqual(difficulty, '5')
        mock_input.assert_called_once_with()

    @patch('builtins.input', side_effect=['computer', 'Player1'])
    def test_get_player_name_pvc(self, mock_input):
        score = Score()
        game_setting = GameSettings(score)
        player = game_setting.get_player_name(1)
        self.assertEqual(player.name, 'Player1')

    @patch('builtins.input', side_effect=['Player2'])
    def test_get_player_name_pvp(self, mock_input):
        score = Score()
        game_setting = GameSettings(score)
        player = game_setting.get_player_name('Player 2')
        self.assertEqual(player.name, 'Player2')


if __name__ == "__main__":
    unittest.main()

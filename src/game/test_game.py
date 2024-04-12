"""unit testing for game.py"""

from unittest.mock import patch, MagicMock
import unittest
import sys
import io
from intelligence import Intelligence
from player import Player
from game import Game


class testGame(unittest.TestCase):
    """test the class"""

    @patch('game.Game.start_round')
    @patch('builtins.input', side_effect=['q', 'q'])
    def test_start_game(self, mock_input, mock_start_round):
        player1 = Player("Player1")
        player2 = Player("Computer")
        players = [player1, player2]
        game = Game(players, None, None, "")
        game.start_game()

        mock_start_round.assert_called_once()

    @patch('game.Game.computer_round')
    @patch('game.Game.player_round')
    def test_take_turns(self, mock_player_round, mock_computer_round):
        player1 = Player("Player1")
        player2 = Player("Computer")
        players = [player1, player2]
        game = Game(players, None, None, "")
        game.take_turns()

        mock_player_round.assert_called_once_with(player1)

        mock_player_round.reset_mock()

        game.curr_player_index = 1
        game.take_turns()

        mock_computer_round.assert_called_once_with(player2)

    @patch('game.Game.hold')
    @patch('game.Game.roll_dice')
    @patch('player.Player.add_round_points')
    @patch('intelligence.Intelligence.choose_action')
    def test_computer_round(self, mock_choose_action, mock_add_round_points,
                            mock_roll_dice, mock_hold):
        player1 = Player("Player1")
        player2 = Player("Computer")
        players = [player1, player2]
        strategy = Intelligence(1, 1)
        game = Game(players, None, strategy, '')

        mock_choose_action.return_value = "roll"
        game.computer_round(players[1])

        mock_add_round_points.assert_called_once_with(0)
        mock_roll_dice.assert_called_once()

        mock_choose_action.reset_mock()

        mock_choose_action.return_value = "hold"
        game.computer_round(players[1])
        mock_hold.assert_called_once()

    @patch('builtins.input', side_effect=['roll'])
    def test_player_round_roll(self, mock_input):
        player = Player("Player1")
        game = Game([], None, None, "")

        with patch.object(game, 'roll_dice') as mock_roll_dice:
            game.player_round(player)

        mock_roll_dice.assert_called_once()

    @patch('builtins.input', side_effect=['hold'])
    def test_player_round_hold(self, mock_input):
        player = Player("Player1")
        game = Game([], None, None, "")

        with patch.object(game, 'hold') as mock_hold:
            game.player_round(player)

        mock_hold.assert_called_once()

    @patch('builtins.input', side_effect=['cheat'])
    def test_player_round_cheat(self, mock_input):
        player = Player("Player1")
        game = Game([], None, None, "")

        with patch.object(game, 'cheat') as mock_cheat:
            game.player_round(player)

        mock_cheat.assert_called_once()

    @patch('builtins.input', side_effect=['exit'])
    def test_player_round_exit(self, mock_input):
        player = Player("Player1")
        game = Game([], None, None, "")

        with patch.object(game, 'end_game') as mock_end_game:
            game.player_round(player)

        mock_end_game.assert_called_once()

    @patch('builtins.input', side_effect=['randomStuff'])
    def test_player_round_invalid(self, mock_input):
        player = Player("Player1")
        game = Game([], None, None, "")

        expected_output = (
            "Invalid decision.\n"
            "Try 'roll', 'hold' or 'exit'\n"
            "or corresponding short cut: r, h or q.\n"
        )

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        game.player_round(player)
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        self.assertTrue(expected_output in output)

    @patch('game.Game.roll_result_1')
    def test_roll_dice_result_1_player(self, mock_roll_result_1):
        player = Player("Player1")
        dice = MagicMock()
        game = Game([], dice, None, "")

        dice.player_roll.return_value = 1
        game.roll_dice(player)

        mock_roll_result_1.assert_called_once_with(player)

    @patch('game.Game.roll_result_1')
    def test_roll_dice_result_1_computer(self, mock_roll_result_1):
        player = Player("Computer")
        dice = MagicMock()
        game = Game([], dice, None, "")

        dice.computer_roll.return_value = 1
        game.roll_dice(player)

        mock_roll_result_1.assert_called_once_with(player)

    @patch('game.Game.roll_result_other')
    def test_roll_dice_result_other_player(self, mock_roll_result_other):
        player = Player("Player1")
        dice = MagicMock()
        game = Game([], dice, None, "")

        dice.player_roll.return_value = 4
        game.roll_dice(player)

        mock_roll_result_other.assert_called_once_with(player, 4)

    @patch('game.Game.roll_result_other')
    def test_roll_dice_result_other_computer(self, mock_roll_result_other):
        player = Player("Computer")
        dice = MagicMock()
        game = Game([], dice, None, "")

        dice.computer_roll.return_value = 3
        game.roll_dice(player)

        mock_roll_result_other.assert_called_once_with(player, 3)

    @patch('game.Game.end_round')
    @patch('game.Game.end_turn')
    def test_hold(self, mock_end_turn, mock_end_round):
        player = Player("Player1")
        game = Game([], None, None, "")
        game.curr_player_index = 0
        game.hold(player)

        mock_end_round.assert_called_once()
        mock_end_turn.assert_called_once()

    @patch('game.Game.high_score_list_checking')
    @patch('game.Game.end_game')
    def test_cheat(self, mock_end_game, mock_high_score_list_checking):
        player = Player("Player1")
        game = Game([], None, None, "")
        game.curr_player_index = 0

        game.cheat(player, 1000)

        mock_high_score_list_checking.assert_called_once_with(player.name,
                                                              1000)
        mock_end_game.assert_called_once()

    @patch('player.Player.reset_round_points')
    @patch('player.Player.current_points_adjust')
    @patch('game.Game.end_round')
    @patch('game.Game.end_turn')
    def test_roll_result_1(self, mock_end_turn, mock_end_round,
                           mock_current_p, mock_reset_round_p):
        player = Player("Player1")
        game = Game([], None, None, "")
        game.curr_player_index = 0

        game.roll_result_1(player)

        mock_current_p.assert_called_once()
        mock_reset_round_p.assert_called_once()
        mock_end_round.assert_called_once()
        mock_end_turn.assert_called_once()

    @patch('player.Player.current_points')
    @patch('player.Player.add_round_points')
    @patch('game.Game.high_score_list_checking')
    @patch('game.Game.end_game')
    def test_roll_result_other(self, mock_end_game,
                               mock_high_score_list_checking,
                               mock_add_round_p, mock_curr_p):
        player = Player("Player1")
        game = Game([], None, None, "")

        mock_curr_p.return_value = 150
        game.roll_result_other(player, 4)

        mock_add_round_p.assert_called_once()
        mock_high_score_list_checking.assert_called_once_with(player.name, 150)
        mock_end_game.assert_called_once()

    @patch('score.Score.pvc_new_record')
    @patch('score.Score.pvp_new_record')
    def test_high_score_list_checking(self, mock_pvp_new_record,
                                      mock_pvc_new_record):
        game = Game([], None, None, "PvC")

        game.high_score_list_checking("Player1", 150)
        mock_pvc_new_record.assert_called_once_with("Player1", 150)
        mock_pvp_new_record.assert_not_called()

        mock_pvc_new_record.reset_mock()
        mock_pvp_new_record.reset_mock()

        game.mode = "PvP"
        game.high_score_list_checking("Player1", 150)
        mock_pvp_new_record.assert_called_once_with("Player1", 150)
        mock_pvc_new_record.assert_not_called()

    def test_end_game(self):
        game = Game([], None, None, "")
        game.end_game()

        self.assertTrue(game.game_over)

    def test_end_turn(self):
        game = Game([], None, None, "")
        game.curr_player_index = 0
        game.end_turn()

        self.assertEqual(game.curr_player_index, 1)

        game.end_turn()
        self.assertEqual(game.curr_player_index, 0)

    def test_start_round(self):
        game = Game([], None, None, "")
        game.start_round()

        self.assertFalse(game.round_finished)

    def test_end_round(self):
        game = Game([], None, None, "")
        game.curr_player_index = 1
        game.end_round()

        self.assertTrue(game.round_finished)
        self.assertEqual(game.round_count, 2)


if __name__ == "__main__":
    unittest.main()

"""unit testing for menu.py"""

from unittest.mock import patch, call
import unittest
import sys
import io
import cowsay
from menu import Menu
from score import Score


class testMenu(unittest.TestCase):
    """test the class"""

    def setUp(self):
        self.score = Score()
        self.menu = Menu(self.score)

    def tearDown(self):
        pass

    @patch('builtins.input', side_effect=['randomStuff', '4'])
    def test_menu_display(self, mock_input):
        expected_output = (
            "Welcome to Pig. Please choose an option, numbers only:\n"
            "1. Start game\n"
            "2. Game rules\n"
            "3. Scores\n"
            "4. Exit\n"
        )

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.menu.menu_main()
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        self.assertTrue(expected_output in output)
        self.assertTrue("Invalid value. Please enter numbers only"
                        in output)

    @patch('menu.Menu.start_game')
    @patch('menu.Menu.show_game_rules')
    @patch('menu.Menu.show_scores')
    @patch('score.Score.save_scores')
    @patch('builtins.input', side_effect=['1', '2', '3', '4'])
    def test_menu_options(self, mock_input, mock_save_scores,
                          mock_show_scores, mock_show_game_rules,
                          mock_start_game):
        self.menu.menu_main()

        mock_start_game.assert_called_once()
        mock_show_game_rules.assert_called_once()
        mock_show_scores.assert_called_once()
        mock_save_scores.assert_called_once()

    @patch('builtins.input', side_effect=['randomStuff', '3'])
    def test_start_game_display(self, mock_input):
        expected_output = (
            "Choose playing mode, numbers only:\n"
            "1. Play against computer\n"
            "2. Two players\n"
            "3. Back\n"
        )

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.menu.start_game()
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        self.assertTrue(expected_output in output)
        self.assertTrue("Invalid value. Please enter numbers only"
                        in output)

    @patch('game_settings.GameSettings.against_computer')
    @patch('game_settings.GameSettings.against_player')
    @patch('builtins.input', side_effect=['1', '2', '3'])
    def test_start_game_options(self, mock_input, mock_against_player,
                                mock_against_computer):
        self.menu.start_game()

        mock_against_computer.assert_called_once()
        mock_against_player.assert_called_once()

    def test_show_game_rules(self):
        expected_output = (
            """
            Each turn, a player repeatedly rolls a die until
            either a 1 is rolled or the player decides to
            "hold": If the player rolls a 1, they score
            nothing and it becomes the next player's turn.
            If the player rolls any other number, it is added
            to their turn total and the player's turn
            continues.
            If a player chooses to "hold", their turn total
            is added to their score, and it becomes the next
            player's turn. The first player to score 100 or
            more points wins.
            """
        )

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.menu.show_game_rules()
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        self.assertTrue(cowsay.get_output_string('tux', expected_output) in
                        output)

    @patch('builtins.input', side_effect=['randomStuff', '4'])
    def test_show_scores_display(self, mock_input):
        expected_output = (
            "Choose the list you want to check, numbers only\n"
            "1. PvC high score ranking\n"
            "2. PvP high score ranking\n"
            "3. Search for player's record\n"
            "4. Back\n"
        )

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.menu.show_scores()
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        self.assertTrue(expected_output in output)
        self.assertTrue("Invalid value. Please enter numbers only"
                        in output)

    @patch('score.Score.print_top_ten')
    @patch('menu.Menu.search_record')
    @patch('builtins.input', side_effect=['1', '2', '3', '4'])
    def test_show_scores_options(self, mock_input, mock_search_record,
                                 mock_print_top_ten):
        self.menu.show_scores()

        mock_print_top_ten.assert_has_calls([call('PvC'), call('PvP')])
        mock_search_record.assert_called_once()

    @patch('score.Score.get_player_pvc_scores')
    @patch('score.Score.get_player_pvp_scores')
    @patch('menu.Menu.change_username')
    @patch('builtins.input', return_value='testPlayer')
    def test_search_record(self, mock_input, mock_change_username,
                           mock_player_pvp_scores, mock_player_pvc_scores):
        expected_output = "Enter the player name you want to search for:"

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.menu.search_record()
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        self.assertTrue(expected_output in output)

        self.assertTrue(mock_player_pvc_scores)
        self.assertTrue(mock_player_pvp_scores)

        mock_change_username.assert_called_once()

    @patch('score.Score.update_player_name')
    @patch('builtins.input', side_effect=['c', '1', '3', 'randomStuffToQuit'])
    def test_change_username_change_pvc_or_quit(self, mock_input,
                                                mock_update_player_name):
        expected_output = "Press 'c' to change name, press any keys to go back"

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.menu.change_username('testName', True, True)
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        self.assertTrue(expected_output in output)

        mock_update_player_name.assert_called_once()

    @patch('score.Score.update_player_name')
    @patch('builtins.input', side_effect=['c', '2', 'randomStuff', '3'])
    def test_change_username_change_pvp_display_menu(self, mock_input,
                                                     mock_update_player_name):
        expected_output = (
            "In which mode do you want to change your name?\n"
            "1. PvC\n"
            "2. PvP\n"
            "3. Back\n"
            "Enter number only\n"
        )

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.menu.change_username('testName', True, True)
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        self.assertTrue(expected_output in output)

        mock_update_player_name.assert_called_once()

        self.assertTrue("Invalid value. Please enter numbers only"
                        in output)

    @patch('score.Score.update_player_name')
    @patch('builtins.input', side_effect=['c', 'c'])
    def test_change_username_only_one_name_in_list(self, mock_input,
                                                   mock_update_player_name):
        self.menu.change_username('testName', True, False)

        score = Score()
        self.menu = Menu(score)
        self.menu.change_username('testName', False, True)

        self.assertEqual(mock_update_player_name.call_count, 2)


if __name__ == "__main__":
    unittest.main()

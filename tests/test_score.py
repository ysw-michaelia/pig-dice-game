"""Test file for testing score."""

import unittest
import io
from unittest.mock import patch, mock_open
from pigGame.score import Score


class TestScore(unittest.TestCase):
    """ Test score class"""

    def setUp(self):
        self.score = Score()

    def tearDown(self):
        pass

    @patch('pigGame.score.open', new_callable=mock_open)
    @patch('json.dump')
    def test_save_scores(self, mock_dump, mock_open):
        Score.save_scores()

        mock_dump.assert_called_once_with({
            'pvc_high_scores': Score.pvc_high_scores,
            'pvp_high_scores': Score.pvp_high_scores
        }, mock_open.return_value)

    @patch('builtins.open', new_callable=mock_open)
    @patch('json.load')
    def test_load_scores(self, mock_load, mock_open):
        test_data = {
            'pvc_high_scores': {'testPlayer1': [100], 'testPlayer2': [200]},
            'pvp_high_scores': {'testPlayer1': [150], 'testPlayer2': [250]}
        }
        mock_load.return_value = test_data

        Score.load_scores()
        mock_open.assert_called_once_with('scores.json', 'r', encoding='utf-8')
        mock_load.assert_called_once()

        self.assertDictEqual(Score.pvc_high_scores, test_data['pvc_high_scores'])
        self.assertDictEqual(Score.pvp_high_scores, test_data['pvp_high_scores'])

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_load_scores_file_not_found(self, mock_open):
        Score.load_scores()
        self.assertTrue(True) 

    def test_pvc_new_record(self):
        player_name = "TestPlayer"
        score = 100
        self.score.pvc_new_record(player_name, score)
        self.assertIn(player_name, self.score.pvc_high_scores)
        self.assertEqual(self.score.pvc_high_scores[player_name], [score])

    def test_pvc_has_player(self):
        player_name = "TestPlayer"
        self.assertFalse(self.score.pvc_has_player(player_name))
        self.score.pvc_high_scores[player_name] = [50]
        self.assertTrue(self.score.pvc_has_player(player_name))

    def test_pvp_new_record(self):
        player_name = "TestPlayer"
        score = 100
        self.score.pvp_new_record(player_name, score)
        self.assertIn(player_name, self.score.pvp_high_scores)
        self.assertEqual(self.score.pvp_high_scores[player_name], [score])

    def test_pvp_has_player(self):
        player_name = "TestPlayer"
        self.assertFalse(self.score.pvp_has_player(player_name))
        self.score.pvp_high_scores[player_name] = [50]
        self.assertTrue(self.score.pvp_has_player(player_name))

    @patch('pigGame.score.Score.print_top_scores')
    def test_print_top_ten_pvc(self, mock_print_top_scores):
        self.score.print_top_ten("PvC")
        mock_print_top_scores.assert_called_once_with("PvC", self.score.pvc_high_scores)

    @patch('pigGame.score.Score.print_top_scores')
    def test_print_top_ten_pvp(self, mock_print_top_scores):
        self.score.print_top_ten("PvP")
        mock_print_top_scores.assert_called_once_with("PvP", self.score.pvp_high_scores)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_top_scores_no_records(self, mock_stdout):
        mode = "PvC"
        high_scores = {}
        self.score.print_top_scores("PvC", high_scores)
        output = mock_stdout.getvalue().strip()
        expected_output = f"{mode} Top Ten High Scores:\nNo record"
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_top_scores_with_records(self, mock_stdout):
        mode = "PvP"
        high_scores = {"Player1": [50], "Player2": [40, 60]}
        self.score.print_top_scores(mode, high_scores)
        output = mock_stdout.getvalue().strip()
        expected_output = f"{mode} Top Ten High Scores:\n1. Player2: 100\n2. Player1: 50"
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_player_pvc_scores_existing_player(self, mock_stdout):
        player_name = "Player1"
        self.score.pvc_high_scores = {"Player1": [50, 60]}
        self.assertTrue(self.score.get_player_pvc_scores(player_name))
        output = mock_stdout.getvalue().strip()
        expected_output = f"Scores for {player_name} in PvC: [50, 60]"
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_player_pvc_scores_non_existing_player(self, mock_stdout):
        player_name = "Player2"
        self.score.pvc_high_scores = {"Player1": [50, 60]}
        self.assertFalse(self.score.get_player_pvc_scores(player_name))
        output = mock_stdout.getvalue().strip()
        expected_output = "Name does not exist in PvC"
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_player_pvp_scores_existing_player(self, mock_stdout):
        player_name = "Player1"
        self.score.pvp_high_scores = {"Player1": [50, 60]}
        self.assertTrue(self.score.get_player_pvp_scores(player_name))
        output = mock_stdout.getvalue().strip()
        expected_output = f"Scores for {player_name} in PvP: [50, 60]"
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_player_pvp_scores_non_existing_player(self, mock_stdout):
        player_name = "Player2"
        self.score.pvp_high_scores = {"Player1": [50, 60]}
        self.assertFalse(self.score.get_player_pvp_scores(player_name))
        output = mock_stdout.getvalue().strip()
        expected_output = "Name does not exist in PvP"
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["Player2", "NewPlayer"])
    def test_update_player_name_pvc(self, mock_input, mock_stdout):
        old_name = "Player1"
        self.score.pvc_high_scores = {"Player1": [50, 60], "Player2": [40, 70]}
        self.score.update_player_name(old_name, 1)
        output = mock_stdout.getvalue().strip()
        expected_output = "Name is already taken in PvC list."
        self.assertIn(expected_output.strip(), output.strip())

        self.assertIn("NewPlayer", self.score.pvc_high_scores)
        self.assertNotIn("Player1", self.score.pvc_high_scores)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["Player2", "NewPlayer"])
    def test_update_player_name_pvp(self, mock_input, mock_stdout):
        old_name = "Player1"
        self.score.pvp_high_scores = {"Player1": [50, 60], "Player2": [40, 70]}
        self.score.update_player_name(old_name, 2)
        output = mock_stdout.getvalue().strip()
        expected_output = "Name is already taken in PvP list."
        self.assertIn(expected_output.strip(), output.strip())

        self.assertIn("NewPlayer", self.score.pvp_high_scores)
        self.assertNotIn("Player1", self.score.pvp_high_scores)


if __name__ == "__main__":
    unittest.main()

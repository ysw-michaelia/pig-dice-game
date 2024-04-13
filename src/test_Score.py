"""Test file for testing score."""

import unittest
from unittest.mock import patch
from score import Score

class TestScore(unittest.TestCase):
    """ Test score class"""

    @classmethod
    def setUpClass(cls):
        cls.score = Score()

    def test_pvc_new_record(self):
        """ test_pvc_new_record"""
        self.score.pvc_new_record("TestPlayer", 100)
        self.assertIn("TestPlayer", self.score.pvc_high_scores)
        self.assertEqual(self.score.pvc_high_scores["TestPlayer"], [100])

    def test_pvc_has_player(self):
        """ test_pvc_new_record"""
        self.score.pvc_high_scores["TestPlayer"] = [100]
        self.assertTrue(self.score.pvc_has_player("TestPlayer"))
        self.assertFalse(self.score.pvc_has_player("NonExistentPlayer"))

    def test_pvp_new_record(self):
        """ test_pvc_new_record"""
        self.score.pvp_new_record("TestPlayer", 100)
        self.assertIn("TestPlayer", self.score.pvp_high_scores)
        self.assertEqual(self.score.pvp_high_scores["TestPlayer"], [100])

    def test_pvp_has_player(self):
        """ test_pvp_has_player"""
        self.score.pvp_high_scores["TestPlayer"] = [100]
        self.assertTrue(self.score.pvp_has_player("TestPlayer"))
        self.assertFalse(self.score.pvp_has_player("NonExistentPlayer"))


    @patch("builtins.print")
    def test_print_top_scores_no_records(self, mock_print):
        """ test_print_top_scores_no_records"""
        self.score.print_top_scores("PvC", {})
        mock_print.assert_any_call("PvC Top Ten High Scores:")
        mock_print.assert_any_call("No record")


    @patch("builtins.print")
    def print_top_scores(self, mode, scores):
        """ print_top_scores"""
        print(f"{mode} Top Ten High Scores:")
        if not scores:
            print("No record")
        else:
            sorted_scores = sorted(scores.items(), key=lambda x: max(x[1]), reverse=True)[:10]
            for i, (player, scores) in enumerate(sorted_scores, 1):
                print(f"{i}. {player}: {max(scores)}")

    def test_get_player_pvc_scores(self):
        """test_get_player_pvc_scores"""
        self.score.pvc_high_scores = {"TestPlayer": [100]}
        with patch("builtins.print") as mock_print:
            self.assertTrue(self.score.get_player_pvc_scores("TestPlayer"))
            mock_print.assert_called_with("Scores for TestPlayer in PvC: [100]")

            self.assertFalse(self.score.get_player_pvc_scores("NonExistentPlayer"))
            mock_print.assert_called_with("Name does not exist in PvC")

    def test_get_player_pvp_scores(self):
        """test_get_plaer_pvp_scores"""
        self.score.pvp_high_scores = {"TestPlayer": [100]}
        with patch("builtins.print") as mock_print:
            self.assertTrue(self.score.get_player_pvp_scores("TestPlayer"))
            mock_print.assert_called_with("Scores for TestPlayer in PvP: [100]")

            self.assertFalse(self.score.get_player_pvp_scores("NonExistentPlayer"))
            mock_print.assert_called_with("Name does not exist in PvP")

    def test_update_player_name(self):
        """test_update_player_name"""
        self.score.pvc_high_scores = {"OldName": [100]}
        with patch("builtins.input", side_effect=["NewName"]):
            self.score.update_player_name("OldName", 1)
            self.assertNotIn("OldName", self.score.pvc_high_scores)
            self.assertIn("NewName", self.score.pvc_high_scores)

if __name__ == "__main__":
    unittest.main()

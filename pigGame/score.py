"""
The Score module provides functionality for managing and storing player scores.

Attributes:
    pvc_high_scores (dict): A dictionary containing the high scores of players
        in Player vs Computer (PvC) mode.
    pvp_high_scores (dict): A dictionary containing the high scores of players
        in Player vs Player (PvP) mode.
"""

import json
import sys
from termcolor import cprint
from colorama import init

init(strip=not sys.stdout.isatty())


class Score:
    """
    A class to manage and operate on game scores.

    It  includs saving, loading, updating, and printing high scores.

    Attributes:
        pvc_high_scores (dict): A dictionary storing Player vs Computer scores.
        pvp_high_scores (dict): A dictionary storing Player vs Player scores.
    """

    pvc_high_scores = {"testPlayer": [50]}
    pvp_high_scores = {"testPlayer": [50]}

    @staticmethod
    def save_scores():
        """Save high scores to a JSON file named 'scores.json'."""
        data = {
            "pvc_high_scores": Score.pvc_high_scores,
            "pvp_high_scores": Score.pvp_high_scores,
        }
        with open("scores.json", "w", encoding="utf-8") as file:
            json.dump(data, file)

    @staticmethod
    def load_scores():
        """Load high scores from the JSON file 'scores.json'."""
        try:
            with open("scores.json", "r", encoding="utf-8") as file:
                scores = json.load(file)
                Score.pvc_high_scores = scores.get("pvc_high_scores", {})
                Score.pvp_high_scores = scores.get("pvp_high_scores", {})
        except FileNotFoundError:
            pass

    def pvc_new_record(self, player_name, score):
        """
        Add a new high score for Player vs Computer mode.

        Args:
            player_name (str): The name of the player.
            score (int): The score achieved by the player.
        """
        self.pvc_high_scores[player_name] = [score]

    def pvc_has_player(self, player_name):
        """
        Check if a player exists in the Player vs Computer high scores.

        Args:
            player_name (str): The name of the player to check.

        Returns:
            bool: True if the player exists, False otherwise.
        """
        return player_name in self.pvc_high_scores

    def pvp_new_record(self, player_name, score):
        """
        Add a new high score for Player vs player mode.

        Args:
            player_name (str): The name of the player.
            score (int): The score achieved by the player.
        """
        self.pvp_high_scores[player_name] = [score]

    def pvp_has_player(self, player_name):
        """
        Check if a player exists in the Player vs Player high scores.

        Args:
            player_name (str): The name of the player to check.

        Returns:
            bool: True if the player exists, False otherwise.
        """
        return player_name in self.pvp_high_scores

    def print_top_ten(self, mode):
        """
        Print the top ten high scores for a specified mode.

        Args:
            mode (str): The game mode to print high scores for 'PvC' or 'PvP'.
        """
        if mode == "PvC":
            self.print_top_scores("PvC", self.pvc_high_scores)
        elif mode == "PvP":
            self.print_top_scores("PvP", self.pvp_high_scores)

    def print_top_scores(self, mode, high_scores):
        """
        Print the top scores for a specified mode.

        Args:
            mode (str): The game mode ('PvC' or 'PvP').
            high_scores (dict): The dictionary containing the high scores.
        """
        if not high_scores:
            cprint(f"{mode} Top Ten High Scores:", "green", attrs=["bold"])
            cprint("No record", "yellow", attrs=["bold"])
            return

        sorted_scores = sorted(
            high_scores.items(), key=lambda x: sum(x[1]), reverse=True
        )
        cprint(f"{mode} Top Ten High Scores:", "green", attrs=["bold"])
        for i, (player_name, scores) in enumerate(sorted_scores[:10], start=1):
            total_score = sum(scores)
            cprint(f"{i}. {player_name}: {total_score}", "yellow",
                   attrs=["bold"])

    def get_player_pvc_scores(self, player_name):
        """
        Get the scores of a player in Player vs Computer mode.

        Args:
            player_name (str): The name of the player.

        Returns:
            bool: True if the player exists in the scores, False otherwise.
        """
        if player_name in self.pvc_high_scores:
            scores = self.pvc_high_scores[player_name]
            cprint(
                f"Scores for {player_name} in PvC: {scores}", "yellow",
                attrs=["bold"]
            )
            return True
        cprint("Name does not exist in PvC", "yellow", attrs=["bold"])
        return False

    def get_player_pvp_scores(self, player_name):
        """
        Get the scores of a player in Player vs Player mode.

        Args:
            player_name (str): The name of the player.

        Returns:
            bool: True if the player exists in the scores, False otherwise.
        """
        if player_name in self.pvp_high_scores:
            scores = self.pvp_high_scores[player_name]
            cprint(
                f"Scores for {player_name} in PvP: {scores}", "yellow",
                attrs=["bold"]
            )
            return True
        cprint("Name does not exist in PvP", "yellow", attrs=["bold"])
        return False

    def update_player_name(self, old_name, message):
        """
        Update the name of a player in the high scores.

        Args:
            old_name (str): The current name of the player.
            message (int): A message indicating the game mode.
        """
        mode = "PvC" if message == 1 else "PvP"
        if mode == "PvC":
            high_scores = self.pvc_high_scores
        else:
            high_scores = self.pvp_high_scores

        while True:
            cprint("Your new name is:", "green",
                   attrs=["bold"])
            new_name = input()
            print("")
            if old_name in high_scores:
                if new_name not in high_scores:
                    high_scores[new_name] = high_scores.pop(old_name)
                    break
                cprint(
                    f"Name is already taken in {mode} list.", "red",
                    attrs=["bold"]
                )

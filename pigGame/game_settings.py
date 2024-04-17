"""
This module contains the GameSettings class.

It is responsible for setting up the game configurations for a dice game.
This includes configuring games against the computer with varying difficulties
or setting up a game between two players.

Classes:
    GameSettings: Handles the configuration and setup of game settings based on
    user input, including the mode (player vs computer or player vs player),
    the difficulty level of the computer opponent, and obtaining player names.
"""
import sys
from termcolor import cprint
from colorama import init
from pigGame.intelligence import Intelligence
from pigGame.dice import Dice
from pigGame.player import Player
from pigGame.game import Game
init(strip=not sys.stdout.isatty())


class GameSettings:
    """
    Handles the setup and configuration of game settings for the dice game.

    Attributes:
        score (Score): An instance of the Score class used for score management
        and to check if player names already exist in the score records.

    Methods:
        against_computer(): Configures and starts a game against the computer.
        against_player(): Configures and starts a game between two players.
        get_difficulty(message): Prompts the user for the difficulty level
        of the computer.
        get_player_name(message): Obtains and validates player names.
    """

    def __init__(self, score):
        """
        Initialize a GameSettings object with the provided score.

        Args:
            score (Score): An instance of the Score class used for score
            management and to check if player names already exist in the
            score records.

        Attributes:
            score (Score): An instance of the Score class to manage scores.

        Example:
            # Initialize a GameSettings object with a Score instance
            score_instance = Score()
            game_settings = GameSettings(score_instance)
        """
        self.score = score

    def against_computer(self):
        """
        Configure and starts a game against the computer.

        This includes setting the intelligence for the computer's dice
        probability and strategy, and initializing the game with these
        settings.
        """
        cprint("Difficulty:", "green", attrs=["bold"])
        prob_difficulty = self.get_difficulty(1)
        stra_difficulty = self.get_difficulty(2)
        diff = Intelligence(int(prob_difficulty), int(stra_difficulty))
        dice = Dice(probability=diff.dice_probability())
        player1 = self.get_player_name(1)
        computer = Player("Computer")
        players = [player1, computer]
        game = Game(players, dice, strategy=diff, mode="PvC")
        game.start_game()

    def against_player(self):
        """
        Configure and starts a game between two players.

        It obtains the names for both players and initializes the game without
        any specific strategy or modified dice probability, implying a fair
        game.
        """
        player1 = self.get_player_name("Player 1")
        player2 = self.get_player_name("Player 2")
        players = [player1, player2]
        dice = Dice(probability=None)
        game = Game(players, dice, strategy=None, mode="PvP")
        game.start_game()

    def get_difficulty(self, message):
        """
        Prompt the user to select a difficulty level for the computer.

        This method presents the user with a prompt to select the difficulty
        level for either the computer's dice probability or its strategy,
        based on the value of the 'message' argument. If 'message' is 1,
        it prompts the user to choose the difficulty level for the dice
        probability. If 'message' is 2, it prompts the user to choose the
        difficulty level for the computer's strategy.

        Parameters:
            message (int): An integer value that determines the type of
                difficulty level being prompted. If 'message' is 1, it prompts
                for dice probability difficulty. If 'message' is 2, it prompts
                for computer strategy difficulty.

        Returns:
            str: The chosen difficulty level as a string, guaranteed to be
                between "1" and "5". If the user provides an invalid value,
                the method continues to prompt until a valid difficulty level
                is selected.
        """
        while True:
            if message == 1:
                cprint("Please choose probability of dice roll level,",
                       "green", attrs=["bold"])
                cprint("from 1 to 5:", "green", attrs=["bold"])
                difficulty = input()
                if difficulty in {"1", "2", "3", "4", "5"}:
                    return difficulty
                else:
                    cprint("Invalid value, please try again.",
                           "red", attrs=["bold"])
            elif message == 2:
                cprint("Please choose computer strategy difficulty,",
                       "green", attrs=["bold"])
                cprint("from 1 to 5:", "green", attrs=["bold"])
                difficulty = input()
                if difficulty in {"1", "2", "3", "4", "5"}:
                    return difficulty
                else:
                    cprint("Invalid value, please try again.",
                           "red", attrs=["bold"])

    def get_player_name(self, message):
        """
        Obtain a player name from user input and ensure its uniqueness.

        This method prompts the user to enter a player name based on the
        provided message or identifier. It ensures that the entered name is
        not "Computer" or "computer" and does not already exist in the
        relevant score records, depending on the game mode specified by the
        message.

        Parameters:
            message (str or int): A message or identifier indicating whether
                the name is for a player in a Player vs. Computer (PvC) or
                Player vs. Player (PvP) setting.

        Returns:
            Player: A new Player instance with the provided name.
        """
        if message == 1:
            while True:
                cprint('Your name is:', "green", attrs=["bold"])
                name = input()
                print('')
                if name == "Computer" or name == "computer":
                    cprint('Invalid name, try a new one',
                           "red", attrs=["bold"])
                elif not self.score.pvc_has_player(name):
                    return Player(name)
                else:
                    cprint('Name exists, try a new one.',
                           "red", attrs=["bold"])
        else:
            while True:
                cprint(f'{message}, your name is:',
                       "green", attrs=["bold"])
                name = input()
                print('')
                if not self.score.pvp_has_player(name):
                    return Player(name)
                else:
                    cprint('Name exists, try a new one.',
                           "red", attrs=["bold"])

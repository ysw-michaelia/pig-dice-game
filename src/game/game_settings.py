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
from intelligence import Intelligence
from dice import Dice
from player import Player
from game import Game


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
        self.score = score

    def against_computer(self):
        """
        Configures and starts a game against the computer. This includes
        setting the intelligence for the computer's dice probability and
        strategy, and initializing the game with these settings.
        """
        print("Difficulty adjust")
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
        Configures and starts a game between two players. It obtains the names
        for both players and initializes the game without any specific strategy
        or modified dice probability, implying a fair game.
        """
        player1 = self.get_player_name("Player 1")
        player2 = self.get_player_name("Player 2")
        players = [player1, player2]
        dice = Dice(probability=None)
        game = Game(players, dice, strategy=None, mode="PvP")
        game.start_game()

    def get_difficulty(self, message):
        """
        Prompts the user to select a difficulty level for the computer, either
        for dice probability or strategy based on the message argument.

        Parameters:
            message (int): Determines whether the prompt is for selecting the
            dice probability difficulty (1) or the strategy difficulty (2).

        Returns:
            str: The chosen difficulty level as a string, guaranteed to be
            between "1" and "5".
        """
        while True:
            if message == 1:
                print("Please choose probability of dice roll level,")
                print("from 1 to 5:")
                difficulty = input()
                if difficulty in {"1", "2", "3", "4", "5"}:
                    return difficulty
                else:
                    print("Invalid value, please try again.")
            elif message == 2:
                print("Please choose computer strategy difficulty,")
                print("from 1 to 5:")
                difficulty = input()
                if difficulty in {"1", "2", "3", "4", "5"}:
                    return difficulty
                else:
                    print("Invalid value, please try again.")

    def get_player_name(self, message):
        """
        Obtains a player name from user input. Ensures the name is not
        "Computer" and does not already exist in the relevant score records,
        based on the game mode.

        Parameters:
            message (str or int): A message or identifier to indicate whether
            the name is for a player in a PvC or PvP setting.

        Returns:
            Player: A new Player instance with the provided name.
        """
        if message == 1:
            while True:
                print('Your name is:')
                name = input()
                print('')
                if name == "Computer" or name == "computer":
                    print('Invalid name, try a new one')
                elif not self.score.pvc_has_player(name):
                    return Player(name)
                else:
                    print('Name exists, try a new one.')
        else:
            while True:
                print(f'{message}, your name is:')
                name = input()
                print('')
                if not self.score.pvp_has_player(name):
                    return Player(name)
                else:
                    print('Name exists, try a new one.')

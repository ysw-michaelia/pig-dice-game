"""
The Game module contains the Game class, which represents a game of Pig.

The game involves players taking turns rolling a die to accumulate points.
The game can be played in different modes, including Player vs Player (PvP)
and Player vs Computer (PvC).
"""
import time
from score import Score


class Game:
    """
    Represents a game of Pig, where players take turns rolling a die
    to accumulate points.
    The game can be played in different modes: Player vs Player (PvP)
    or Player vs Computer (PvC).

    Attributes:
        players (list of Player): A list containing the two players.
        dice (Dice): An instance of the Dice class representing the game's die.
        strategy (Intelligence): An instance of the Intelligence class
            representing the computer's intelligence.
        mode (str): The mode of the game, either "PvP" or "PvC".
        target_score (int): The target score that players need to reach to win.
        current_player_index (int): Index of the current player taking turns.
        game_over (bool): Indicates whether the game is over.
    """

    def __init__(self, players, dice, strategy, mode):
        self.players = players
        self.dice = dice
        self.strategy = strategy
        self.mode = mode
        self.target_score = 100
        self.current_player_index = 0
        self.game_over = False

    def start_game(self):
        """
        Starts the game and manages the flow of turns between players until
        the game is over.
        """
        while not self.game_over:
            print(f"{self.players[self.current_player_index].name}'s turn")
            self.take_turns()

    def take_turns(self):
        """
        Manages the turns for each player, calling the appropriate round
        method based on the player."""
        current_player = self.players[self.current_player_index]
        if current_player.name == 'Computer':
            self.computer_round(current_player)
        else:
            self.player_round(current_player)

    def computer_round(self, current_player):
        """Conducts a round of the game for the computer player."""
        round_points = current_player.add_round_points(0)
        if self.strategy.choose_action(round_points) == "roll":
            self.roll_dice(current_player)
            print('')
        else:
            self.hold(current_player)
            print('')

    def player_round(self, current_player):
        """
        Conducts a round of the game for a human player. When it is PvP,
        two players both using this method.
        """
        print('"roll"(r), "hold"(h), cheat(c) or "exit"(q)')
        decision = input().lower()
        if decision.lower() == "roll" or decision.lower() == "r":
            self.roll_dice(current_player)
        elif decision.lower() == "hold" or decision.lower() == "h":
            self.hold(current_player)
        elif decision.lower == "cheat" or decision.lower() == "c":
            self.cheat(current_player, 1000)
        elif decision.lower == "exit" or decision.lower() == "q":
            print('Feel free to join again! :)')
            print('')
            self.end_game()
        else:
            print("Invalid decision.")
            print("Try 'roll', 'hold' or 'exit'")
            print("or corresponding short cut: r, h or q.")
            print('')

    def roll_dice(self, player):
        """
        Simulates rolling the die for the current player and handles the
        outcomes.
        """
        print(f'{player.name} decided to roll.')
        time.sleep(1)
        if player.name != "Computer":
            result = self.dice.player_roll()
        else:
            result = self.dice.computer_roll()

        if result == 1:
            print(f"{player.name} rolled a 1. Your turn is over.")
            print('')
            time.sleep(1)
            player.current_points_adjust()
            player.reset_round_points()
            self.end_turn()
        else:
            player.add_round_points(result)
            curr_points = player.current_points(result)
            print(f'{player.name} got {result}. Total points: {curr_points}')
            print('')
            time.sleep(1)
            if curr_points >= self.target_score:
                print(f"Congratulations! {player.name} wins!")
                print('')
                self.high_score_list_checking(player.name, curr_points)
                self.end_game()

    def hold(self, player):
        """Handles the decision to hold the current player's turn."""
        curr_points = player.current_points(0)
        player.reset_round_points()
        print(f"{player.name} decided to hold.")
        time.sleep(1)
        print(f"{player.name} total points: {curr_points}")
        print('')
        time.sleep(1)
        self.end_turn()

    def cheat(self, player, cheat):
        """
        Simulates a cheating move for the player, adding a specified amount
        of points.
        """
        cheat_points = player.current_points(cheat)
        print(f'{player.name} got {cheat}. Total points: {cheat_points}')
        print(f"Congratulations! {player.name} wins!")
        print('')
        self.high_score_list_checking(player.name, cheat_points)
        self.end_game()

    def high_score_list_checking(self, name, points):
        """ Updates the high score list based on the game mode and player."""
        score = Score()
        if self.mode == "PvC" and name != "Computer":
            score.pvc_new_record(name, points)
        elif self.mode == "PvP":
            score.pvp_new_record(name, points)

    def end_game(self):
        """End the game"""
        self.game_over = True

    def end_turn(self):
        """Ends the current player's turn and switches to the next player."""
        self.current_player_index = (self.current_player_index + 1) % 2

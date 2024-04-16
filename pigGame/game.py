"""
The Game module contains the Game class, which represents a game of Pig.

The game involves players taking turns rolling a die to accumulate points.
The game can be played in different modes, including Player vs Player (PvP)
and Player vs Computer (PvC).
"""
import time
import sys
import cowsay
from termcolor import cprint
from pyfiglet import figlet_format
from colorama import init
from pigGame.score import Score
init(strip=not sys.stdout.isatty())


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
        curr_player_index (int): Index of the current player taking turns.
        game_over (bool): Indicates whether the game is over.
    """

    def __init__(self, players, dice, strategy, mode):
        self.players = players
        self.dice = dice
        self.strategy = strategy
        self.mode = mode
        self.target_score = 100
        self.curr_player_index = 0
        self.round_count = 1
        self.game_over = False
        self.round_finished = True

    def start_game(self):
        """
        Starts the game and manages the flow of turns between players until
        the game is over.
        """
        while not self.game_over:
            if self.round_finished:
                cprint(figlet_format(f'ROUND {self.round_count}',
                                     font='banner3-D'),
                       'green', 'on_black', attrs=['bold'])
                self.start_round()
                time.sleep(1)
            if self.curr_player_index == 0:
                cprint(f"{self.players[self.curr_player_index].name}'s turn",
                       "yellow", attrs=['bold'])
            else:
                cprint(f"{self.players[self.curr_player_index].name}'s turn",
                       "cyan", attrs=['bold'])
            self.take_turns()

    def take_turns(self):
        """
        Manages the turns for each player, calling the appropriate round
        method based on the player."""
        current_player = self.players[self.curr_player_index]
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
        if self.curr_player_index == 0:
            cprint('"roll"(r), "hold"(h), cheat(c) or "exit"(q)',
                   'yellow', attrs=['bold'])
        else:
            cprint('"roll"(r), "hold"(h), cheat(c) or "exit"(q)',
                   'cyan', attrs=['bold'])
        decision = input().lower()
        if decision.lower() == "roll" or decision.lower() == "r":
            self.roll_dice(current_player)
        elif decision.lower() == "hold" or decision.lower() == "h":
            self.hold(current_player)
        elif decision.lower() == "cheat" or decision.lower() == "c":
            self.cheat(current_player, 1000)
        elif decision.lower() == "exit" or decision.lower() == "q":
            cprint(cowsay.get_output_string('cow', 'Feel free to join again!'),
                   'green', attrs=['bold'])
            print('')
            self.end_game()
        else:
            cprint("Invalid decision.")
            cprint("Try 'roll', 'hold' or 'exit'")
            cprint("or corresponding short cut: r, h or q.")
            print('')

    def roll_dice(self, player):
        """
        Simulates rolling the die for the current player and handles the
        outcomes.
        """
        if self.curr_player_index == 0:
            cprint(f'{player.name} decided to roll.', 'yellow', attrs=['bold'])
        else:
            cprint(f'{player.name} decided to roll.', 'cyan', attrs=['bold'])
        time.sleep(1)

        if player.name != "Computer":
            result = self.dice.player_roll()
        else:
            result = self.dice.computer_roll()

        if result == 1:
            self.roll_result_1(player)
        else:
            self.roll_result_other(player, result)

    def hold(self, player):
        """Handles the decision to hold the current player's turn."""
        curr_points = player.current_points(0)
        player.reset_round_points()
        if self.curr_player_index == 0:
            cprint(f"{player.name} decided to hold.",
                   "yellow", attrs=['bold'])
            time.sleep(1)
            cprint(f"{player.name} total points: {curr_points}",
                   "yellow", attrs=['bold'])
        else:
            cprint(f"{player.name} decided to hold.",
                   "cyan", attrs=['bold'])
            time.sleep(1)
            cprint(f"{player.name} total points: {curr_points}",
                   "cyan", attrs=['bold'])
        print('')
        time.sleep(1)
        self.end_round()
        self.end_turn()

    def cheat(self, player, cheat):
        """
        Simulates a cheating move for the player, adding a specified amount
        of points.
        """
        cheat_points = player.current_points(cheat)
        if self.curr_player_index == 0:
            cprint(f"{player.name} decided to cheat.",
                   "yellow", attrs=['bold'])
            cprint(f'{player.name} got {cheat}. Total points: {cheat_points}',
                   "yellow", attrs=['bold'])
        else:
            cprint(f"{player.name} decided to cheat.",
                   "cyan", attrs=['bold'])
            cprint(f'{player.name} got {cheat}. Total points: {cheat_points}',
                   "cyan", attrs=['bold'])
        cprint(cowsay.get_output_string(
            'turtle', f'Congratulations! {player.name} wins!'),
            'green', attrs=['bold'])
        print('')
        self.high_score_list_checking(player.name, cheat_points)
        self.end_game()

    def roll_result_1(self, player):
        """When die gets result 1, this method would be activated"""
        if self.curr_player_index == 0:
            cprint(f"{player.name} rolled a 1. Your turn is over.",
                   'yellow', attrs=['bold'])
        else:
            cprint(f"{player.name} rolled a 1. Your turn is over.",
                   'cyan', attrs=['bold'])
        print('')
        time.sleep(1)
        player.current_points_adjust()
        player.reset_round_points()
        self.end_round()
        self.end_turn()

    def roll_result_other(self, player, result):
        """When die gets other results than 1, this method would activate"""
        player.add_round_points(result)
        curr_points = player.current_points(result)
        if self.curr_player_index == 0:
            cprint(f'{player.name} got {result}.', 'yellow', attrs=['bold'])
            time.sleep(1)
            cprint(f'Total points: {curr_points}', 'yellow', attrs=['bold'])
        else:
            cprint(f'{player.name} got {result}.', 'cyan', attrs=['bold'])
            time.sleep(1)
            cprint(f'Total points: {curr_points}', 'cyan', attrs=['bold'])
        print('')
        time.sleep(1)
        if curr_points >= self.target_score:
            cprint(cowsay.get_output_string(
                'turtle', f'Congratulations! {player.name} wins!'),
                'green', attrs=['bold'])
            print('')
            self.high_score_list_checking(player.name, curr_points)
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
        self.curr_player_index = (self.curr_player_index + 1) % 2

    def start_round(self):
        """Start a round"""
        self.round_finished = False

    def end_round(self):
        """Ends the round after all the players finished"""
        if self.curr_player_index == 1:
            self.round_finished = True
            self.round_count += 1

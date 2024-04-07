"""
This module defines the Menu class which represents the main menu interface.

The Menu class provides functionalities for navigating through different
options in the game's main menu. These options include starting a new game,
viewing the game rules, checking high scores, and exiting the game.
It interacts with other components such as the Score class for score
management and the GameSettings class for configuring game settings before
the start of a game.

Classes:
    Menu: Handles the display and navigation of the game's main menu.

Dependencies:
    - score.py: Contains the Score class used for managing score-related
    functionalities.
    - gameSettings.py: Contains the GameSettings class used for configuring
    game settings.
"""

import sys
import cowsay
from termcolor import cprint
from pyfiglet import figlet_format
from colorama import init
from score import Score
from game_settings import GameSettings
init(strip=not sys.stdout.isatty())


class Menu:
    """
    Represents the main menu of the game, handling user input for game options,
    including starting a game, viewing rules, checking scores, and exiting.

    Attributes:
        score (Score): An instance of the Score class to manage score-related
        functionalities.
        game_settings (GameSettings): An instance of the GameSettings class to
        configure game settings.
    """

    def __init__(self, scores):
        self.score = scores
        self.score.load_scores()
        self.game_settings = GameSettings(scores)

    def menu_main(self):
        """
        Displays the main menu and handles the user's input to navigate
        through the menu options.
        """
        cprint(figlet_format('pig', font='isometric1'),
               'green', 'on_black', attrs=['bold'])
        while True:
            cprint("Welcome to Pig. Please choose an option, numbers only:",
                   "green", attrs=["bold"])
            cprint("1. Start game", "green", attrs=["bold"])
            cprint("2. Game rules", "green", attrs=["bold"])
            cprint("3. Scores", "green", attrs=["bold"])
            cprint("4. Exit", "green", attrs=["bold"])
            choice_menu = input()
            print('')

            if choice_menu == "1":
                self.start_game()
            elif choice_menu == "2":
                self.show_game_rules()
            elif choice_menu == "3":
                self.show_scores()
            elif choice_menu == "4":
                cprint("Saving...", "green", attrs=["bold"])
                self.score.save_scores()
                cprint("Thank you! See you next time!",
                       "green", attrs=["bold"])
                break
            else:
                cprint("Invalid value. Please try again. Enter numbers only",
                       "red", attrs=["bold"])

    def start_game(self):
        """
        Displays the game mode options and delegates the setting up of the
        game based on the user's choice.
        """
        while True:
            cprint("Choose playing mode, numbers only:",
                   "green", attrs=["bold"])
            cprint("1. Play against computer", "green", attrs=["bold"])
            cprint("2. Two players", "green", attrs=["bold"])
            cprint("3. Back", "green", attrs=["bold"])
            choice_mode = input()
            print('')

            if choice_mode == "1":
                self.game_settings.against_computer()
            elif choice_mode == "2":
                self.game_settings.against_player()
            elif choice_mode == "3":
                break
            else:
                cprint("Invalid value. Please try again",
                       "red", attrs=["bold"])

    def show_game_rules(self):
        """
        Prints the rules of the game to the console.
        """
        cprint(cowsay.get_output_string('tux', '''
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
        '''), "yellow", attrs=["bold"])

    def show_scores(self):
        """
        Displays the score menu, allowing users to view high scores or search
        for a player's scores.
        """
        while True:
            cprint('Choose the list you want to check, numbers only',
                   "green", attrs=["bold"])
            cprint('1. PvC high score ranking', "green", attrs=["bold"])
            cprint('2. PvP high score ranking', "green", attrs=["bold"])
            cprint("3. Search for player's record",
                   "green", attrs=["bold"])
            cprint('4. Back', "green", attrs=["bold"])
            choice_score = input()
            print('')
            if choice_score == "1":
                self.score.print_top_ten("PvC")
                print('')
            elif choice_score == "2":
                self.score.print_top_ten("PvP")
                print('')
            elif choice_score == "3":
                self.search_record()
            elif choice_score == "4":
                break
            else:
                cprint("Invalid value. Please try again",
                       'red', attrs=['bold'])

    def search_record(self):
        """
        Allows searching for a player's score record by name and offers the
        option to change the player's name.
        """
        cprint("Enter the player name you want to search for:",
               'green', attrs=['bold'])
        name = input()
        print('')
        pvc_player_exists = self.score.get_player_pvc_scores(name)
        print('')
        pvp_player_exists = self.score.get_player_pvp_scores(name)
        print('')
        if pvc_player_exists or pvp_player_exists:
            self.change_username(name, pvc_player_exists, pvp_player_exists)

    def change_username(self, name, pvc_player_exists, pvp_player_exists):
        """
        Provides an interface for changing a player's name in the score
        records.

        Args:
            name (str): The current name of the player.
            pvc_player_exists (bool): Indicates if the player has a PvC
            (Player vs Computer) score record.
            pvp_player_exists (bool): Indicates if the player has a PvP
            (Player vs Player) score record.
        """
        cprint("Press 'c' to change name, press any keys to go back",
               'green', attrs=['bold'])
        choice = input().lower()
        print('')
        if choice == "c":
            if pvc_player_exists and pvp_player_exists:
                while True:
                    cprint('In which mode do you want to change your name?',
                           "green", attrs=["bold"])
                    cprint('1. PvC', "green", attrs=["bold"])
                    cprint('2. PvP', "green", attrs=["bold"])
                    cprint('3. Back', "green", attrs=["bold"])
                    cprint('Enter number only', "green", attrs=["bold"])
                    choice_name = input()
                    if choice_name == '1':
                        self.score.update_player_name(name, 1)
                        break
                    elif choice_name == '2':
                        self.score.update_player_name(name, 2)
                        break
                    elif choice_name == '3':
                        break
                    else:
                        cprint('Invalid value, please try again',
                               "red", attrs=["bold"])
            elif pvc_player_exists:
                self.score.update_player_name(name, 1)
            elif pvp_player_exists:
                self.score.update_player_name(name, 2)
        elif choice == "q":
            pass


if __name__ == "__main__":
    score = Score()
    menu = Menu(score)
    menu.menu_main()

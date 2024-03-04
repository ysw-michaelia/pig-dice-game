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

from score import Score
from game_settings import GameSettings


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
        self.game_settings = GameSettings(scores)

    def menu_main(self):
        """
        Displays the main menu and handles the user's input to navigate
        through the menu options.
        """
        self.score.load_scores()

        while True:
            print("Welcome to Pig. Please choose an option, numbers only:")
            print("1. Start game")
            print("2. Game rules")
            print("3. Scores")
            print("4. Exit")
            choice_menu = input()
            print('')

            if choice_menu == "1":
                self.start_game()
            elif choice_menu == "2":
                self.show_game_rules()
            elif choice_menu == "3":
                self.show_scores()
            elif choice_menu == "4":
                print("Saving...")
                self.score.save_scores()
                print("Thank you! See you next time!")
                break
            else:
                print("Invalid value. Please try again. Enter numbers only")

    def start_game(self):
        """
        Displays the game mode options and delegates the setting up of the
        game based on the user's choice.
        """
        while True:
            print("Choose playing mode, numbers only:")
            print("1. Play against computer")
            print("2. Two players")
            print("3. Back")
            choice_mode = input()
            print('')

            if choice_mode == "1":
                self.game_settings.against_computer()
            elif choice_mode == "2":
                self.game_settings.against_player()
            elif choice_mode == "3":
                break
            else:
                print("Invalid value. Please try again")

    def show_game_rules(self):
        """
        Prints the rules of the game to the console.
        """
        print('''
        Each turn, a player repeatedly rolls a die until
        either a 1 is rolled or the player decides to "hold":
        If the player rolls a 1, they score nothing and
        it becomes the next player's turn.
        If the player rolls any other number, it is added
        to their turn total and the player's turn continues.
        If a player chooses to "hold", their turn total is
        added to their score, and it becomes the next player's turn.
        The first player to score 100 or more points wins.
        ''')

    def show_scores(self):
        """
        Displays the score menu, allowing users to view high scores or search
        for a player's scores.
        """
        while True:
            print('Choose the list you want to check, numbers only')
            print('1. PvC high score ranking')
            print('2. PvP high score ranking')
            print("3. Search for player's record")
            print('4. Back')
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
                print("Invalid value. Please try again")

    def search_record(self):
        """
        Allows searching for a player's score record by name and offers the
        option to change the player's name.
        """
        print("Enter the player name you want to search for:")
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
        print("Press 'c' to change name, press 'q' to go back")
        choice = input().lower()
        print('')
        if choice == "c":
            if pvc_player_exists and pvp_player_exists:
                while True:
                    print('In which mode do you want to change your name?')
                    print('1. PvC')
                    print('2. PvP')
                    print('3. Back')
                    print('Enter number only')
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
                        print('Invalid value, please try again')
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

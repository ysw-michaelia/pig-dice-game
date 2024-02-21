from game import Game
from difficulty import Difficulty
from player import Player
from scores import Scores

class Menu:
    """
    A menu showed when game starts. 
    Options are for choosing by entering corresponding numbers.
    """

    def menu_main(self):
        while True:
            print("Welcome to Pig. Please choose an option. Enter Numbers only")
            print("1. Start game")
            print("2. Game rules")
            print("3. Scores")
            print("4. Cheat")
            print("5. Exit")
            choice_menu = input()

            if choice_menu == "1":
                self.start_game()
            elif choice_menu == "2":
                self.show_game_rules()
            elif choice_menu == "3":
                self.show_scores()
            elif choice_menu == "4":
                self.cheat()
            elif choice_menu == "5":
                print("Thank you! See you next time!")
                break
            else:
                print("Invalid value. Please try again. Enter numbers only")

    def start_game(self):
        while True:
            print("Choose playing mode, numbers only:")
            print("1. Play against computer")
            print("2. Two players")
            print("3. Back")
            choice_mode = input()

            if choice_mode == "1":
                self.start_computer_game()
            elif choice_mode == "2":
                self.start_two_player_game()
            elif choice_mode == "3":
                break
            else:
                print("Invalid value. Please try again")
                
    def start_computer_game(self):
        #considering moving the method to game.py
        while True:
            print("Please choose difficulty, from 1 to 3")
            choice_difficulty = input()
            if choice_difficulty in {"1", "2", "3"}:
                diff = Difficulty()
                diff.difficulty_adjust(int(choice_difficulty))
                break
            else:
                print("Invalid value, please try again.")
        name = input("Your name is:")
        player1 = Player(name)
        computer = Player("Computer")
        game = Game(player1, computer)
        game.play_against_computer()

    def start_two_player_game(self):
        player_name1 = input('Player 1 please enter your name')
        player1 = Player(player_name1)
        player_name2 = input('Player 2 please enter your name')
        player2 = Player(player_name2)
        # Implement two-player game logic

    def show_game_rules(self):
        print('''
        Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold":
        If the player rolls a 1, they score nothing and it becomes the next player's turn.
        If the player rolls any other number, it is added to their turn total and the player's turn continues.
        If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.
        The first player to score 100 or more points wins.
        ''')

    def show_scores(self):
        scores = Scores()
        # Implement showing scores logic

    def cheat(self):
        # Implement cheat functionality

if __name__ == "__main__":
    menu = Menu()
    menu.menu_main()

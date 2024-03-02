from game import Game
from intelligence import Intelligence
from dice import Dice
from player import Player
from score import Score


class Menu:
    """
    A menu appears when game starts.
    Options are for choosing by entering corresponding numbers.
    """
    def __init__(self, score):
        self.score = score

    def menu_main(self):
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
        while True:
            print("Choose playing mode, numbers only:")
            print("1. Play against computer")
            print("2. Two players")
            print("3. Back")
            choice_mode = input()
            print('')

            if choice_mode == "1":
                self.against_computer_settings()
            elif choice_mode == "2":
                self.player_against_player_settings()
            elif choice_mode == "3":
                break
            else:
                print("Invalid value. Please try again")

    def against_computer_settings(self):
        print("Difficulty adjust")
        prob_difficulty = self.get_difficulty(1)
        stra_difficulty = self.get_difficulty(2)
        diff = Intelligence(int(prob_difficulty), int(stra_difficulty))
        dice = Dice(probability=diff.dice_probability())
        player1 = self.get_player_name(1)
        computer = Player("Computer")
        game = Game(player1, computer, dice, strategy=diff, mode="PvC")
        game.start_game()

    def player_against_player_settings(self):
        player1 = self.get_player_name("Player 1")
        player2 = self.get_player_name("Player 2")
        dice = Dice(probability=None)
        game = Game(player1, player2, dice, strategy=None, mode="PvP")
        game.start_game()

    def show_game_rules(self):
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

    def get_difficulty(self, message):
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

    def search_record(self):
        print("Enter the player name you want to search for:")
        name = input()
        print('')
        pvc_player_exists = self.score.get_player_pvc_scores(name)
        pvp_player_exists = self.score.get_player_pvp_scores(name)
        if pvc_player_exists or pvp_player_exists:
            self.change_username(name, pvc_player_exists, pvp_player_exists)

    def change_username(self, name, pvc_player_exists, pvp_player_exists):
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

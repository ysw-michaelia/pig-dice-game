from intelligence import Intelligence
from dice import Dice
from player import Player
from game import Game


class GameSettings:
    def __init__(self, score):
        self.score = score

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

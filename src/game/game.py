from dice import Dice
from player import Player


class Game:

    def __init__(self, player, target_score=100):
        self.player = player
        self.target_score = target_score
        self.dice = Dice()

    def play_against_computer(self, current_points=0, round_points=0):
        print('It is your turn, "roll" or "hold"')
        decision = input()
        if decision == "roll":
            result = self.dice.roll()
            if result == 1:
                print("You rolled a 1. Your turn is over.")
                current_points -= round_points
                round_points = 0
                self.play_computer_turn()
            else:
                round_points += result
                current_points += result
                print(f'You got {result}. Your total points: {current_points}')
                if current_points >= self.target_score:
                    print("Congratulations! You win!")
                else:
                    self.play_against_computer(current_points, round_points)
        elif decision == "hold":
            self.player.points += current_points
            print("You decided to hold.")
            print(f"Your total points: {self.player.points}")
            self.play_computer_turn()
        else:
            print("Invalid decision. Please enter 'roll' or 'hold'.")
            self.play_against_computer(current_points)

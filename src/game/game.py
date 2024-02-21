from dice import Dice


class Game:
    def __init__(self, player1, player2, mode, target_score=100):
        self.player1 = player1
        self.player2 = player2
        self.mode = mode
        self.target_score = target_score
        self.dice = Dice()

    def play_mode(self):
        # a way to switch between two modes
        if self.mode == 'PvC':
            self.play_against_computer()
        elif self.mode == 'PvP':
            self.play_against_player()
        else:
            print("Invalid game mode.")

    def play_against_computer(self):
        # need to change it to be suitable for both PvE and PvP
        print('It is your turn, "roll" or "hold"')
        decision = input()
        if decision == "roll":
            result = self.dice.roll()
            if result == 1:
                print("You rolled a 1. Your turn is over.")
                self.player1.reset_round_points()
                self.player1.current_points_adjust()
                # self.play_computer_turn()
            else:
                self.player1.add_round_points(result)
                curr_points = self.player1.current_points(result)
                print(f'You got {result}. Your total points: {curr_points}')
                if curr_points >= self.target_score:
                    print("Congratulations! You win!")
                else:
                    self.play_against_computer(curr_points)
        elif decision == "hold":
            curr_points = self.player1.current_points(0)
            self.player1.reset_round_points()
            print("You decided to hold.")
            print(f"Your total points: {curr_points}")
            # self.play_computer_turn()
        else:
            print("Invalid decision. Please enter 'roll' or 'hold'.")
            self.play_against_computer()

    def computer_turn(self):
        print("Computer's turn")
        round_points = 0
        while round_points < 20:
            result = self.dice.roll()
            if result == 1:
                print("Computer rolled a 1. Its turn is over.")
                self.computer.reset_round_points()
                self.computer.current_points_adjust()
                break
            else:
                self.computer.add_round_points(result)
                curr_points = self.computer.current_points(result)
                print(f'Computer got {result}.')
                print('Its total points: {curr_points}')
                if curr_points >= self.target_score:
                    print("Computer wins!")
                    break
        else:
            print("Computer decides to hold.")
            curr_points = self.computer.current_points(0)
            self.computer.reset_round_points()
            print(f"Computer's total points: {curr_points}")

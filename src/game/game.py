from dice import Dice


class Game:
    def __init__(self, player1, player2, computer, mode, target_score=100):
        self.players = [player1, player2]
        self.computer = computer
        self.mode = mode
        self.target_score = target_score
        self.current_player_index = 0
        self.dice = Dice()

    def play_mode(self):
        # a way to switch between two modes
        while not self.game_over:
            if self.mode == 'PvC':
                self.dice_game()
                if not self.game_over:
                    self.computer_turn()
            elif self.mode == 'PvP':
                print(f"It is {self.players[self.current_player_index].name}'s turn")
                self.dice_game()

    def end_game(self):
        self.game_over = True

    def end_turn(self):
        self.current_player_index = (self.current_player_index + 1) % 2

    def dice_game(self):
        # need to change it to be suitable for both PvE and PvP
        current_player = self.players[self.current_player_index]
        print('"roll", "hold" or "exit"')
        decision = input()
        if decision.lower() == "roll":
            result = self.dice.roll()
            if result == 1:
                print(f"{self.players[self.current_player_index].name} rolled a 1. Your turn is over.")
                current_player.reset_round_points()
                current_player.current_points_adjust()
                if self.mode == "PvP":
                    self.end_turn()
            else:
                current_player.add_round_points(result)
                curr_points = current_player.current_points(result)
                print(f'You got {result}. Your total points: {curr_points}')
                if curr_points >= self.target_score:
                    print(f"Congratulations! {self.players[self.current_player_index].name} win!")
                    self.end_game()
        elif decision.lower() == "hold":
            curr_points = current_player.current_points(0)
            current_player.reset_round_points()
            print(f"{self.players[self.current_player_index].name} decided to hold.")
            print(f"{self.players[self.current_player_index].name} total points: {curr_points}")
            if self.mode == "PvP":
                self.end_turn()
        elif decision.lower() == "Exit":
            print('Feel free to join again! :)')
            self.end_game()
        else:
            print("Invalid decision. Please enter 'roll', 'hold' or 'exit'.")

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

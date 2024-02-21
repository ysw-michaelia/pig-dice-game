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

    def dice_game(self):
        current_player = self.players[self.current_player_index]
        print('"roll", "hold" or "exit"')
        decision = input().lower()
        if decision == "roll":
            self.roll_dice(current_player)
        elif decision == "hold":
            self.hold(current_player)
        elif decision == "exit":
            print('Feel free to join again! :)')
            self.end_game()
        else:
            print("Invalid decision. Please enter 'roll', 'hold' or 'exit'.")
   
    def roll_dice(self, player):
        result = self.dice.roll()
        if result == 1:
            print(f"{player.name} rolled a 1. Your turn is over.")
            player.current_points_adjust()
            player.reset_round_points()
            if self.mode == "PvP":
                self.end_turn()
        else:
            player.add_round_points(result)
            curr_points = player.current_points(result)
            print(f'{player.name} got {result}. Total points: {curr_points}')
            if curr_points >= self.target_score:
                print(f"Congratulations! {player.name} wins!")
                self.end_game()

    def hold(self, player):
        curr_points = player.current_points(0)
        player.reset_round_points()
        print(f"{player.name} decided to hold.")
        print(f"{player.name} total points: {curr_points}")
        if self.mode == "PvP":
            self.end_turn()

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

    def end_game(self):
        self.game_over = True

    def end_turn(self):
        self.current_player_index = (self.current_player_index + 1) % 2
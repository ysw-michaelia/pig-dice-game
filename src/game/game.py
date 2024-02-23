class Game:
    def __init__(self, player1, player2, dice, strategy):
        self.players = [player1, player2]
        self.dice = dice
        self.strategy = strategy
        self.target_score = 100
        self.current_player_index = 0
        self.game_over = False

    def play_game(self):
        while not self.game_over:
            print(f"{self.players[self.current_player_index].name}'s turn")
            self.dice_game()

    def dice_game(self):
        current_player = self.players[self.current_player_index]
        if self.players[self.current_player_index].name == 'Computer':
            action = current_player.strategy
            if action == "roll":
                self.roll_dice(current_player)
            else:
                self.hold(current_player)
        else:
            print('"roll"(r), "hold"(h) or "exit"(q)')
            decision = input().lower()
            if decision.lower() == "roll" or "r":
                self.roll_dice(current_player)
            elif decision.lower() == "hold" or "h":
                self.hold(current_player)
            elif decision.lower == "exit" or "q":
                print('Feel free to join again! :)')
                self.end_game()
            else:
                print("Invalid decision.")
                print("Try 'roll', 'hold' or 'exit'")
                print("or corresponding short cut: r, h or q.")

    def roll_dice(self, player):
        result = self.dice.roll()
        if result == 1:
            print(f"{player.name} rolled a 1. Your turn is over.")
            player.current_points_adjust()
            player.reset_round_points()
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
        self.end_turn()

    def end_game(self):
        self.game_over = True

    def end_turn(self):
        self.current_player_index = (self.current_player_index + 1) % 2

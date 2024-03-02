import time
from score import Score


class Game:
    def __init__(self, player1, player2, dice, strategy, mode):
        self.players = [player1, player2]
        self.dice = dice
        self.strategy = strategy
        self.mode = mode
        self.target_score = 100
        self.current_player_index = 0
        self.game_over = False

    def start_game(self):
        while not self.game_over:
            print(f"{self.players[self.current_player_index].name}'s turn")
            self.take_turns()

    def take_turns(self):
        current_player = self.players[self.current_player_index]
        if current_player.name == 'Computer':
            self.computer_round(current_player)
        else:
            self.player_round(current_player)

    def computer_round(self, current_player):
        round_points = current_player.add_round_points(0)
        if self.strategy.choose_action(round_points) == "roll":
            self.roll_dice(current_player)
            print('')
        else:
            self.hold(current_player)
            print('')

    def player_round(self, current_player):
        print('"roll"(r), "hold"(h), cheat(c) or "exit"(q)')
        decision = input().lower()
        if decision.lower() == "roll" or decision.lower() == "r":
            self.roll_dice(current_player)
        elif decision.lower() == "hold" or decision.lower() == "h":
            self.hold(current_player)
        elif decision.lower == "cheat" or decision.lower() == "c":
            self.cheat(current_player, cheat=1000)
        elif decision.lower == "exit" or decision.lower() == "q":
            print('Feel free to join again! :)')
            print('')
            self.end_game()
        else:
            print("Invalid decision.")
            print("Try 'roll', 'hold' or 'exit'")
            print("or corresponding short cut: r, h or q.")
            print('')

    def roll_dice(self, player):
        print(f'{player.name} decided to roll.')
        time.sleep(1)
        result = self.dice.roll()
        if result == 1:
            print(f"{player.name} rolled a 1. Your turn is over.")
            print('')
            time.sleep(1)
            player.current_points_adjust()
            player.reset_round_points()
            self.end_turn()
        else:
            player.add_round_points(result)
            curr_points = player.current_points(result)
            print(f'{player.name} got {result}. Total points: {curr_points}')
            print('')
            time.sleep(1)
            if curr_points >= self.target_score:
                print(f"Congratulations! {player.name} wins!")
                print('')
                self.high_score_list_checking(player.name, curr_points)
                self.end_game()

    def hold(self, player):
        curr_points = player.current_points(0)
        player.reset_round_points()
        print(f"{player.name} decided to hold.")
        time.sleep(1)
        print(f"{player.name} total points: {curr_points}")
        print('')
        time.sleep(1)
        self.end_turn()

    def cheat(self, player, cheat):
        cheat_points = player.current_points_adjust(cheat)
        print(f'{player.name} got {cheat}. Total points: {cheat_points}')
        print(f"Congratulations! {player.name} wins!")
        print('')
        self.end_game()

    def high_score_list_checking(self, name, points):
        score = Score()
        if self.mode == "PvC" and name != "Computer":
            score.pvc_new_record(name, points)
        elif self.mode == "PvP":
            score.pvp_new_record(name, points)

    def end_game(self):
        self.game_over = True

    def end_turn(self):
        self.current_player_index = (self.current_player_index + 1) % 2

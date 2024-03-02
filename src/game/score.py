import json


class Score:
    pvc_high_scores = {}
    pvp_high_scores = {}

    @staticmethod
    def save_scores():
        data = {
            'pvc_high_scores': Score.pvc_high_scores,
            'pvp_high_scores': Score.pvp_high_scores
        }
        with open('scores.json', 'w') as file:
            json.dump(data, file)

    @staticmethod
    def load_scores():
        try:
            with open('scores.json', 'r') as file:
                scores = json.load(file)
                Score.pvc_high_scores = scores.get('pvc_high_scores', {})
                Score.pvp_high_scores = scores.get('pvp_high_scores', {})
        except FileNotFoundError:
            pass

    def pvc_new_record(self, player_name, score):
        self.pvc_high_scores[player_name] = [score]

    def pvc_has_player(self, player_name):
        return player_name in self.pvc_high_scores

    def pvp_new_record(self, player_name, score):
        self.pvp_high_scores[player_name] = [score]

    def pvp_has_player(self, player_name):
        return player_name in self.pvp_high_scores

    def print_top_ten(self, mode):
        if mode == "PvC":
            self.print_top_scores("PvC", self.pvc_high_scores)
        elif mode == "PvP":
            self.print_top_scores("PvP", self.pvp_high_scores)

    def print_top_scores(self, mode, high_scores):
        if not high_scores:
            print(f"{mode} Top Ten High Scores:")
            print("No record")
            return

        sorted_scores = sorted(
            high_scores.items(),
            key=lambda x: sum(x[1]),
            reverse=True
        )
        print(f"{mode} Top Ten High Scores:")
        for i, (player_name, scores) in enumerate(sorted_scores[:10], start=1):
            total_score = sum(scores)
            print(f"{i}. {player_name}: {total_score}")

    def get_player_pvc_scores(self, player_name):
        if player_name in self.pvc_high_scores:
            scores = self.pvc_high_scores[player_name]
            print(f"Scores for {player_name} in PvC: {scores}")
            return True
        else:
            print("Name does not exist in PvC")
            return False

    def get_player_pvp_scores(self, player_name):
        if player_name in self.pvp_high_scores:
            scores = self.pvp_high_scores[player_name]
            print(f"Scores for {player_name} in PvP: {scores}")
            return True
        else:
            print("Name does not exist in PvP")
            return False

    def update_player_name(self, old_name, message):
        mode = "PvC" if message == 1 else "PvP"
        if mode == "PvC":
            high_scores = self.pvc_high_scores
        else:
            high_scores = self.pvp_high_scores

        while True:
            new_name = input("Your new name is:")
            if old_name in high_scores:
                if new_name not in high_scores:
                    high_scores[new_name] = high_scores.pop(old_name)
                    break
                else:
                    print(f'Name is already taken in {mode} list, try a new one')

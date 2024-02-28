class Scores:
    def __init__(self):
        self.high_scores = {}

    def add_score(self, player_name, score):
        if player_name in self.high_scores:
            self.high_scores[player_name].append(score)
        else:
            self.high_scores[player_name] = [score]

    def get_high_scores(self, player_name=None):
        if player_name:
            return self.high_scores.get(player_name, [])
        else:
            return self.high_scores

    def update_player_name(self, old_name, new_name):
        if old_name in self.high_scores:
            self.high_scores[new_name] = self.high_scores.pop(old_name)

    def __str__(self):
        return str(self.high_scores)

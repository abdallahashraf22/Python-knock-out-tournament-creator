import random
from metadata.match import Match

class Round:
    def __init__(self, list_of_players):
        self.players = list_of_players

    def get_round_matches(self):
        if all(player.got_a_bye for player in self.players):
            self.reset_byes()
        self.matches = []
        how_many_matches = len(self.players) // 2 
        if len(self.players) % 2 == 1:
            bye_player_index = random.randrange(len(self.players))
            while self.players[bye_player_index].got_a_bye is True:
                bye_player_index = random.randrange(len(self.players))
            self.matches.append(Match(self.players.pop(bye_player_index), None))
        for i in range(how_many_matches):
            player_one_index = random.randrange(len(self.players))
            player_one = self.players.pop(player_one_index)
            player_two_index = random.randrange(len(self.players))
            player_two = self.players.pop(player_two_index)
            self.matches.append(Match(player_one, player_two))
        return self.matches, self.get_remaining_players()
    
    def get_remaining_players(self):
        self.players = []
        for match in self.matches:
            self.players.append(match.get_winner())
        return self.players
    
    def reset_byes(self):
        for player in self.players:
            player.got_a_bye = False
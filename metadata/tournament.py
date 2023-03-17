import csv

from metadata.round import Round
from metadata.player import Player


class Tournament:
    def __init__(self, file_path):
        self.players = []
        with open(file_path, newline='') as csvfile:
            something = csv.DictReader(csvfile)
            list_of_teams = list(something)
        for team in list_of_teams:
            self.players.append(Player(team["Name"]))

    def start_tournament(self):
        i = 0
        while len(self.players) > 1:
            i += 1
            the_round = Round(self.players)
            matches, self.players = the_round.get_round_matches()
            print(f"round {i}: {matches}")
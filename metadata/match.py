import string
import random
from metadata.player import Player

class Match:
    alphatbet = string.ascii_lowercase
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    taken_matches = []

    def __init__(self, player_one, player_two):
        self.right = player_one
        self.left = player_two
        self.name = self.get_random_match_name()

    def get_winner(self):
        try:
            if self.right.got_a_bye or self.left.got_a_bye:
                return Player(f'winner of {self.name}', True)
        except AttributeError:
                return Player(f'winner of {self.name}', True)
        return Player(f'winner of {self.name}')
    
    def __repr__(self):
        if self.left is None:
            return f'{self.name}: {self.right} gets a bye'
        return f'{self.name}: {self.right} vs {self.left}'
    
    @classmethod
    def get_random_match_name(cls):
        name = random.choice(cls.alphatbet) + random.choice(cls.numbers)
        while name in cls.taken_matches:
            name = random.choice(cls.alphatbet) + random.choice(cls.numbers)
        cls.taken_matches.append(name)
        return name
    
    @classmethod
    def reset_matches(cls):
        cls.taken_matches = []

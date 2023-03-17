class Player:
    def __init__(self, name, got_a_bye = False):
        self.name = name
        self.got_a_bye = got_a_bye

    def __repr__(self):
        return f"{self.name}"
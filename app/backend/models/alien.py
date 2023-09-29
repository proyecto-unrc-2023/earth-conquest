from enum import Enum


class Alien:
    _id_counter = 0

    def __init__(self, team):
        Alien._id_counter += 1
        self.id = Alien._id_counter
        self.eyes = 1
        self.team = team

    def __str__(self):
        if self.team == Team.BLUE:
            return 'BLUE'
        else:
            return 'GREEN'

    def add_eyes(self, new_eyes):
        if (new_eyes > 5) or (self.eyes + new_eyes > 5):
            del self
        else:
            self.eyes += new_eyes


class Team(Enum):
    BLUE = 1
    GREEN = 2

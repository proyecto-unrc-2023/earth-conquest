from enum import Enum

from app.backend.models.team import Team


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

    """
    Given an amount of eyes, this method adds it to the
    current amount.
    """
    def add_eyes(self, new_eyes):
        if (new_eyes > 5) or (self.eyes + new_eyes > 5):
            del self
        else:
            self.eyes += new_eyes

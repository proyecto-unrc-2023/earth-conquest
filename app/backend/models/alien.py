from marshmallow import Schema, fields

from app.backend.models.team import Team


class Alien:
    _id_counter = 0

    def __init__(self, team, eyes=1):
        Alien._id_counter += 1
        self.id = Alien._id_counter
        self.eyes = eyes
        self.team = team

    def __str__(self):
        if self.team == Team.BLUE:
            return 'B:'+self.eyes.__str__()
        else:
            return 'G:'+self.eyes.__str__()

    """
    Given an amount of eyes, this method adds it to the
    current amount.
    """

    def add_eyes(self, new_eyes):
        if (new_eyes > 5) or (self.eyes + new_eyes > 5):
            del self
        else:
            self.eyes += new_eyes


class AlienSchema(Schema):
    id = fields.Integer()
    eyes = fields.Integer()
    team = fields.Enum(Team)

from marshmallow import Schema, fields

from app.backend.models.direction import Direction


class Directioner:
    """
    Directioners occupy three Cells, init_pos represents the position of the first
    Cell it ocuppies. snd_pos represents the second cell it ocuppies and same with
    the thrd_col
    """

    def __init__(self, init_pos=(0, 0), direction=Direction.RIGHT):
        self.direction = direction
        self.init_pos = init_pos
        self.snd_pos = None
        self.thrd_pos = None
        # on the third position, the alien will move to the last cell in the directioner's direction
        self.last_pos = None
        self.calculate_snd_position()
        self.calculate_thrd_position()
        self.calculate_last_position()

    def calculate_snd_position(self):
        if self.direction == Direction.RIGHT:
            self.snd_pos = (self.init_pos[0], self.init_pos[1] + 1)
        elif self.direction == Direction.LEFT:
            self.snd_pos = (self.init_pos[0], self.init_pos[1] - 1)
        elif self.direction == Direction.UPWARDS:
            self.snd_pos = (self.init_pos[0] - 1, self.init_pos[1])
        else:
            self.snd_pos = (self.init_pos[0] + 1, self.init_pos[1])

    def calculate_thrd_position(self):
        if self.direction == Direction.RIGHT:
            self.thrd_pos = (self.init_pos[0], self.init_pos[1] + 2)
        elif self.direction == Direction.LEFT:
            self.thrd_pos = (self.init_pos[0], self.init_pos[1] - 2)
        elif self.direction == Direction.UPWARDS:
            self.thrd_pos = (self.init_pos[0] - 2, self.init_pos[1])
        else:
            self.thrd_pos = (self.init_pos[0] + 2, self.init_pos[1])

    def calculate_last_position(self):
        if self.direction == Direction.RIGHT:
            self.last_pos = (self.init_pos[0], self.init_pos[1] + 3)
        elif self.direction == Direction.LEFT:
            self.last_pos = (self.init_pos[0], self.init_pos[1] - 3)
        elif self.direction == Direction.UPWARDS:
            self.last_pos = (self.init_pos[0] - 3, self.init_pos[1])
        else:
            self.last_pos = (self.init_pos[0] + 3, self.init_pos[1])


class DirectionerSchema(Schema):
    name = fields.Str(default="DIRECTIONER")
    init_pos = fields.Tuple((fields.Integer(), fields.Integer()))
    last_pos = fields.Tuple((fields.Integer(), fields.Integer()))
    direction = fields.Enum(Direction)

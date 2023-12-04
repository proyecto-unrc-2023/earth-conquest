from marshmallow import Schema, fields


class Teleporter:

    def __init__(self, door_pos=None, exit_pos=None):
        self.door_pos = door_pos
        self.exit_pos = exit_pos


class TeleporterSchema(Schema):
    name = fields.Str(default ="TELEPORTER")
    door_pos = fields.Tuple((fields.Integer(), fields.Integer()))
    exit_pos = fields.Tuple((fields.Integer(), fields.Integer()))

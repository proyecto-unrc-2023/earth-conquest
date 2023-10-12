import random

from marshmallow import Schema, fields

from app.backend.models import team
from app.backend.models.game_enum import TGame
from app.backend.models.alien import Alien
from app.backend.models.board import Board, BoardSchema
from app import db

INIT_CREW = 6


class Game(db.Model):

    def __init__(self):
        #id = db.Column(db.Integer, primary_key=True)
        self.status = TGame.NOT_STARTED
        self.green_player = None
        self.blue_player = None
        self.board = Board()

    def join_as_green(self, name):
        if self.green_player is not None:
            raise Exception("Player green is already taken")
        self.green_player = name

    def join_as_blue(self, name):
        if self.blue_player is not None:
            raise Exception("Player blue is already taken")
        self.blue_player = name

    def set_board_dimensions(self, rows, cols):
        if rows < 4 or rows > 25 or cols < 6 or cols > 45:
            raise Exception("Invalid dimensions. Minimum board is 4x6. Max is 25x45")
        self.board = Board(rows, cols, round((rows*cols*0.1)**0.5))   # raiz cuadrada del 10% del area de la matriz

    def start_game(self):
        self.set_initial_crew()
        self.status = TGame.STARTED

    def set_initial_crew(self):
        for i in range(INIT_CREW):
            self.add_alien_to_range(team.Team.BLUE)
            self.add_alien_to_range(team.Team.GREEN)

    def add_alien_to_range(self, t):
        if t == team.Team.GREEN:
            x0, y0 = self.board.green_ovni_range
            f = random.randint(0, x0)
            c = random.randint(0, y0)

        elif t == team.Team.BLUE:
            x0, y0 = self.board.blue_ovni_range
            f = random.randint(x0, self.board.rows - 1)
            c = random.randint(y0, self.board.cols - 1)

        else:
            raise Exception("Invalid team")

        if self.board.aliens.__contains__((f, c)):
            self.add_alien_to_range(t)
        else:
            alien = Alien(t)
            self.board.set_alien(f, c, alien)

    def refresh_board(self):
        if not self.board:
            raise Exception("No board created")
        self.board.refresh_board()

    def act_board(self):
        if not self.board:
            raise Exception("No board created")
        self.board.act_board()

    def has_game_ended(self):
        return self.board.green_ovni == 0 or self.board.blue_ovni == 0

    """
    ends the game if some player want to leave
    """
    def end_game(self):
        print('Game ended')
        self.blue_player = None
        self.green_player = None

    def set_alterator(self, alterator, x, y):
        try:
            self.board.set_alterator(alterator, x, y)
        except Exception:
            print("Invalid cell selected. Can not place an alterator there")


class GameSchema(Schema):
    status = fields.Enum(TGame)
    green_player = fields.Str(required=False)
    blue_player = fields.Str(required=False)
    board = fields.Str()#Nested(lambda: BoardSchema, only=('board',))

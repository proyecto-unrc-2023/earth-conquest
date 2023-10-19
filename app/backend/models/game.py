import random

from marshmallow import Schema, fields

from app.backend.models import team
from app.backend.models.alterator import Alterator
from app.backend.models.directioner import Directioner
from app.backend.models.game_enum import TGame
from app.backend.models.alien import Alien
from app.backend.models.board import Board
from app.backend.models.team import Team
from app.backend.models.teleporter import Teleporter

INIT_CREW = 6


class Game:

    def __init__(self):
        self.status = TGame.NOT_STARTED
        self.green_player = None
        self.blue_player = None
        self.board = Board()
        self.winner = (None, None)  # (Player name, TEAM)

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
        self.board = Board(rows, cols, round((rows * cols * 0.1) ** 0.5))  # raiz cuadrada del 10% del area de la matriz

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
        res = self.board.act_board()
        if res is not None:
            self.status = TGame.OVER
            self.winner = (self.green_player, Team.GREEN) if res == Team.GREEN else (self.blue_player, Team.BLUE)

    def has_game_ended(self):
        return self.board.green_ovni_life <= 0 or self.board.blue_ovni_life <= 0

    """
    ends the game if some player want to leave
    """

    def end_game(self):
        print('Game ended')
        self.blue_player = None
        self.green_player = None

    def set_alterator(self, alterator, team, x=None, y=None):

        if isinstance(alterator, Directioner):
            if self.board.kill_aliens(team, 4):
                self.board.set_directioner(alterator)
            else:
                raise Exception("not enough aliens to put a Directioner")

        if isinstance(alterator, Teleporter):
            if self.board.kill_aliens(team, 6):
                self.board.set_teleporter(alterator)
            else:
                raise Exception("not enough aliens to put a Teleporter")

        if alterator is Alterator.TRAP:
            if self.board.kill_aliens(team, 4):
                self.board.set_trap(x, y)
            else:
                raise Exception("not enough aliens to put a TRAP")

    def get_team_winner(self):
        return self.winner[1]

    def get_alien_position(self, alien):
        return self.board.get_alien_position(alien)

    def remove_alien(self, x, y, alien):
        return self.board.remove_alien_from_board(x, y, alien)

    def set_alien(self, x, y, alien):
        return self.board.set_alien(x, y, alien)

    def aliens_dict(self):
        return self.board.aliens

    def get_board_rows(self):
        return self.board.rows

    def get_board_cols(self):
        return self.board.cols

    def is_position_in_blue_range(self, x, y):
        return self.board.is_position_in_blue_range(x, y)

    def is_position_in_green_range(self, x, y):
        return self.board.is_position_in_green_range(x, y)

    def is_pos_on_any_range(self, x, y):
        return self.board.is_pos_on_any_range(x, y)

    def is_free_position(self, x, y):
        return self.board.is_free_position(x, y)

    def get_base_range_dimentions(self):
        return self.board.base_range_dimentions

    def get_green_ovni_range(self):
        return self.board.green_ovni_range

    def get_blue_ovni_range(self):
        return self.board.blue_ovni_range

    def json(self):
        return {
            'status': self.status,
            'green_player': self.green_player,
            'blue_player': self.blue_player,
            'board': self.board
        }


class GameSchema(Schema):
    status = fields.Str()
    green_player = fields.Str()
    blue_player = fields.Str()
    board = fields.List(fields.List(fields.List(fields.List(fields.Str()))))

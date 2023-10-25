import random

from marshmallow import Schema, fields

from app.backend.models import team
from app.backend.models.alterator import Alterator
from app.backend.models.directioner import Directioner
from app.backend.models.game_enum import TGame
from app.backend.models.alien import Alien
from app.backend.models.board import Board, BoardSchema
from app.backend.models.board import Board
from app.backend.models.modifier import Modifier
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
        self.green_alien_cant = 0
        self.blue_alien_cant = 0

    def join_as_green(self, name):
        if self.green_player is not None:
            raise Exception("Player green is already taken")
        if name == self.blue_player:
            raise Exception("This name is already taken")
        self.green_player = name

    def join_as_blue(self, name):
        if self.blue_player is not None:
            raise Exception("Player blue is already taken")
        if name == self.green_player:
            raise Exception("This name is already taken")
        self.blue_player = name

    def set_board_dimensions(self, rows, cols):
        if rows < 4 or rows > 25 or cols < 6 or cols > 45:
            raise Exception("Invalid dimensions. Minimum board is 4x6. Max is 25x45")
        self.board = Board(rows, cols, round((rows * cols * 0.1) ** 0.5))  # raiz cuadrada del 10% del area de la matriz

    def start_game(self):
        if (self.status is TGame.NOT_STARTED and
                self.blue_player is not None and
                self.green_player is not None):
            self.set_initial_crew()
            self.status = TGame.STARTED
        else:
            raise Exception("can not start the game, some player is left or game status is not NOT_STARTED")

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
            # Update cant of aliens
            if t == team.Team.GREEN:
                self.green_alien_cant += 1
            else:
                self.blue_alien_cant += 1

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

        # Updates cants of aliens
        self.green_alien_cant = self.board.get_aliens_cant_of_team(Team.GREEN)
        self.blue_alien_cant = self.board.get_aliens_cant_of_team(Team.BLUE)

    def has_game_ended(self):
        return self.board.green_ovni_life <= 0 or self.board.blue_ovni_life <= 0

    """
    ends the game if some player wants to leave
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

    '''
    This method sets a modifier on the given position if this one's free and valid.
    '''
    def set_modifier_in_position(self, modifier, x, y):
        self.board.set_modifier(modifier, x, y)


    '''
    This method gets the modifier that's on the given position
    '''
    def get_modifier_in_position(self, x, y):
        return self.board.get_modifier(x,y)
        #return self.board.get_cell(x,y).modifier




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

    def is_pos_within_board_range(self, x, y):
        return self.board.is_within_board_range(x, y)

    def get_cell(self, x, y):
        return self.board.get_cell(x, y)

    '''
    This method returns the team of a specific alien in the board.
    '''

    def get_alien_team_in_position(self, x, y, alien_pos_in_list):
        return self.board.get_alien_in_position(x, y, alien_pos_in_list).team

    def json(self):
        return {
            'status': self.status,
            'green_player': self.green_player,
            'blue_player': self.blue_player,
            'board': self.board
        }

    '''
    This method sets an alien on a given position of a respective team
    '''

    def create_an_alien_in_pos(self, x, y, team):
        alien = Alien(team)
        self.board.set_alien(x, y, alien)

    '''
    This method sets a specific ammount of aliens in a given position of a respective team
    '''

    def creates_aliens_in_pos(self, x, y, cant, team):
        for i in range(cant):
            self.board.set_alien(x, y, Alien(team))

    '''
    This method returns the number of aliens in a given position
    '''

    def get_num_aliens_in_position(self, x, y):
        return self.board.get_num_aliens_in_position(x, y)

    '''
    This method returns the alien in a given position
    '''

    def get_alien_in_position(self, x, y, index):
        return self.board.get_alien_in_position(x, y, index)

    '''
    This method returns the number of eyes of a specific alien in the board
    '''

    def get_alien_eyes_in_position(self, x, y, alien_pos_in_list):
        return self.board.get_alien_in_position(x, y, alien_pos_in_list).eyes

    '''
    This method adds eyes to a specific alien in the board
    '''

    def add_eyes_to_alien(self, x, y, alien_pos_in_list, eyes):
        self.board.get_alien_in_position(x, y, alien_pos_in_list).add_eyes(eyes)

    '''
    This method returns the aliens list in a given position
    '''

    def get_aliens_in_pos(self, x, y):
        return self.board.get_cell(x, y).aliens

    '''
    This method returns True if an ovni has been destroyed
    '''

    def any_ovni_destroyed(self):
        return self.board.any_ovni_destroyed()


class GameSchema(Schema):
    id = fields.Integer()
    status = fields.Enum(TGame)
    green_player = fields.Str()
    blue_player = fields.Str()
    board = fields.Nested(BoardSchema(), only=('board',))
    green_alien_cant = fields.Integer()
    blue_alien_cant = fields.Integer()
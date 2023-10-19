import random

from marshmallow import Schema, fields
from sql import SQL

from app.backend.models import team
from app.backend.models.game_enum import TGame
from app.backend.models.alien import Alien
from app.backend.models.board import Board
from app.backend.models.team import Team

INIT_CREW = 6


class Game(SQL):

    def __init__(self):
        self.status = TGame.NOT_STARTED
        self.green_player = None
        self.blue_player = None
        self.board = Board()
        self.winner = (None, None)          # (Player name, TEAM)

    def join_as_green(self):
        if self.green_player is not None:
            raise Exception("Player green is already taken")
        self.green_player = team.Team.GREEN

    def join_as_blue(self):
        if self.blue_player is not None:
            raise Exception("Player blue is already taken")
        self.blue_player = team.Team.BLUE

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

    def set_alterator(self, alterator, x, y):
        try:
            self.board.set_alterator(alterator, x, y)
        except Exception:
            print("Invalid cell selected. Can not place an alterator there")

    def get_team_winner(self):
        return self.winner[1]
    

    '''
    This method returns the team of a specific alien in the board.
    '''
    def __get_alien_team_in_position(self, x, y, alien_pos_in_list):
        return self.board.get_alien_in_position(x, y, alien_pos_in_list).team
    



    def json(self):
        return {
            'status': self.status,
            'green_player': self.green_player,
            'blue_player': self.blue_player,
            'board': self.board
        }
       
    '''
    This method set an alien in a given position of respective team
    '''   
    def create_an_alien_in_pos(self, x, y, team):
        alien = Alien(team)
        self.board.set_alien(x, y, alien)
        
    '''
    This method sets an alien in a given position of respective team
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
    This method returns the number of aliens in the board
    '''
    def get_num_aliens_in_board(self):
        return self.board.get_num_aliens_in_board()
    
    
    '''
    This method returns the number eyes on specific alien in the board
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
    
    '''
    def any_ovni_destroyed(self):
        return self.board.any_ovni_destroyed()


class GameSchema(Schema):
    status = fields.Str()
    green_player = fields.Str()
    blue_player = fields.Str()
    board = fields.List(fields.List(fields.List(fields.List(fields.Str()))))

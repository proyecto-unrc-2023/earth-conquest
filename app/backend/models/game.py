import random

from app.backend.models import team
from app.backend.models.game_enum import TGame
from app.backend.models.alien import Alien
from app.backend.models.board import Board

INIT_CREW = 6


class Game:   # que herede de (SQL) para tener los metodos get , etc, gratis
    
    def __init__(self):
        self.status = TGame.NOT_STARTED
        self.green_player = None
        self.blue_player = None
        self.board = Board(10, 15, 4)
    
    def __init__(self, rows: int, cols: int):
        self.status = TGame.NOT_STARTED
        self.green_player = None
        self.blue_player = None
        self.board = Board(rows, cols, 4)

    def join_as_green(self):
        if self.green_player is not None:
            raise Exception("Player green is already taken")
        self.green_player = team.Team.GREEN

    def join_as_blue(self):
        if self.blue_player is not None:
            raise Exception("Player blue is already taken")
        self.blue_player = team.Team.BLUE

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

    def set_alterator(self, x, y, alterator):
        try:
            self.board.set_alterator(x, y, alterator)
        except Exception:
            print("Invalid cell selected. Can not place a alterator there")

    # TODO implementar cuando un alien pisa el rango de las naves

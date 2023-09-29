import random

from app.backend.models.game_enum import TGame
from app.backend.models.team import TTeam
from app.backend.models.alien import Alien
from app.backend.models.board import Board

INIT_CREW = 6


class Game:   # que herede de (SQL) para tener los metodos get , etc, gratis

    def __init__(self):
        self.status = TGame.NOT_STARTED
        self.green_player = None
        self.blue_player = None
        self.board = Board(10, 15, round(150/6))

    def __init__(self, rows: int, cols: int):
        self.status = TGame.NOT_STARTED
        self.green_player = None
        self.blue_player = None
        self.board = Board(rows, cols, round(rows*cols)/6)

    def join_as_green(self):
        if self.green_player is not None:
            raise Exception("Player green is already taken")
        self.green_player = TTeam.GREEN

    def join_as_blue(self):
        if self.blue_player is not None:
            raise Exception("Player blue is already taken")
        self.blue_player = TTeam.BLUE

    def set_initial_crew(self):
        for i in range(INIT_CREW):
            self.add_alien_to_range(TTeam.BLUE)
            self.add_alien_to_range(TTeam.GREEN)

    def add_alien_to_range(self, team):
        if team == TTeam.GREEN:
            green_range = self.board.green_ovni_range[0]  # taking first of tuple
            f = random.randint(0, green_range)
            c = random.randint(0, green_range)

            # verify that it is not generating more than one alien in one random position
            while self.board.aliens.__contains__((f, c)):
                f = random.randint(0, green_range)
                c = random.randint(0, green_range)

            green_alien = Alien(TTeam.GREEN)
            self.board.set_alien(green_alien, f, c)

        elif team == TTeam.BLUE:
            blue_range = self.board.blue_ovni_range[0]  # taking first of tuple
            max_cols = self.board.cols
            f = random.randint(max_cols, blue_range)
            c = random.randint(15, blue_range)

            # verify that it is not generating more than one alien in one random position
            while self.board.aliens.__contains__((f, c)):
                f = random.randint(max_cols, blue_range)
                c = random.randint(max_cols, blue_range)

            blue_alien = Alien(TTeam.BLUE)
            self.board.set_alien(blue_alien, f, c)

        else:
            raise Exception("Invalid team")

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

import random

from models.TGame import TGame
from models.TTeam import TTeam
from models.board import Board

INIT_CREW = 6


class Game:

    def __init__(self):
        self.status = TGame.NOT_STARTED
        self.green_player = None
        self.blue_player = None
        self.board = Board(10, 15)
        self.blue_aliens = {}
        self.green_aliens = {}

    def __init__(self, rows: int, cols: int):
        self.status = TGame.NOT_STARTED
        self.green_player = None
        self.blue_player = None
        self.board = Board(rows, cols)
        self.blue_aliens = {}
        self.green_aliens = {}

    def join_as_green(self):
        if self.green_player is not None:
            raise Exception("Player green is already taken")
        self.green_player = TPlayer.UNDEFINED   # id here?

    def join_as_blue(self):
        if self.blue_player is not None:
            raise Exception("Player blue is already taken")
        self.blue_player = TPlayer.UNDEFINED

    def add_alien_to_board(self, team):
        if team == TTeam.GREEN:
            green_range = self.board.green_nave_range[0]  # taking first of tuple
            f = random.randint(0, green_range)
            c = random.randint(0, green_range)

            # verify that it is not generating more than one alien in one random position
            while self.green_aliens.__contains__((f, c)):
                f = random.randint(0, green_range)
                c = random.randint(0, green_range)

            green_alien = Alien(TTeam.GREEN)
            self.board.set_alien(green_alien, (f, c))
            return green_alien

        elif team == TTeam.BLUE:
            blue_range = self.board.blue_nave_range[0]  # taking first of tuple
            f = random.randint(15, blue_range)
            c = random.randint(15, blue_range)

            # verify that it is not generating more than one alien in one random position
            while self.blue_aliens.__contains__((f, c)):
                f = random.randint(15, blue_range)
                c = random.randint(15, blue_range)

            blue_alien = Alien(TTeam.BLUE)
            self.board.set_alien(blue_alien, (f, c))
            return blue_alien

        else:
            raise Exception("Invalid team")

    def set_initial_crew(self):

        for i in range(INIT_CREW):
            blue_alien = self.add_alien_to_board(TTeam.BLUE)
            green_alien = self.add_alien_to_board(TTeam.GREEN)

            self.blue_aliens["alien_id"] = blue_alien.id
            self.blue_aliens["alien_pos"] = blue_alien.pos
            self.green_aliens["alien_id"] = green_alien.id
            self.green_aliens["alien_pos"] = green_alien.pos

    def refresh_board(self):
        if not self.board:
            raise Exception("No board created")
        self.board.refresh()

    def act_board(self):
        if not self.board:
            raise Exception("No board created")
        new_board = self.board.act()
        self.board = new_board

    def has_game_ended(self):
        return self.board.green_nave == 0 or self.board.blue_nave == 0

    def end_game(self):
        """
        ends the game if some player want to leave
        """
        print('Game ended')
        self.blue_player = None
        self.green_player = None

    def add_modifier(self, alterator, cell):
        try:
            self.board.set_alterator(alterator, cell)
        except Exception as e:
            print("Invalid cell selected. Can not place a modifier there")

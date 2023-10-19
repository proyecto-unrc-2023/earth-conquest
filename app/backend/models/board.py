import random

from marshmallow import Schema, fields

from app.backend.models.alien import Alien
from app.backend.models.alterator import Alterator
from app.backend.models.cell import Cell, CellSchema
from app.backend.models.direction import Direction
from app.backend.models.modifier import Modifier
from app.backend.models.orientation import Orientation
from app.backend.models.mountain_range import MountainRange
from app.backend.models.directioner import Directioner
from app.backend.models.team import Team
from app.backend.models.teleporter import Teleporter

GREEN_OVNI_LIFE = 100
BLUE_OVNI_LIFE = 100


class Board:

    def __init__(self, rows=10, cols=15, base_range_dimentions=4):
        self.rows = rows
        self.cols = cols
        self.aliens = {}  # Dictionary with Key = position on the board, Value = list of aliens in that position
        self.base_range_dimentions = base_range_dimentions
        self.green_ovni_range = (base_range_dimentions - 1, base_range_dimentions - 1)
        self.blue_ovni_range = (rows - 1 - (base_range_dimentions - 1), cols - 1 - (base_range_dimentions - 1))
        self.board = []
        self.create_board()
        self.green_ovni_life = GREEN_OVNI_LIFE
        self.blue_ovni_life = BLUE_OVNI_LIFE

    """
    Creates the initial board full of Cells and
    default modifiers: MountainRange, Killer, Multiplier
    that are set outside the ovnis ranges.
    """

    def create_board(self):
        rows = self.rows
        cols = self.cols
        self.board = [[Cell() for _ in range(cols)] for _ in range(rows)]

        # Setting the default Modifiers in free random positions
        for i in range(2):
            # setting the mountain range on the board
            self.set_mountain_range_on_board()

            # setting a killer
            x, y = self.get_random_free_pos()
            self.get_cell(x, y).modifier = Modifier.KILLER

            # setting a multiplier
            x, y = self.get_random_free_pos()
            self.get_cell(x, y).modifier = Modifier.MULTIPLIER

    """
    This method sets a mountain range on the board with a random orientation and on a random, 
    valid and free position of the board.
    """

    def set_mountain_range_on_board(self):
        while True:
            x, y = self.get_random_free_pos()
            initial_position = (x, y)
            orientations = [Orientation.VERTICAL, Orientation.HORIZONTAL]
            mountain_list = MountainRange(initial_position, random.choice(orientations))

            are_all_pos_valid = True

            for pos in mountain_list.mountain:
                if not self.is_free_position(pos[0], pos[1]) or self.is_pos_on_any_range(pos[0], pos[1]):
                    are_all_pos_valid = False
                    break

            if are_all_pos_valid:
                for pos in mountain_list.mountain:
                    self.set_modifier(Modifier.MOUNTAIN_RANGE, pos[0], pos[1])
                break

    """
    Returns a free position of the board which it is not
    a modifier, nor an alterator or is in any ovnis ranges.
    """

    def get_random_free_pos(self):
        while True:  # se ejecuta infinitamente hasta que se le isntruccione salir del bucle
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.cols - 1)
            if self.is_free_position(x, y) and not self.is_pos_on_any_range(x, y):
                return x, y

    """
    Checks if a given position is within the board's perimeter
    """

    def is_within_board_range(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols

    """
    Returns True if he position is on the board range 
    and it's not a modifier or an alterator.
    """

    def is_free_position(self, x, y):
        if self.is_within_board_range(x, y):
            if self.get_cell(x, y).modifier is None and self.get_cell(x, y).alterator is None:
                return True
            else:
                return False
        else:
            return False

    """
    Returns True if the position is on any of the ranges of the ovnis
    """

    def is_pos_on_any_range(self, x, y):
        return self.is_position_in_blue_range(x, y) or self.is_position_in_green_range(x, y)

    """
    Returns True if the position is on the blue base range.
    """

    def is_position_in_blue_range(self, x, y):
        if self.blue_ovni_range[0] <= x < self.rows and self.blue_ovni_range[1] <= y < self.cols:
            return True
        else:
            return False

    """
    Returns True if the position is on the green base range.
    """

    def is_position_in_green_range(self, x, y):
        if 0 <= x <= self.green_ovni_range[0] and 0 <= y <= self.green_ovni_range[1]:
            return True
        else:
            return False

    """
    Returns the Cell that's at a specific position.
    """

    def get_cell(self, x, y):
        if 0 <= x < self.rows and 0 <= y < self.cols:
            return self.board[x][y]
        else:
            raise IndexError("Index out of range")

    """ 
    Sets a Trap on a specific Cell only if on that cell 
    there's no Modifier or Alterator already placed there.
    """

    def set_trap(self, x, y):
        if self.is_free_position(x, y) and not self.is_pos_on_any_range(x, y):
            self.get_cell(x, y).alterator = Alterator.TRAP
        else:
            raise ValueError("Position isn't free or valid")

    """ 
    Sets a Teleporter on two specific Cells (door and exit) only if on those 
    cells there's no Modifier or Alterator already placed there.
    """

    def set_teleporter(self, teleporter):
        door_row, door_col = teleporter.door_pos
        exit_row, exit_col = teleporter.exit_pos

        if (
                self.is_free_position(door_row, door_col)
                and self.is_free_position(exit_row, exit_col)
                and not self.is_pos_on_any_range(door_row, door_col)
                and not self.is_pos_on_any_range(exit_row, exit_col)
        ):
            self.get_cell(door_row, door_col).alterator = teleporter
            self.get_cell(exit_row, exit_col).alterator = teleporter
        else:
            raise ValueError("Positions of the teleporter aren't free or valid")

    """ 
    Sets a Directioner on three specific Cells only if on those 
    cells there's no Modifier or Alterator already placed there.
    """

    def set_directioner(self, directioner):
        positions = [
            directioner.init_pos,
            directioner.snd_pos,
            directioner.thrd_pos,
        ]

        for row, col in positions:
            if not (self.is_free_position(row, col) and not self.is_pos_on_any_range(row, col)):
                raise ValueError("Positions of the directioner aren't free or valid")

        for row, col in positions:
            self.get_cell(row, col).alterator = directioner

    """ 
    Sets a Modifier on a specific Cell only if on that cell 
    there's no Modifier or Alterator already placed there.
    """

    def set_modifier(self, modifier, x, y):
        if self.is_free_position(x, y):
            self.get_cell(x, y).modifier = modifier
        else:
            raise AttributeError("There's already a Modifier on that cell")

    """
    Method that sets an alien on the alive aliens dictionary.
    """

    def set_alien_in_dictionary(self, x, y, alien):
        position = (x, y)
        # if there's already aliens at that position
        if position in self.aliens:
            self.aliens[position].append(alien)  # we add it to the list of aliens
        else:
            self.aliens[position] = [alien]  # Key doesn't exist, create new list of aliens

    """ 
    Updates the board by moving each alien to a free random adjoining position.
    """

    def refresh_board(self):
        aliens_copy = dict(self.aliens)  # dictionary copy
        for key in aliens_copy:
            list_of_aliens = aliens_copy[key]  # list of aliens in that key
            for alien in list_of_aliens:
                x = key[0]
                y = key[1]
                self.move_alien(x, y, alien)

    """ 
    This method solves each fight and/or reproduction that may occur between aliens 
    on each cell. 
    It also solves any action that may occur between aliens and Alterators/Modifiers.
    """

    def act_board(self):
        for key in self.aliens:
            x = key[0]
            y = key[1]
            cell = self.get_cell(x, y)
            cell.action()  # only one alien will be left or just none after the action
            self.aliens[(x, y)] = cell.aliens
            if not cell.aliens == []:
                alien = cell.aliens[0]
                if (alien.team == Team.BLUE and self.is_position_in_green_range(x, y)
                        or alien.team == Team.GREEN and self.is_position_in_blue_range(x, y)):
                    self.alien_attack_ovni(x, y, alien)
                    if self.any_ovni_destroyed():
                        return alien.team

    """
    Moves an alien to a free random and adjacent position.
    x, y represent the position where the alien is currently placed at.
    It updates both the dictionary and board.
    """

    def move_alien(self, x, y, alien):
        alterator = self.get_cell(x, y).alterator  # alterator on the cell
        if isinstance(alterator, Teleporter):
            new_x, new_y = self.new_alien_pos_with_teleporter(x, y, alterator)
        elif isinstance(alterator, Directioner):
            new_x, new_y = self.new_alien_pos_with_directioner(x, y, alterator)
        else:
            new_x, new_y = self.get_adjoining_valid_pos(x, y)

        # updates the cell
        self.get_cell(x, y).remove_alien(alien)
        self.get_cell(new_x, new_y).add_alien(alien)

        # update the dictionary
        if (x, y) in self.aliens:
            self.aliens[(x, y)].remove(alien)
            self.set_alien_in_dictionary(new_x, new_y, alien)
        else:
            raise ValueError("The key provided does not have the alien on its list of aliens")

    """
    An alien is placed at a (x,y) position where a teleporter is placed.
    This method returns the position where the alien has to move to.
    """

    def new_alien_pos_with_teleporter(self, x, y, teleporter):
        if x == teleporter.door_pos[0] and y == teleporter.door_pos[1]:
            return teleporter.exit_pos
        else:
            return self.get_adjoining_valid_pos(x, y)

    """
    An alien is placed at a (x,y) position where a directioner is placed.
    This method returns the position where the alien has to move to.
    """

    def new_alien_pos_with_directioner(self, x, y, directioner):
        if x == directioner.init_pos[0] and y == directioner.init_pos[1]:
            return directioner.snd_pos
        if x == directioner.snd_pos[0] and y == directioner.snd_pos[1]:
            return directioner.thrd_pos
        if x == directioner.thrd_pos[0] and y == directioner.thrd_pos[1]:
            if self.can_alien_move_to_pos(directioner.last_pos[0], directioner.last_pos[1]):
                return directioner.last_pos
            else:
                if directioner.direction == Direction.LEFT or directioner.direction == Direction.RIGHT:
                    if self.can_alien_move_to_pos(x-1,y) or self.can_alien_move_to_pos(x-1,y):
                        # the alien will move to a random adjacent position that's not equal to the snd_pos
                        new_x, new_y = self.get_adjoining_valid_pos(x, y)
                        while (new_x == directioner.snd_pos[0] and new_y == directioner.snd_pos[1]):
                            new_x, new_y = self.get_adjoining_valid_pos(x, y)
                        return new_x, new_y
                    else:
                        return x, y
                if directioner.direction == Direction.DOWNWARDS or directioner.direction == Direction.UPWARDS:
                    if self.can_alien_move_to_pos(x,y-1) or self.can_alien_move_to_pos(x,y+1):
                        # the alien will move to a random adjacent position that's not equal to the snd_pos
                        new_x, new_y = self.get_adjoining_valid_pos(x, y)
                        while (new_x == directioner.snd_pos[0] and new_y == directioner.snd_pos[1]):
                            new_x, new_y = self.get_adjoining_valid_pos(x, y)
                        return new_x, new_y
                    else:
                        return x, y

    """
    Returns a position that 
    it is on the board dimension and 
    it is not a modifier nor an alterator
    """

    def get_adjoining_valid_pos(self, x, y):
        # the alien can only stay on it's place
        if not self.alien_has_free_adjacent_positions(x, y):
            return x, y
        else: # the alien has a free adjacent position to move to
            move_to = random.randint(0, 3)
            if move_to == 0:  # move to the left
                new_x, new_y = x - 1, y
            elif move_to == 1:  # move to the right
                new_x, new_y = x + 1, y
            elif move_to == 2:  # move up
                new_x, new_y = x, y - 1
            else:  # move down
                new_x, new_y = x, y + 1
            if not self.can_alien_move_to_pos(new_x, new_y):
                return self.get_adjoining_valid_pos(x, y)  # calls the method again
            else:
                return new_x, new_y


    """
    Method that returns True if there's a free adjacent position for the alien
    to move to. False if there's none.
    """
    def alien_has_free_adjacent_positions(self, x, y):
        if self.can_alien_move_to_pos(x-1,y):
            return True
        elif self.can_alien_move_to_pos(x+1,y):
            return True
        elif self.can_alien_move_to_pos(x,y-1):
            return True
        elif self.can_alien_move_to_pos(x,y+1):
            return True
        else:
            return False

    """
    Given a position, returns True if the alien can move there.
    The alien can move there if the position is within the board's perimeter and
    there's no mountain there.
    """

    def can_alien_move_to_pos(self, x, y):
        if 0 <= x < self.rows and 0 <= y < self.cols:
            if self.get_cell(x, y).modifier is Modifier.MOUNTAIN_RANGE:
                return False
            else:
                return True
        else:
            return False

    """
    Methods that sets an alien on the board at a given position.
    The dictionary of aliens is updated.
    """

    def set_alien(self, x, y, alien):
        self.get_cell(x, y).add_alien(alien)
        self.set_alien_in_dictionary(x, y, alien)

    """
    Methods that removes an alien on the board at a given position.
    The dictionary of aliens is updated.
    """

    def remove_alien_from_board(self, x, y, alien):
        if isinstance(alien, Alien):
            self.get_cell(x, y).remove_alien(alien)
            self.aliens[(x, y)].remove(alien)
        else:
            raise ValueError(f'you can only remove aliens')

    """
    Given an alien, this method returns the position were the alien is placed
    on the board. The position is returned in the form of a tuple.
    """

    def get_alien_position(self, alien):
        for key in self.aliens:
            list_of_aliens = self.aliens[key]  # list of aliens in that key
            for alien_aux in list_of_aliens:
                if alien_aux is alien:
                    return (key[0], key[1])

    """
    This code defines a method for handling alien attacks on OVNI (UFO) units in a game scenario.

    The method checks the team of the attacking alien (either "BLUE" or "GREEN") and compares its position with the 
    range of the opposing team's OVNI. It then reduces the OVNI's life points based on the alien's "eyes" attribute, 
    and if the alien's position matches an entry in the 'aliens' dictionary, it removes the alien from that position.
    """

    def alien_attack_ovni(self, x, y, alien):
        if alien.team == Team.BLUE and self.is_position_in_green_range(x, y):
            self.green_ovni_life -= alien.eyes
            if (x, y) in self.aliens:
                self.aliens[(x, y)].remove(alien)  # removes from hash and cell
        elif alien.team == Team.GREEN and self.is_position_in_blue_range(x, y):
            self.blue_ovni_life -= alien.eyes
            if (x, y) in self.aliens:
                self.aliens[(x, y)].remove(alien)
    
    def any_ovni_destroyed(self):
        return self.green_ovni_life <= 0 or self.blue_ovni_life <= 0

    @staticmethod
    def _row_to_string(row):
        res = ''
        columns = len(row)
        for col in range(columns):
            res += row[col].__str__()
            if col < columns - 1:
                res += '|'
        return res

    def __str__(self):
        res = ''
        for row_num in range(self.rows):
            res += Board._row_to_string(self.board[row_num])
            if row_num < self.rows - 1:
                res += '\n'
        return res

    @staticmethod
    def from_string(board_str):
        rows = board_str.split('\n')
        n_rows = len(rows)
        if n_rows < 1:
            raise ValueError(f'Invalid number of rows: {n_rows}')
        matrix = [row.split('|') for row in rows]
        n_cols = len(matrix[0])
        if n_cols < 1:
            raise ValueError(f'Invalid number of columns: {n_cols}')
        for row in range(n_rows):
            row_len = len(matrix[row])
            if row_len != n_cols:
                raise ValueError(f'Invalid number of columns: {row_len}')

        return Board._from_string_matrix(n_rows, n_cols, matrix)

    @staticmethod
    def _from_string_matrix(rows, cols, matrix):
        new_board = Board(rows, cols)
        for row in range(rows):
            for col in range(cols):
                board_cell = new_board.get_cell(row, col)
                board_cell.modifier = None
                board_cell.alterator = None

                curr_cell = matrix[row][col]
                new_board.put_cell(row, col, Cell.from_string(curr_cell))
        return new_board

    def put_cell(self, row, column, cell):
        self.board[row][column] = cell

    def json(self):
        return {
            'blue_ovni_range': self.blue_ovni_range,
            'green_ovni_range': self.green_ovni_range,
            'base_range_dimentions': self.base_range_dimentions,
            'board': self.board.__str__()
        }


class BoardSchema(Schema):
    blue_ovni_range = fields.Tuple((fields.Integer(), fields.Integer()))
    green_ovni_range = fields.Tuple((fields.Integer(), fields.Integer()))
    base_range_dimentions = fields.Integer()
    board = fields.List(fields.List(fields.Nested(CellSchema())))

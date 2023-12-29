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

GREEN_OVNI_LIFE = 10
BLUE_OVNI_LIFE = 10


class Board:

    def __init__(self, rows=10, cols=15, base_range_dimentions=4):
        self.rows = rows
        self.cols = cols
        # Dictionary with Key = position on the board, Value = list of aliens in that position
        self.aliens = {}
        self.alterators_positioned = {}
        self.base_range_dimentions = base_range_dimentions
        self.green_ovni_range = (
            base_range_dimentions - 1, base_range_dimentions - 1)
        self.blue_ovni_range = (
            rows - 1 - (base_range_dimentions - 1), cols - 1 - (base_range_dimentions - 1))
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
            mountain_list = MountainRange(
                initial_position, random.choice(orientations))

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
        return 0 <= x <= self.green_ovni_range[0] and 0 <= y <= self.green_ovni_range[1]

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
            self.alterators_positioned[(x, y)] = Alterator.TRAP
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
            self.alterators_positioned[(door_row, door_col)] = teleporter
            self.alterators_positioned[(exit_row, exit_col)] = teleporter
        else:
            raise ValueError(
                "Positions of the teleporter aren't free or valid")

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
                raise ValueError(
                    "Positions of the directioner aren't free or valid")

        for row, col in positions:
            self.get_cell(row, col).alterator = directioner
            self.alterators_positioned[(row, col)] = directioner

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
    Returns the Modifier that's on a specific Cell.
    """

    def get_modifier(self, x, y):
        return self.get_cell(x, y).modifier

    """
    Method that sets an alien on the alive aliens dictionary.
    """

    def set_alien_in_dictionary(self, x, y, alien):
        position = (x, y)
        # if there's already aliens at that position
        if position in self.aliens:
            # we add it to the list of aliens
            self.aliens[position].append(alien)
        else:
            # Key doesn't exist, create new list of aliens
            self.aliens[position] = [alien]

    """ 
    Updates the board by moving each alien to a free random adjoining position.
    """

    def refresh_board(self):

        copy = {}
        for pos in self.aliens.keys():
            for alien in self.aliens[pos]:
                if pos in copy:
                    copy[pos].append(alien)
                else:
                    copy[pos] = [alien]
        # en este entonces estaria copiado self.aliens en copy, con las claves y valores

        for pos in copy.keys():     # se mueven todos los aliens del hash copy
            x = pos[0]
            y = pos[1]
            for alien in copy[pos]:
                self.move_alien(x, y, alien)

    """
    This method solves each fight and/or reproduction that may occur between aliens 
    on each cell. 
    It also solves any action that may occur between aliens and Alterators/Modifiers.
    """

    def act_board(self):

        for key in list(self.aliens.keys()):
            x, y = key[0], key[1]
            cell = self.get_cell(x, y)
            if cell.aliens.__len__() >= 1:   # action the cell if there is more than one alien
                cell.action()
                self.aliens[(x, y)] = cell.aliens.copy()   # updates the dict

            # atack enemy ovni
            if len(cell.aliens) == 1:
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
        if not self.get_cell(x, y).aliens.__contains__(alien):
            raise ValueError("alien not found in position")

        alterator = self.get_cell(x, y).alterator  # alterator on the cell

        if isinstance(alterator, Teleporter):
            new_x, new_y = self.new_alien_pos_with_teleporter(x, y, alterator)
        elif isinstance(alterator, Directioner):
            new_x, new_y = self.new_alien_pos_with_directioner(x, y, alterator)
        else:
            new_x, new_y = self.get_adjoining_valid_pos(x, y)

        self.remove_alien_from_board(x, y, alien)
        self.set_alien(new_x, new_y, alien)

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
                    valid_positions = []
                    if self.can_alien_move_to_pos(x - 1, y):
                        valid_positions.append((x-1, y))
                    if self.can_alien_move_to_pos(x + 1, y):
                        valid_positions.append((x+1, y))
                    if valid_positions:
                        # the alien will move to a random adjacent position that's not equal to the snd_pos
                        new_x, new_y = random.choice(valid_positions)
                        return new_x, new_y
                    else:
                        # the alien has nowhere to move, it'll stay on its position
                        return x, y
                if directioner.direction == Direction.DOWNWARDS or directioner.direction == Direction.UPWARDS:
                    valid_positions = []
                    if self.can_alien_move_to_pos(x, y-1):
                        valid_positions.append((x, y-1))
                    if self.can_alien_move_to_pos(x, y+1):
                        valid_positions.append((x, y+1))
                    if valid_positions:
                        # the alien will move to a random adjacent position that's not equal to the snd_pos
                        new_x, new_y = random.choice(valid_positions)
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
        else:  # the alien has a free adjacent position to move to
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
                # calls the method again
                return self.get_adjoining_valid_pos(x, y)
            else:
                return new_x, new_y

    """
    Method that returns True if there's a free adjacent position for the alien
    to move to. False if there's none.
    """

    def alien_has_free_adjacent_positions(self, x, y):
        positions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for new_x, new_y in positions:
            if self.can_alien_move_to_pos(x + new_x, y + new_y):
                return True
        return False

    """
    Given a position, returns True if the alien can move there.
    The alien can move there if the position is within the board's perimeter and
    there's no mountain there.
    """

    def can_alien_move_to_pos(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.get_cell(x, y).modifier is not Modifier.MOUNTAIN_RANGE

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
        if isinstance(alien, Alien) and self.aliens.__contains__((x, y)):
            self.get_cell(x, y).remove_alien(alien)
            self.remove_alien_in_dict(x, y, alien)
        else:
            raise ValueError(f'alien not found')

    '''
    This method removes an alien ONLY from the dictionary of aliens
    '''

    def remove_alien_in_dict(self, x, y, alien):
        if self.aliens[(x, y)].__len__() == 1:
            self.aliens.pop((x, y))
        elif self.aliens[(x, y)].__len__() > 1:
            self.aliens[(x, y)].remove(alien)

    """
    This method returns True if the game is over.
    The game is over when any of the OVNI's life is 0.
    """

    def any_ovni_destroyed(self):
        return self.green_ovni_life <= 0 or self.blue_ovni_life <= 0

    """
    Given an alien, this method returns the position were the alien is placed
    on the board. The position is returned in the form of a tuple.
    """

    def get_alien_position(self, alien):
        for key in self.aliens:
            list_of_aliens = self.aliens[key]  # list of aliens in that key
            for alien_aux in list_of_aliens:
                if alien_aux is alien:
                    return key[0], key[1]

    """
    This code defines a method for handling alien attacks on OVNI (UFO) units in a game scenario.
    The method checks the team of the attacking alien (either "BLUE" or "GREEN") and compares its position with the 
    range of the opposing team's OVNI. It then reduces the OVNI's life points based on the alien's "eyes" attribute, 
    and if the alien's position matches an entry in the 'aliens' dictionary, it removes the alien from that position.
    """

    def alien_attack_ovni(self, x, y, alien):
        if alien.team == Team.BLUE and self.is_position_in_green_range(x, y):
            self.green_ovni_life -= alien.eyes
        elif alien.team == Team.GREEN and self.is_position_in_blue_range(x, y):
            self.blue_ovni_life -= alien.eyes

        if (x, y) in self.aliens:
            self.remove_alien_from_board(x, y, alien)

    '''
    The method returns True if any of the OVNI's life is 0.
    '''

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

    '''
    This method kills a given number of aliens of a given team  
    '''

    def kill_aliens(self, team, cant):
        team_aliens = self.list_aliens_of_team(team)
        # en este punto todos los aliens del equipo 'team' estaran almacenados en team_aliens
        if team_aliens.__len__() < cant:
            return False

        else:
            for i in range(cant):
                alien_to_kill = random.choice(list(team_aliens.keys()))
                # deletes the key and return its value
                x, y = team_aliens.pop(alien_to_kill)
                self.remove_alien_from_board(
                    x, y, alien_to_kill)  # kills the alien
            return True

    '''
    This method returns a dict with the aliens of a given team as keys and their positions as values
    '''

    def list_aliens_of_team(self, team):
        team_aliens = {}  # dict que llevara los aliens como clave y su pos como valor
        for pos, aliens_on_cell in self.aliens.items():
            for alien in aliens_on_cell:
                if alien.team is team:
                    x, y = pos
                    team_aliens[alien] = (x, y)
        return team_aliens

    '''
    This method returns the number of aliens of a given team
    '''

    def get_aliens_cant_of_team(self, team):
        return self.list_aliens_of_team(team).__len__()

    '''
    This method adds eyes to an alien in a given position
    '''

    def add_eyes_to_alien(self, x, y, alien_pos_in_list, num_eyes):
        cell = self.get_cell(x, y)
        cell.aliens[alien_pos_in_list].add_eyes(num_eyes)

    '''
    This method returns an alien in a given position
    '''

    def get_alien_in_position(self, x, y, alien_pos_in_list):
        cell = self.get_cell(x, y)
        return cell.aliens[alien_pos_in_list]

    '''
    This method returns the number of aliens in a given position 
    '''

    def get_num_aliens_in_position(self, x, y):
        cell = self.get_cell(x, y)
        return len(cell.aliens)


class AliensPositionField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        cell_dict = {}
        cell_schema = CellSchema()
        for key in obj.aliens:  # add aliens to the schema
            cell = obj.get_cell(key[0], key[1])
            if str(key) in cell_dict:
                cell_dict[str(key)].append(cell_schema.dump(cell))
            else:
                cell_dict[str(key)] = cell_schema.dump(cell)

        for key in obj.alterators_positioned:   # add alterators
            cell = obj.get_cell(key[0], key[1])
            if str(key) not in cell_dict:
                cell_dict[str(key)] = cell_schema.dump(cell)

        return cell_dict


class BoardSchema(Schema):
    blue_ovni_range = fields.Tuple((fields.Integer(), fields.Integer()))
    green_ovni_range = fields.Tuple((fields.Integer(), fields.Integer()))
    base_range_dimentions = fields.Integer()
    cells = AliensPositionField(attribute='aliens')
    green_ovni_life = fields.Integer()
    blue_ovni_life = fields.Integer()
    grid = fields.List(fields.List(
        fields.Nested(CellSchema())), attribute='board')

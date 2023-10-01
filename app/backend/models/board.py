import random
from app.backend.models.alterator import Alterator
from app.backend.models.cell import Cell
from app.backend.models.modifier import Modifier
from app.backend.models.orientation import Orientation
from app.backend.models.mountain_range import MountainRange


class Board:

    def __init__(self, rows, cols, base_range_dimentions):
        self.rows = rows
        self.cols = cols
        self.aliens = {}  # Dictionary with Key = position on the board, Value = list of aliens in that position
        self.base_range_dimentions = base_range_dimentions
        self.green_ovni_range = (base_range_dimentions - 1, base_range_dimentions - 1)
        self.blue_ovni_range = (rows - 1 - (base_range_dimentions - 1), cols - 1 - (base_range_dimentions - 1))
        self.board = []
        self.create_board()
        # TODO llevar vidas de las naves

    """
    Creates the initial board full of Cells and
    default modifiers: MountainRange, Killer, Multiplier
    that are set outside the ovnis ranges
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
                    self.set_modifier(Modifier.MOUNTAIN, pos[0], pos[1])
                break

    """
    Returns a free position of the board which it is not
    a modifier, nor an alterator or is in any ovnis ranges
    """
    def get_random_free_pos(self):
        while True: # se ejecuta infinitamente hasta que se le isntruccione salir del bucle
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.cols - 1)
            if self.is_free_position(x, y) and not self.is_pos_on_any_range(x, y):
                return x, y
        """
        x = random.randint(0, self.rows-1)
        y = random.randint(0, self.cols-1)
        if not self.is_free_position(x, y) or self.is_pos_on_any_range(x, y):
            return self.get_random_free_pos()  # calls the method again
        else:
            return x, y
    """

    # TODO la uso en el test move_alien
    """
    Checks if a given position is within the board's perimeter
    """
    def is_within_board_range(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols


    """
    Returns True if 
    the position is on the board range and 
    it's not a modifier or an alterator
    """
    def is_free_position(self, x, y):
        if self.is_within_board_range(x,y):
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
    Returns True if the position is on the blue base range
    """
    def is_position_in_blue_range(self, x, y):
        if self.blue_ovni_range[0] <= x < self.rows and self.blue_ovni_range[1] <= y < self.cols:
            return True
        else:
            return False


    """
    Returns True if the position is on the green base range
    """
    def is_position_in_green_range(self, x, y):
        if 0 <= x <= self.green_ovni_range[0] and 0 <= y <= self.green_ovni_range[1]:
            return True
        else:
            return False


    """
    Returns the Cell that's at a specific position
    """
    def get_cell(self, x, y):
        #return self.board[x][y]
        if 0 <= x < self.rows and 0 <= y < self.cols:
            return self.board[x][y]
        else:
            raise IndexError("Index out of range")
    

    """ 
    Sets an Alterator on a specific Cell
    only if on that cell there's no Modifier or Alterator already placed there
    """
    #   TODO agregar condicion que no sea el rango de las naves?
    # TODO si es un direccionador necesito recibir la direccion, si es un teleporter necesito 
    # recibir la posicion inicial y decidir si la salida va a ser fija o la decide el usuario
    def set_alterator(self, alterator, x, y):
        if self.is_free_position(x, y):
            self.get_cell(x, y).alterator = alterator
        else:
            raise AttributeError("There's already an Alterator on that cell")


    """ 
    Sets a Modifier on a specific Cell only if on that cell 
    there's no Modifier or Alterator already placed there
    """
    def set_modifier(self, modifier, x, y):
        if self.is_free_position(x, y):
            self.get_cell(x, y).modifier = modifier
        else:
            raise AttributeError("There's already a Modifier on that cell")


    """
    Method that sets an alien on the alives aliens dictionary
    """
    def set_alien_in_dictionary(self, x, y, alien):
        position = (x, y)
        # if there's already aliens at that position
        if position in self.aliens:
            self.aliens[position].append(alien)  # we add it to the list of aliens
        else:
            self.aliens[position] = [alien]  # Key doesn't exist, create new list of aliens



    """ 
    Updates the board by moving each alien to a free random adjoining position
    """
    def refresh_board(self):
        aliens_copy = dict(self.aliens)     # dictionary copy
        for key in aliens_copy:
            list_of_aliens = aliens_copy[key]  # list of aliens in that key
            for alien in list_of_aliens:
                x = key[0]
                y = key[1]
                self.move_alien(x, y, alien)



    """ 
    This method solves each fight and/or reproduction that may occur between aliens 
    on each cell. 
    It also solves any action that may occur between aliens and Alterators/Modifiers. # TODO alterators
    """
    def act_board(self):
        for key in self.aliens:
            x = key[0]
            y = key[1]
            cell = self.get_cell(x, y)
            cell.action()   # only one alien will be left or just none after the action
            self.aliens[(x, y)] = cell.aliens


    """
    Moves an alien to a free random and adjacent position.
    x, y represent the position where the alien is currently placed at.
    It updates both the dictionary and board.
    """
    def move_alien(self, x, y, alien):
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
    Returns a position that 
    it is on the board dimension and 
    it is not a modifier nor an alterator
    """
    def get_adjoining_valid_pos(self, x, y):
        move_to = random.randint(0, 3)
        if move_to == 0:    # move to the left
            new_x, new_y = x-1, y
        elif move_to == 1:  # move to the right
            new_x, new_y = x+1, y
        elif move_to == 2:  # move up
            new_x, new_y = x, y-1
        else:  # move down
            new_x, new_y = x, y+1
        if not self.can_alien_move_to_pos(new_x, new_y):
           return self.get_adjoining_valid_pos(x, y)  # calls the method again
        else:
            return new_x, new_y


    """
    Given a position, return True if the alien can move there.
    The alien can move there if the position is within the board's perimeter and
    there's no mountain there.
    """
    def can_alien_move_to_pos(self, x, y):
        if 0 <= x < self.rows and 0 <= y < self.cols:
            if self.get_cell(x, y).alterator is not Modifier.MOUNTAIN:
                return True
            else:
                return False
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
    Given an alien, this method returns the position were the alien is placed
    on the board. The position is returned in the form of a tuple.
    """
    def get_alien_position(self, alien):
        for key in self.aliens:
            list_of_aliens = self.aliens[key]  # list of aliens in that key
            for alien_aux in list_of_aliens:
                if alien_aux == alien:
                    return (key[0], key[1])


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

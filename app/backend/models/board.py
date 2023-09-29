import random


from app.backend.models.cell import Cell
from app.backend.models.modifier import Modifier
from app.backend.models.mountain_range import MountainRange


class Board:

    def __init__(self, rows, cols, base_range_dimentions):
        self.rows = rows
        self.cols = cols
        self.board = self.create_board()
        self.aliens = {}  # Dictionary with Key = position on the board, Value = list of aliens in that position
        self.base_range_dimentions = base_range_dimentions
        self.green_ovni_range = (base_range_dimentions - 1, base_range_dimentions - 1)
        self.blue_ovni_range = (rows - 1 - (base_range_dimentions - 1), cols - 1 - (base_range_dimentions - 1))
        # TODO llevar vidas de las naves
    """
    Creates the initial board full of Cells and
    default modifiers: MountainRange, Killer, Multiplier
    that are setted outside the ovnis ranges
    """

    def create_board(self):
        rows = self.rows
        cols = self.cols
        board = [[Cell() for _ in range(rows)] for _ in range(cols)]  # creates the board with Cells

        # Setting the default Modifiers in free random positions
        for i in range(2):
            # setting mountains
            x, y = self.get_random_free_pos()
            mountain_list = MountainRange(x, y)
            # TODO iterar la lista de listas(posiciones) que devuelve un constructor de MountainCordon
            #   y setearlas como tal
            #   chequear tambien que las posiciones que me devuelve son validas
            for m in mountain_list:     # something like this
                x, y = mountain_list[i][0], mountain_list[i][1]
                self.get_cell(x, y).modifier = mountain_range()
            # setting killers
            x, y = self.get_random_free_pos()
            self.get_cell(x, y).modifier = Modifier.KILLER

            # setting multipliers
            x, y = self.get_random_free_pos()
            self.get_cell(x, y).modifier = Modifier.MULTIPLIER

        return board

    """
    Returns a free position of the board which it is not
    a modifier, nor an alterator or is in any ovnis ranges
    """

    def get_random_free_pos(self):
        x = random.randint(0, self.rows-1)
        y = random.randint(0, self.cols-1)
        if not self.is_free_position(x, y) or self.is_pos_on_any_range(x, y):
            self.get_random_free_pos()  # calls the method again
        else:
            return x, y

    """
    Returns True if 
    the position is on the board range and 
    it's not a modifier or an alterator
    """

    def is_free_position(self, x, y):
        if 0 <= x < self.rows and 0 <= y < self.cols:
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
        if 0 <= x <= self.blue_ovni_range[0] and 0 <= y <= self.blue_ovni_range[1]:
            return True
        else:
            return False

    """
    Returns True if the position is on the green base range
    """

    def is_position_in_green_range(self, x, y):
        if self.green_ovni_range[0] <= x < self.rows and self.green_ovni_range[1] <= y < self.cols:
            return True
        else:
            return False

    """
    Returns the Cell that's at a specific position
    """

    def get_cell(self, x, y):
        return self.board[x][y]

    """ 
    Sets an Alterator on a specific Cell
    only if on that cell there's no Modifier or Alterator already placed there
    """
    #   TODO agregar condicion que no sea el rango de las naves?
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
        for key in self.aliens:
            list_of_aliens = self.aliens[key]  # list of aliens in that key
            for alien in list_of_aliens:
                x = key[0]
                y = key[1]
                self.move_alien(x, y, alien)

    """
    solving each fight and/or reproduction that may occur in aliens positions
    """
    def act_board(self):
        for key in self.aliens:
            x = key[0]
            y = key[1]
            cell = self.get_cell(x, y)
            cell.action()

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
        if (x, y) in self.aliens and alien in self.aliens[(x, y)]:
            self.aliens[(x, y)].remove(alien)
            self.set_alien_in_dictionary(new_x, new_y, alien)
        else:
            raise

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
        if not self.is_free_position(new_x, new_y):
            self.get_adjoining_valid_pos(x, y)  # calls the method again
        else:
            return new_x, new_y

    def set_alien(self, x, y, alien):
        self.get_cell(x, y).add_alien(alien)
        self.set_alien_in_dictionary(x, y, alien)

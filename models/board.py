import random

from models.cell import Cell


class Board:

    def __init__(self, rows, cols, baseRangeDimentions):
        self.rows = rows
        self.cols = cols
        self.board = self.create_board()
        self.aliens = {} # Dictionary with Key = position on the board, Value = list of aliens in that position
        self.baseRangeDimentions = baseRangeDimentions
        self.green_nave_range = (baseRangeDimentions - 1, baseRangeDimentions - 1)
        self.blue_nave_range = (rows - 1 - baseRangeDimentions - 1, cols - 1 - baseRangeDimentions - 1)


    # Creates the initial board with Cells and Modifiers
    def create_board(self):
        rows = self.rows
        cols = self.cols
        board = [[Cell() for _ in range(cols)] for _ in range(rows)]  # Creates the board with Cells

        # Setting the default Modifiers in free random positions
        for i in range(2):
            r, c = self.get_random_free_pos()
            board[r][c].modifier = MountainCordon()

            r, c = self.get_random_free_pos()
            board[r][c].modifier = Killer()

            r, c = self.get_random_free_pos()
            board[r][c].modifier = Multiplier()

        return board

    """
    Returns a free position of the board which is not
    a modifier, nor an alterator or is in the nave range 
    """
    def get_random_free_pos(self):
        r = random.randint(0, self.rows)
        c = random.randint(0, self.cols)
        if not self.is_free_position(r, c):
            self.get_random_free_pos()
        else:
            return r, c
    

    """
    Returns True if the position is on the board range, it's not on both
     nave ranges and it's not a modifier or alterator already.
    """
    def is_free_position(self, x, y):
        if 0 < x < self.rows and 0 < y < self.rows:
            if (self.board[x][y].modifier is None or
                    self.board[x][y].alterator is None or
                        not self.is_pos_on_any_range(x, y)):
                    return True
            else:
                return False
        else:
            return False


    # Returns True if the position is on any of the ranges of the spaceships
    def is_pos_on_any_range(self, x, y):
        return self.is_position_in_blue_range(x, y) or self.is_position_in_green_range(x, y)


    
    # Returns True if the position is on the blue base
    def is_position_in_blue_range(self, x, y):
        if (x <= self.blue_nave_range[0] and x >= 0 and y <= self.blue_nave_range[1] and y <= 0):
            return True
        else:
            return False


    # Returns True if the position is on the blue base
    def is_position_in_green_range(self, x, y):
        if (x >= self.green_nave_range[0] and x <= self.rows-1 and y >= self.green_nave_range[1] and y <= self.cols-1):
            return True
        else:
            return False


    # Returns the Cell that's at a specific position
    def get_cell(self, x, y):
        return self.board[x][y]
        

    """ 
    Sets an Alterator on a specific Cell
    only if on that cell there's no Modifier or Alterator already placed there
    """
    def set_alterator(self, alterator, row, col):
        if (self.board[row][col].alterator == None and self.board[row][col].modifier == None):
            self.board[row][col].alterator == alterator
        else:
            raise AttributeError("There's already an Alterator or a Modifier on that cell")
        
    """ 
    Sets a Modifier on a specific Cell only if on that cell 
    there's no Modifier or Alterator already placed there
    """
    def set_modifier(self, modifier, row, col):
        if (self.board[row][col].modifier == None and self.board[row][col].modifier == None):
            self.board[row][col].modifier == modifier
        else:
            raise AttributeError("There's already an Alterator or a Modifier on that cell")
        

    # Method that sets an Alien in a specific position of the board
    def set_alien(self, row, col, alien):
        self.board[row][col].alien.append(alien)
        self.set_alien_in_dictionary(row, col, alien)
        
        
    # Method that sets an alien on the dictionary
    def set_alien_in_dictionary(self, x, y, alien):
        position = (x, y)
        # if there's already aliens at that position
        if position in self.aliens:  
            self.aliens[position].append(alien)  # we add it to the list of aliens 
        else:
            self.aliens[position] = [alien] # Key doesn't exist, create new list of aliens 


    """
    Updates the board by moving each alien to a free random adjacent position
    and solving each fight and/or reproduction that may occur in the new position
    """
    def refresh_board(self):
        # first we move all the aliens to the new random position
        for key in self.aliens:
            listOfAliens = self.aliens[key]  # list of aliens in that key
            for alien in listOfAliens:
                self.move_alien(key[0], key[1], alien)

        # now we update each cell
        for key in self.aliens:
            self.board[key[0]][key[1]].action()


    """
    Moves an alien to a free random and adjacent position.
    x, y represent the position where the alien is currently placed at.
    It updates both the dictionary and board.
    """
    def move_alien(self, x, y, alien):
        flag = False
        invalid = []    #si la posicion es invalida no la mira mas
        while flag is False:
            newPos = Methods.random(4)    # TODO como funciona ese random?
            if (newPos == 0 and newPos not in invalid):
                if (self.is_free_position(x-1,y)):  # newPos on the left of current position
                    self.board[x][y].remove_alien(alien)    # update the board
                    self.board[x-1][y].add_alien(alien)
                    # update the dictionary
                    if ((x,y) in self.aliens and alien in self.aliens[(x,y)]):
                        self.aliens[(x,y)].remove(alien)  
                        self.set_alien_in_dictionary(x-1, y, alien)
                    flag = True
                else:
                    invalid.append(newPos)  # the position is invalid
                
            if (newPos is 1 and newPos not in invalid): 
                if (self.is_valid_position(x,y-1)):     # newPos is at the bottom of current position
                    self.board[x][y].remove_alien(alien)
                    self.board[x][y-1].add_alien(alien)
                    # update the dictionary
                    if ((x,y) in self.aliens and alien in self.aliens[(x,y)]):
                        self.aliens[(x,y)].remove(alien)  
                        self.set_alien_in_dictionary(x, y-1, alien)
                    flag = True
                else:
                    invalid.append(newPos)

            if (newPos is 2 and newPos not in invalid): 
                if (self.is_valid_position(x+1,y)):    # newPos is on the right of current position
                    self.board[x][y].remove_alien(alien)
                    self.board[x+1][y].add_alien(alien)
                    # update the dictionary
                    if ((x,y) in self.aliens and alien in self.aliens[(x,y)]):
                        self.aliens[(x,y)].remove(alien)  
                        self.set_alien_in_dictionary(x+1, y, alien)
                    flag = True
                else:
                    invalid.append(newPos)

            if (newPos is 3 and newPos not in invalid): 
                if(self.is_valid_position(x,y+1)):     # newPos is at the top of current position
                    self.board[x][y].remove_alien(alien)
                    self.board[x][y+1].add_alien(alien)
                    # update the dictionary
                    if ((x,y) in self.aliens and alien in self.aliens[(x,y)]):
                        self.aliens[(x,y)].remove(alien)  
                        self.set_alien_in_dictionary(x, y+1, alien)
                    flag = True
                else:
                    invalid.append(newPos)


    
import random

from models.cell import Cell


class Board:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = self.create_board()
        self.aliens = {}
        self.green_nave_range = (4, 4) # esta bien eso?
        self.blue_nave_range = (rows - 5, cols - 5)

    # Creates the board with Cells and Modifiers
    def create_board(self):
        rows = self.rows
        cols = self.cols
        board = [[Cell() for _ in range(cols)] for _ in range(rows)]  # Crea una matriz de objetos Cell

        # set killers
        for i in range(2):
            r, c = self.get_random_free_pos()
            board[r][c].modifier = MountainCordon()

            r, c = self.get_random_free_pos()
            board[r][c].modifier = Killer()

            r, c = self.get_random_free_pos()
            board[r][c].modifier = Multiplier()

        return board

    # returns a free position of the board
    # not modifier, not alter, not range
    def get_random_free_pos(self):
        r = random.randint(0, self.rows)
        c = random.randint(0, self.cols)
        if not self.is_free_position(r, c):
            self.get_random_free_pos()
        else:
            return r, c

    # return true if the pos is on the board range and if it is not a modifier already
    # and position is not on the nave ranges
    def is_free_position(self, x, y):
        if 0 < x < self.rows and 0 < y < self.rows:
            if (self.board[x][y].modifier is None or
                    self.board[x][y].alterator is None or
                        not self.is_pos_on_range(x, y)):
                    return True
            else:
                return False
        else:
            return False

    def is_pos_on_range(self, x, y):
        return self.in_blue_range(x, y) or self.in_green_range(x, y)


    # Range of the blue base
    def in_blue_range(self, i, j):
        blue_range_x = self.blue_nave_range[0]
        blue_range_y = self.blue_nave_range[1]
        # lista de posiciones que son permimetro de la base azul
        blue_range = [(x, blue_range_y) for x in range(0, blue_range_x)]
        blue_range1 = [(blue_range_x, y) for y in range(0, blue_range_y)]
        return (i, j) in blue_range + blue_range1
    
    # Range of the green base
    def in_green_range(self, i, j):
        green_range_x = self.green_nave_range[0]
        green_range_y = self.green_nave_range[1]
        #lista de posiciones que son permimetro de la base verde
        green_range = [(x, green_range_y-5) for x in range(green_range_x - 5,  green_range_x)]
        green_range1 = [(green_range_x - 5, y) for y in range(green_range_y - 5,  green_range_y)]
        return (i, j) in green_range + green_range1


    #retorna una celda
    def get_cell(self, x, y):
        return self.board[x][y]
        
    #setea un alterador o modificador en una celda especifica
    def set_alterator(self, cell, row, col):
        if(self.board[row][col] is None):
            self.board[row][col].alterator = cell


    #metodo privado para setear un alien en el diccionario
    def __set_alien_hash__(self, x, y, alien):
        position = (x, y) #clave del diccionario
        if position in self.aliens:  #Si la posicion ya tiene alien, lo agrega a la lista de aliens de esa posicion
            self.aliens[position] = self.aliens[position].append(alien)  #lo agrega al hash como lista, para poder tener una clave, varios valores
        else:
            self.aliens[position] = [alien] #si no existe en el hash, la crea y lo agrega

    #setea un alien en una posicion especifica
    def set_alien(self, row, col, alien):
        self.board[row][col].alien.append(alien)
        Board.__set_alien_hash__(row, col, alien)

    #mueve un alien a una posicion random(arriba, abajo, izquierda, derecha)
    def move_alien(self, x, y, alien):
        flag = False
        invalid = []    #si la posicion es invalida no la mira mas
        while flag is False:
            move = Methods.random(4)
            if (move == 0 and move not in invalid):
                if (Board.is_valid_position(x-1,y)):
                    self.board[x][y].remove_alien(alien)
                    self.board[x-1][y].add_alien(alien)
                    #lo elimino del diccionario en esa posicion y lo agrego en otra position
                    if ((x,y) in self.alien):
                        self.aliens[(x,y)].remove(alien)  
                        Board.__set_alien_hash__(x-1, y, alien)
                    flag = True
                else:
                    invalid.append(move)
                
            if (move is 1 and move not in invalid): 
                if (Board.is_valid_position(x,y-1)):
                    self.board[x][y].remove_alien(alien)
                    self.board[x][y-1].add_alien(alien)
                    #lo elimino del diccionario en esa posicion y lo agrego en otra position
                    if ((x,y) in self.aliens):
                        self.aliens[(x,y)].remove(alien)  
                        Board.__set_alien_hash__(x, y-1, alien)
                    flag = True
                else:
                    invalid.append(move)

            if (move is 2 and move not in invalid): 
                if (Board.is_valid_position(x+1,y)):
                    self.board[x][y].remove_alien(alien)
                    self.board[x+1][y].add_alien(alien)
                    #lo elimino del diccionario en esa posicion y lo agrego en otra position
                    if ((x,y) in self.aliens):
                        self.aliens[(x,y)].remove(alien)  
                        Board.__set_alien_hash__(x+1, y, alien)
                    flag = True
                else:
                    invalid.append(move)

            if (move is 3 and move not in invalid): 
                if(Board.is_valid_position(x,y+1)):
                    self.board[x][y].remove_alien(alien)
                    self.board[x][y+1].add_alien(alien)
                    #lo elimino del diccionario en esa posicion y lo agrego en otra position
                    if ((x,y) in self.aliens):
                        self.aliens[(x,y)].remove(alien)  
                        Board.__set_alien_hash__(x, y+1, alien)
                    flag = True
                else:
                    invalid.append(move)


    #Actualiza el tablero moviendo los aliens y luego accionando las celdas
    def refresh_board(self):
        #mueve los aliens
        for clave in self.aliens:
            posicion = clave  #La clave es la posición 
            alien = self.aliens[clave]  #Se obtiene el alien en esa posición
            Board.move_alien(posicion[0], posicion[1], alien)

        #actualiza la celda
        for clave in self.aliens:
            posicion = clave  #La clave es la posición 
            alien = self.aliens[clave]  #Se obtiene el alien en esa posición
            self.board[posicion[0]][posicion[1]].action()

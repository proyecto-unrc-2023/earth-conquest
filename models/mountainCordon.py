import TOrientation

class MountainCordon:

    # Each Mountain occupies three cells in the board
    def __init__(self, initialPosition, orientation):
        self.initialPosition = initialPosition  # tuple with the initial (x,y) position of the mountain
        self.orientation = orientation
        self.mountain = self.createMountain()   # list of tuples representing the three cells where the mountain is placed

    # Creates a mountain as a list of tuples, each tuple represents a position of
    # each part of the mountain
    def createMountain(self):
        mountainAux = [self.initialPosition]
        if self.orientation == TOrientation.VERTICAL:
            mountainAux.append(self.initialPosition[0], self.initialPosition[1] - 1)
            mountainAux.append(self.initialPosition[0], self.initialPosition[1] - 2)
        else:
            mountainAux.append(self.initialPosition[0] + 1, self.initialPosition[1])
            mountainAux.append(self.initialPosition[0] + 2, self.initialPosition[1])

        return mountainAux
from app.backend.models import orientation


class MountainRange:

    # Each Mountain occupies three cells on the board
    def __init__(self, initial_position, orientation):
        # tuple with the initial (x,y) position of the mountain
        self.initial_position = initial_position
        self.orientation = orientation
        # list of tuples representing the three cells where the mountain is
        self.mountain = self.create_mountain()
        # placed

    """
    Creates a mountain as a list of tuples, each tuple represents
    a position of each part of the mountain
    """

    def create_mountain(self):
        mountain_aux = [self.initial_position]
        if self.orientation == orientation.Orientation.VERTICAL:
            mountain_aux.append(
                (self.initial_position[0], self.initial_position[1] - 1))
            mountain_aux.append(
                (self.initial_position[0], self.initial_position[1] - 2))
        else:
            mountain_aux.append(
                (self.initial_position[0] + 1, self.initial_position[1]))
            mountain_aux.append(
                (self.initial_position[0] + 2, self.initial_position[1]))

        return mountain_aux

from models.game import Game


class Application:

    def __init__(self):
        self.game = None

    def new_game(self, team):
        pass
        # self.game = Game(team)


game = Game(10, 15)

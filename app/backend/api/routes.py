from app.backend.api import *
from app.backend.api.game_controller import GameController

from flask_restful import Resource


class GamesResource(Resource):
    def get(self):
        return GameController.get_all_games()


class GameResource(Resource):

    def get(self, game_id):
        return GameController.get_game_by_id(game_id)

    def post(self):
        return GameController.create_new_game()

    def put(self, game_id):
        return GameController.start_game(game_id)


api.add_resource(GamesResource, '/')
api.add_resource(GameResource, '/', '/<int:game_id>', '/<int:game_id>/start_game')


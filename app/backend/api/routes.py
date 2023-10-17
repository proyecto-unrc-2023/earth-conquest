from app.backend.api import *
from app.backend.api.game_controller import GameController

from flask_restful import Resource, request


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

    def patch(self, game_id):
        data = request.get_json()
        return GameController.update_game(self=self, game_id=game_id, data=data)


api.add_resource(GamesResource, '/')
api.add_resource(GameResource, '/', '/<int:game_id>',
                 '/<int:game_id>/start_game', '/<int:game_id>/update_game')

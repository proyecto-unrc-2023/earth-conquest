from flask import jsonify, request

from app.backend.api import *
from app.backend.api import game_controller
from app.backend.api.game_controller import GameController
from app.backend.models.game import Game, GameSchema

from flask_restful import Resource


class GamesResource(Resource):
    def get(self):
        return game_controller.get_all_games()


class GameResource(Resource):

    def get(self, game_id):
        return GameController.get_game_by_id(game_id)

    def post(self):
        return GameController.create_new_game()

    def put(self, game_id):
        return GameController.update_game(request.json)

    # set board dimentions
    def put(self, game_id, x, y):
        return "dimensions updated successfully"
    # act board
    #def put(self, game_id):
    # refresh board
    #def put(self, game_id):


api.add_resource(GamesResource, '/')
api.add_resource(GameResource, '/', '/<int:game_id>', '/<int:game_id>/board', '/<int:game_id>/board/<int:x>/<int:y>')


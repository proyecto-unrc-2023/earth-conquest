from app.backend.api import *
from app.backend.api.game_controller import GameController

from flask_restful import Resource, request


class GamesResource(Resource):
    def get(self):
        return GameController.get_all_games()

    def post(self):
        return GameController.create_new_game()


class GameDetails(Resource):
    def get(self, game_id):
        return GameController.get_game_by_id(game_id)


class StartGame(Resource):
    def put(self, game_id):
        return GameController.start_game(game_id)


class RefreshBoard(Resource):
    def put(self, game_id):
        return GameController.refresh_board(game_id)


class ActBoard(Resource):
    def put(self, game_id):
        return GameController.act_board(game_id)


api.add_resource(GamesResource, '/')
api.add_resource(GameDetails, '/<int:game_id>')     # get details of a game by its id
api.add_resource(StartGame, '/start_game/<int:game_id>')
api.add_resource(RefreshBoard, '/refresh_board/<int:game_id>')
api.add_resource(ActBoard, '/act_board/<int:game_id>')
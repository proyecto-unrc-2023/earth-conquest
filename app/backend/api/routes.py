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


class IsFreePosition(Resource):
    # /is_free_position/game_id?x=n1&y=n2
    def get(self, game_id):
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
        return GameController.is_free_position(game_id, x, y)


class SetAlterator(Resource):
    def put(self, game_id):
        data = request.json  # data is sent as JSON in the body of the petition
        return GameController.set_alterator(game_id, data)


api.add_resource(GamesResource, '/')
api.add_resource(GameDetails, '/<int:game_id>')     # get details of a game by its id
api.add_resource(StartGame, '/start_game/<int:game_id>')
api.add_resource(IsFreePosition,
                 '/is_free_position/<int:game_id>')  # get info on a position of a game with its id
api.add_resource(SetAlterator, '/set_alterator/<int:game_id>')  # set alterator on board of game with id

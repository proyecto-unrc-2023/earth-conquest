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


class SpawnAliens(Resource):
    def put(self, game_id):
        return GameController.spawn_aliens(game_id)


class JoinAs(Resource):
    # /join/game_id?team=GREEN&player_name=pepito
    def put(self, game_id):
        team = request.args.get('team')
        player_name = request.args.get('player_name')
        return GameController.join_as(game_id, team, player_name)


api.add_resource(GamesResource, '/')
api.add_resource(GameDetails, '/<int:game_id>')                 # get details of a game by its id
api.add_resource(StartGame, '/start_game/<int:game_id>')        # launch initial crew and set status game as STARTED
api.add_resource(RefreshBoard, '/refresh_board/<int:game_id>')  # moves all aliens
api.add_resource(ActBoard, '/act_board/<int:game_id>')          # acts all aliens
api.add_resource(SpawnAliens, '/spawn_aliens/<int:game_id>')    # spawn of two aliens , one of each team in their areas
api.add_resource(JoinAs, '/join/<int:game_id>')                 # player joins to a game as blue or green player with his name

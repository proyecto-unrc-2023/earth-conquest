from app.backend.api import *
from app.backend.api.game_controller import GameController

from flask_restful import Resource, request
import json

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
        print(f"Received request to {request.path} with data: {request.data}")
        data = request.json
        print(f"Parsed JSON data: {data}")

        return GameController.set_alterator(game_id, data)


class NextState(Resource):
    def put(self, game_id):
        return GameController.next_state(game_id)


class JoinAs(Resource):
    # /join/game_id?team=GREEN&player_name=pepitoIsOut
    def put(self, game_id):
        team = request.args.get('team')
        player_name = request.args.get('player_name')
        return GameController.join_as(game_id, team, player_name)


class Sse(Resource):
    def get(self, game_id):
        return GameController.sse(game_id)


# get all games
api.add_resource(GamesResource, '/')
# get details of a game by its id
api.add_resource(GameDetails, '/<int:game_id>')
# launch initial crew and set status game as STARTED
api.add_resource(StartGame, '/start_game/<int:game_id>')
# moves and act all aliens, 3 secs interval
api.add_resource(NextState, '/next_state/<int:game_id>')
# player joins to a game as blue or green player with his name
api.add_resource(JoinAs, '/join/<int:game_id>')
# get position info of a game with its id
api.add_resource(IsFreePosition, '/is_free_position/<int:game_id>')
# set alterator on board of game with id
api.add_resource(SetAlterator, '/set_alterator/<int:game_id>')
# server sent events for game with id
api.add_resource(Sse, '/sse/<int:game_id>')

import json

from flask import jsonify, Response

from app.backend.models.board import BoardSchema
from app.backend.models.game import Game, GameSchema

games_dict = {}

'''
    This is the GameController class. It is used to control the game.
'''


class GameController:

    def get_game_by_id(id):
        game = games_dict.get(id)

        if game is None:
            message = json.dumps(
                {
                    "success": False,
                    "message": "Game not found with id: " + str(id)
                }
            )
            return Response(message, status=404, mimetype='application/json')

        game_schema = GameSchema()
        response = {
            "success": True,
            "message": "Game %d retrieved successfully" % id,
            "data": {
                "game": game_schema.dump(game)
            }
        }
        return jsonify(response)

    @staticmethod
    def create_new_game():
        game = Game()
        id = games_dict.__len__() + 1
        games_dict[id] = game

        message = json.dumps(
            {
                "success": True,
                "message": "Game created successfully",
                "data": {
                    "gameId": id
                }
            }
        )
        return Response(message, status=201, mimetype='application/json')

    def start_game(id):
        game = games_dict.get(id)
        if game is None:
            message = json.dumps(
                {
                    "success": False,
                    "message": "Game not found with id: " + str(id)
                }
            )
            return Response(message, status=404, mimetype='application/json')

        try:
            game.start_game()
            games_dict[id] = game
        except Exception as e:
            message = json.dumps(
                {
                    "success": False,
                    'errors': str(e)
                }
            )
            return Response(message, status=400, mimetype='application/json')

        response = {
            "success": True,
            "message": "Game %d started successfully" % id
        }
        return jsonify(response)

    '''
        This method updates a game.
    '''

    def update_game(self, game_id, data):
        game = games_dict.get(game_id)
        if game is None:
            message = json.dumps(
                {
                    "success": False,
                    "message": "Game not found with id: " + str(id)
                }
            )
            return Response(message, status=404, mimetype='application/json')

        game_data = {}
        if 'status' in data:
            game_data['status'] = data['status']
        if 'green_player' in data:
            game_data['green_player'] = data['green_player']
        if 'blue_player' in data:
            game_data['blue_player'] = data['blue_player']
        if 'board' in data:
            game_data['board'] = data['board']

        # Validate with schema
        game_schema = GameSchema()
        game = Game(**game_schema.load(game_data))

        # updates the game
        games_dict[game_id] = game

        response = {
            "success": True,
            "message": "Game %d updated successfully" % id
        }
        return jsonify(response)

    def get_all_games():
        games_data = []
        game_schema = GameSchema()

        for game_id, game in games_dict.items():
            game_data_entry = game_schema.dump(game)
            game_data_entry["game_id"] = game_id
            games_data.append(game_data_entry)

        response = {
            "success": True,
            "message": "All games retrieved successfully",
            "data": {
                "games": games_data
            }
        }
        return jsonify(response)

    # este metodo iria en board_controller ?
    def get_board_by_game_id(id):
        game = games_dict.get(id)

        if game is None:
            message = json.dumps(
                {
                    "success": False,
                    "message": "Game not found with id: " + str(id)
                }
            )
            return Response(message, status=404, mimetype='application/json')

        board = game.board
        board_schema = BoardSchema()
        response = {
            "success": True,
            "message": "Board of game %d retrieved successfully" % id,
            "data": {
                "board": board_schema.dump(board)
            }
        }
        return jsonify(response)
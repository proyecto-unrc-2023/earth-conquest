import json

from flask import jsonify, Response

from app.backend.models.board import BoardSchema
from app.backend.models.game import Game, GameSchema

games_dict = {}


class GameController:

    def get_game_by_id(id):
        game = games_dict.get(id)
        if game is None:
            message = json.dumps({'errors': "game not found with id: " + str(id)})
            return Response(message, status=404, mimetype='application/json')
        game_schema = GameSchema()

        return jsonify(game_schema.dump(game))

    def get_board_by_game_id(id):
        game = games_dict.get(id)
        if game is None:
            message = json.dumps({'errors': "game not found with id: " + str(id)})
            return Response(message, status=404, mimetype='application/json')
        board = game.board
        board_schema = BoardSchema()

        return jsonify(board_schema.dump(board))

    @staticmethod
    def create_new_game():
        game = Game()
        id = games_dict.__len__() + 1
        games_dict[id] = game
        message = json.dumps({'response': "game created successfully with id: " + str(id)})
        return Response(message, status=200, mimetype='application/json')

    def start_game(id):
        game = games_dict.get(id)
        if game is None:
            message = json.dumps({'errors': "game not found with id: " + str(id)})
            return Response(message, status=404, mimetype='application/json')

        try:
            game.start_game()
            games_dict[id] = game
        except Exception as e:
            message = json.dumps({'errors': str(e)})
            return Response(message, status=400, mimetype='application/json')

        game_schema = GameSchema()
        return jsonify(game_schema.dump(game))

    def update_game(self, data):
        game = games_dict.get(id)
        if game is None:
            message = json.dumps({'errors': "game not found with id: " + str(id)})
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

        # update game in db

        return game_data#jsonify({'success': 'true'})


    def get_all_games():
        game_data = []
        game_schema = GameSchema()

        for game in games_dict.values():
            # dump as json data the object `game`
            game_data.append(game_schema.dump(game))

        return jsonify({"games": game_data})

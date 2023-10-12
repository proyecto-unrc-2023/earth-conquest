from flask import jsonify, request

from app.backend.blueprints import *
from app.backend.models.game import Game, GameSchema

from flask_restful import Resource


class GamesResource(Resource):
    def get(self):
        # levantar conexion a la db
        get_all_games = "SELECT * FROM game"
        game_data = []
        game_schema = GameSchema()

        for game in Game.all(get_all_games):
            # dump as json data the object `game`
            game_data.append(game_schema.dump(game))

        return jsonify({"games": game_data})


class GameResource(Resource):

    def get(self, game_id):
        # levantar conexion a la db
        get_game_by_id = "SELECT * FROM game WHERE id = %s"
        #game = db.one(get_game_by_id, (game_id,))
        # close db
        if game is None:
            return "Juego no encontrado", 404
        game_schema = GameSchema()
        return jsonify(game_schema.dump(game))

    def post(self):
        # open db
        # esto solo para hacer jsonify y ver que guardó
        game_schema = GameSchema()
        game = Game()

        # add game to db
        # close db
        return jsonify(game_schema.dump(game))

    def put(self, game_id):
        # levantar conexion a db
        game = Game.find(game_id)
        if game is None:
            return "Juego no encontrado", 404

        data = request.json
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

    # set board dimentions
    def put(self, game_id, x, y):
        return "dimensions updated successfully"
    # act board
    #def put(self, game_id):
    # refresh board
    #def put(self, game_id):


api.add_resource(GamesResource, '/')
api.add_resource(GameResource, '/', '/<int:game_id>', '/<int:game_id>/board', '/<int:game_id>/board/<int:x>/<int:y>')


from flask import jsonify, request
from app.backend.blueprints import api
from app.backend.models.game import Game, GameSchema

from flask_restful import Resource


class GamesResource(Resource):
    def get(self):
        game_data = []

        return jsonify({"games": game_data})



api.add_resource(GamesResource, '/index')
# api.add_resource(GameResource, '/', '/<int:game_id>')


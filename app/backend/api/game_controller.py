import json

from flask import jsonify, Response
from app.backend.models.alterator import Alterator

from app.backend.models.board import BoardSchema
from app.backend.models.cell import CellSchema
from app.backend.models.direction import Direction
from app.backend.models.directioner import Directioner
from app.backend.models.game import Game, GameSchema
from app.backend.models.team import Team
from app.backend.models.teleporter import Teleporter

games_dict = {}

'''
    This is the GameController class. It is used to control the game.
'''


class GameController:

    def find_game(id):
        game = games_dict.get(id)
        if game is None:
            message = json.dumps(
                {
                    "success": False,
                    "message": "Game not found with id: %d" % id
                }
            )
            response = Response(message, status=404, mimetype='application/json') 
            return response



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

    def update_game(game_id, data):
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

    """
        This method checks if a given position is valid (free of modifiers/alterators and 
        not on any Ovni's range).
    """

    def is_valid_position(id, row, col):
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

        if board.is_free_position(row, col) and not board.is_pos_on_any_range(row, col):
            response = {
                "success": True,
                "message": f"Position ({row},{col}) of game with id {id} is valid"
            }
            return jsonify(response)
        else:
            message = json.dumps(
                {
                    "success": False,
                    "message": f"Position ({row},{col}) of game with id {id} is not valid"
                }
            )
            return Response(message, status=400, mimetype='application/json')


    """
        This method sets an alterator on the board if the positions are valid.
    """
    def set_alterator(id, data):
        response = GameController.find_game(id)
        if response is not None:
           return response
       
        game = games_dict[id]
        

        information = {
            "alterator": data.get("alterator").get("name"),
            "initPos": (data.get("alterator").get("positionInit").get("x"), data.get("alterator").get("positionInit").get("y")),
            "endPos": (data.get("alterator").get("positionEnd").get("x"), data.get("alterator").get("positionEnd").get("y")),
            "direction": data.get("alterator").get("direction"),
            "team": data.get("team")
        }

        if information["team"] == "BLUE":
            team = Team.BLUE
        if information["team"] == "GREEN":
            team = Team.GREEN

        if information["alterator"] == "directioner":
            alterator = GameController.create_directioner(information["direction"], information["initPos"])

        if information["alterator"] == "teleporter":
            alterator = Teleporter(information["initPos"], information["endPos"])

        if information["alterator"] == "trap":
            alterator = Alterator.TRAP

        try:
            if alterator == Alterator.TRAP:
                game.set_alterator(alterator, team, information["initPos"][0], information["initPos"][1])
            else:
                game.set_alterator(alterator, team)
        except Exception as e:
            message = json.dumps(
                {
                    "success": False,
                    'errors': str(e)
                }
            )
            return Response(message, status=400, mimetype='application/json')
        
        games_dict[id] = game
        print(games_dict[id].board.__str__())
        board_schema = BoardSchema()
        board = game.board
        response = {
            "success": True,
            "message": "Alterator successfully placed in game with id %d" % id,
            "data": {
                "board": board_schema.dump(board)
            }
        }

        return jsonify(response)



    """
        Creates and returns a directioner given its direction and initial position
    """
    def create_directioner(direction, initPos):
        if direction == "right":
            return Directioner(initPos, Direction.RIGHT)
        if direction == "left":
            return Directioner(initPos, Direction.LEFT)
        if direction == "downwards":
            return Directioner(initPos, Direction.DOWNWARDS)
        if direction == "upwards":
            return Directioner(initPos, Direction.UPWARDS)


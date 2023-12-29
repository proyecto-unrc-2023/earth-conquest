import json
import time

from flask import jsonify, Response
from app.backend.models.alterator import Alterator
from app.backend.models.direction import Direction
from app.backend.models.directioner import Directioner
from app.backend.models.game import Game, GameSchema, GameAliensSchema
from app.backend.models.team import Team
from app.backend.models.teleporter import Teleporter
from app.backend.api.redis_config import r


games_dict = {}
SPAWN_TIME = 3

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
            response = Response(message,
                                status=404,
                                mimetype='application/json')
            return response

    def get_game_by_id(id):
        response = GameController.find_game(id)
        if response is not None:
            return response

        game = games_dict.get(id)
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

        game_schema = GameSchema()
        message = json.dumps(
            {
                "success": True,
                "message": "Game created successfully",
                "data": {
                    "gameId": id,
                    "game": game_schema.dump(game)
                }
            }
        )
        return Response(message, status=201, mimetype='application/json')

    def start_game(id):
        response = GameController.find_game(id)
        if response is not None:
            return response

        game = games_dict.get(id)
        try:
            game.start_game()
            games_dict[id] = game
            game_schema = GameAliensSchema()
            r.set('game_status', json.dumps(game_schema.dump(game)))

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
            "gameId": str(id),
            "message": "Game started successfully"
        }
        return jsonify(response)

    '''
        This method updates a game.
    '''

    def next_state(id):
        response = GameController.find_game(id)
        if response is not None:
            return response

        game = games_dict.get(id)

        try:
            # REFRESH: Move aliens
            game.refresh_board()
            game.spawn_aliens_tick += 1
            games_dict[id] = game
            game_schema = GameAliensSchema()
            r.set('game_status', json.dumps(game_schema.dump(game)))

            time.sleep(2)

            # ACT: Act cells on board
            if game.spawn_aliens_tick % SPAWN_TIME == 0:
                game.spawn_aliens()

            game.act_board()
            games_dict[id] = game
            r.set('game_status', json.dumps(game_schema.dump(game)))

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
            "gameId": str(id),
            "message": "New state has been updated successfully"
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

    """
        This method checks if a given position is valid (free of modifiers/alterators and 
        not on any Ovni's range).
    """

    def is_free_position(id, row, col):

        response = GameController.find_game(id)
        if response is not None:
            return response

        game = games_dict.get(id)
        if game.is_free_position(row, col) and not game.is_pos_on_any_range(row, col):
            response = {
                "success": True,
                "message": f"Position ({row},{col}) of game {id} is free and is not on a range"
            }
            return jsonify(response)
        else:
            response = {
                "success": False,
                "message": f"Position ({row},{col}) of game {id} is not free or is on a range"
            }
            return jsonify(response)

    """
        This method sets an alterator on the board if the positions are valid.
    """

    def set_alterator(id, data):
        response = GameController.find_game(id)
        if response is not None:
            return response

        game = games_dict.get(id)

        info = {
            "alterator": data.get("alterator").get("name"),
            "initPos": (
                data.get("alterator").get("positionInit").get("x"), data.get("alterator").get("positionInit").get("y")),
            "endPos": (
                data.get("alterator").get("positionEnd").get("x"), data.get("alterator").get("positionEnd").get("y")),
            "direction": data.get("alterator").get("direction"),
            "team": data.get("team")
        }

        if info["team"] == "BLUE":
            team = Team.BLUE
        elif info["team"] == "GREEN":
            team = Team.GREEN
        else:
            message = json.dumps(
                {
                    "success": False,
                    "message": "Team not valid"
                }
            )
            return Response(message, status=400, mimetype='application/json')

        if info["alterator"] == "DIRECTIONER":
            alterator = GameController.create_directioner(info["direction"], info["initPos"])

        elif info["alterator"] == "TELEPORTER":
            alterator = Teleporter(info["initPos"], info["endPos"])

        elif info["alterator"] == "TRAP":
            alterator = Alterator.TRAP
        else:
            message = json.dumps(
                {
                    "success": False,
                    "message": "Alterator not valid. Must be a trap, a teleporter or a directioner"
                }
            )
            return Response(message, status=400, mimetype='application/json')

        try:
            if alterator == Alterator.TRAP:
                game.set_alterator(
                    alterator, team, info["initPos"][0], info["initPos"][1])
            else:
                game.set_alterator(alterator, team)
        except Exception as e:
            message = json.dumps(
                {
                    "success": False,
                    'errors': str(e)
                }
            )
            return Response(message, status=200, mimetype='application/json')

        games_dict[id] = game
        game_schema = GameAliensSchema()
        r.set('game_status', json.dumps(game_schema.dump(game)))

        response = {
            "success": True,
            "gameId": str(id),
            "message": "Alterator setted successfully"
        }
        return jsonify(response)

    def join_as(id, team, player_name):
        response = GameController.find_game(id)
        if response is not None:
            return response

        game = games_dict.get(id)
        try:
            if team == 'GREEN':
                game.join_as_green(player_name)
            elif team == 'BLUE':
                game.join_as_blue(player_name)
            else:
                message = json.dumps(
                    {
                        "success": False,
                        'errors': "Invalid team as argument, possible teams are: GREEN or BLUE"
                    }
                )
                return Response(message, status=400, mimetype='application/json')

            games_dict[id] = game  # save the game on the dict
            game_schema = GameSchema()
            r.set('game_status', json.dumps(game_schema.dump(game)))
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
            "message": "Player %s has joined to game: %d as %s player" % (player_name, id, team)
        }
        return jsonify(response)

    """
        Creates and returns a directioner given its direction and initial position
    """

    def create_directioner(direction, initPos):
        if direction == "RIGHT":
            return Directioner(initPos, Direction.RIGHT)
        if direction == "LEFT":
            return Directioner(initPos, Direction.LEFT)
        if direction == "DOWNWARDS":
            return Directioner(initPos, Direction.DOWNWARDS)
        if direction == "UPWARDS":
            return Directioner(initPos, Direction.UPWARDS)

    def sse(id):
        def sse_events():
            old_status = None

            while True:
                new_status = r.get('game_status')

                if old_status != new_status:
                    status_data = json.loads(new_status) if new_status else {}
                    yield f'data: {json.dumps(status_data)}\n\n'

                    old_status = new_status

        return Response(sse_events(), mimetype='text/event-stream')

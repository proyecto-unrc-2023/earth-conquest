import json

from flask import jsonify, Response

from app.backend.models.board import BoardSchema
from app.backend.models.game import Game, GameSchema
from app.backend.models.team import Team

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
        
        except Exception as e:
            message = json.dumps(
                {
                    "success": False,
                    'errors': str(e)
                }
            )
            return Response(message, status=400, mimetype='application/json')
        game_schema = GameSchema()
        response = {
            "success": True,
            "message": "Game %d started successfully" % id,
            "data": {
                "gameId": id,
                "game": game_schema.dump(game)
            }
        }
        return jsonify(response)

    '''
        This method updates a game.
    '''

    def refresh_board(id):
        response = GameController.find_game(id)
        if response is not None:
            return response
       
        game = games_dict.get(id)

        try:
            game.refresh_board()
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
            "message": "Board %d refreshes successfully" % id
        }
        return jsonify(response)
    
    '''
        This method acts a game.
    '''
    def act_board(id):
        response = GameController.find_game(id)
        if response is not None:
           return response
       
        game = games_dict.get(id)
        
        try:
            game.act_board()
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
            "message": "Board %d acts successfully" % id
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

    def spawn_aliens(id):
        response = GameController.find_game(id)
        if response is not None:
            return response

        game = games_dict.get(id)

        try:
            game.add_alien_to_range(Team.GREEN)
            game.add_alien_to_range(Team.BLUE)
            games_dict[id] = game   # save the game on the dict
        except Exception as e:
            message = json.dumps(
                {
                    "success": False,
                    'errors': str(e)
                }
            )
            return Response(message, status=400, mimetype='application/json')

        board_schema = BoardSchema()
        response = {
            "success": True,
            "message": "Aliens blue and green added successfully to game: %d" % id,
            "data": {
                "board": board_schema.dump(game.board)
            }
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



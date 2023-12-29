from flask import url_for
from app import create_app
import pytest


@pytest.fixture
def flask_app():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client


@pytest.fixture
def game_created(flask_app):
    """
    Creates a game in the games dictionary
    """
    url = '/games/'
    response = flask_app.post(url)
    game_id = response.json['data']['gameId']
    yield game_id


@pytest.fixture
def game_pre_started(flask_app, game_created):
    """
    Creates a game in the games dictionary
    And adds two players to the game
    """
    game_id = game_created
    url = f'games/join/{game_id}?team=BLUE&player_name=Donnie'
    flask_app.put(url)
    url = f'games/join/{game_id}?team=GREEN&player_name=Brasco'
    flask_app.put(url)
    yield game_id


def test_get_empty_all_games(flask_app):
    """
    When we make a GET request to the root of the API, we should get an empty list
    """
    # Arrange
    url = '/games/'

    # Act
    response = flask_app.get(url)

    # Assert
    assert response.status_code == 200
    assert response.json['success'] == True
    assert response.json['message'] == "All games retrieved successfully"
    assert response.json['data']['games'] == []


def test_get_all_games(flask_app, game_created):
    """
    Given we have a list of games in the games dictionary
    When we make a GET request to '/games/'
    Then we should get a list of all games
    """
    # Arrange
    url = '/games/'

    # Act
    response = flask_app.get(url)

    # Assert
    assert response.status_code == 200
    assert response.json['success'] == True
    assert response.json['message'] == "All games retrieved successfully"
    assert response.json['data']['games'] != []


def test_find_game_by_id(flask_app, game_created):
    """
    Given we have a list of games in the games dictionary
    When we make a GET request to '/games/id'
    Then we should get a list of all games
    """
    # Arrange
    id = game_created
    url = f'/games/{id}'

    # Act
    response = flask_app.get(url)

    # Assert
    assert response.status_code == 200
    assert response.json['success'] == True
    assert response.json['message'] == f"Game {id} retrieved successfully"
    assert response.json['data']['game'] != []


def test_find_nonexistent_game(flask_app):
    """
    Given we have an empty list of games in the games dictionary
    When we make a GET request to '/games/id'
    Then we should get a not found message
    """
    # Arrange
    id = 10
    url = f'/games/{id}'

    # Act
    response = flask_app.get(url)

    # Assert
    assert response.status_code == 404
    assert response.json['success'] == False
    assert response.json['message'] == f"Game not found with id: {id}"


def test_start_game(flask_app, game_pre_started):
    """
    Given we have a list of games in the games dictionary
    When we make a PUT request to '/games/start'
    Then we should get that the game was started successfully
    """
    # Arrange
    id = game_pre_started
    url = f'/games/start_game/{id}'

    # Act
    response = flask_app.put(url)

    # Assert
    assert response.status_code == 200
    assert response.json['gameId'] == f"{id}"
    assert response.json['success'] == True
    assert response.json['message'] == "Game started successfully"


def test_start_game_not_found(flask_app):
    """
    Given we have a empty list of games in the games dictionary
    When we make a PUT request to '/games/start'
    Then we should get an error message
    """
    # Arrange
    id = 10
    url = f'/games/start_game/{id}'

    # Act
    response = flask_app.put(url)

    # Assert
    assert response.status_code == 404
    assert response.json['success'] == False
    assert response.json['message'] == f"Game not found with id: {id}"


def test_start_game_without_player(flask_app, game_created):
    """
    Given we have a game with no players in the games dictionary
    When we make a PUT request to '/games/start'
    Then we should get an error message
    """
    # Arrange
    id = game_created
    url = f'/games/start_game/{id}'

    # Act
    response = flask_app.put(url)

    # Assert
    assert response.status_code == 400
    assert response.json['success'] is False
    assert response.json['errors'] == "can not start the game, some player is left or game status is not NOT_STARTED"


def test_join_as_blue(flask_app, game_created):
    """
    Given we have a game with no players in the games dictionary
    When we make a PUT request to '/games/join'
    Then we should get an success message
    """
    # Arrange
    id = game_created
    player = 'Donnie'
    team = 'BLUE'
    url = f'/games/join/{id}?team={team}&player_name={player}'

    # Act
    response = flask_app.put(url)

    # Assert
    assert response.status_code == 200
    assert response.json['success'] == True
    assert response.json['message'] == f"Player {player} has joined to game: {id} as {team} player"


def test_join_as_invalid_team(flask_app, game_created):
    """
    Given we have a game with no players in the games dictionary
    When we make a PUT request to '/games/join' with an invalid team
    Then we should get an error message
    """
    # Arrange
    id = game_created
    player = 'Edgarshino Do Baia Do Brasil'
    team = 'RED'
    url = f'/games/join/{id}?team={team}&player_name={player}'

    # Act
    response = flask_app.put(url)

    # Assert
    assert response.status_code == 400
    assert response.json['success'] == False
    assert response.json['errors'] == "Invalid team as argument, possible teams are: GREEN or BLUE"

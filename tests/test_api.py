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
    '''
    Creates a game in the games dictionary
    '''
    url = '/games/'
    response = flask_app.post(url)
    return response


def test_get_empty_all_games(flask_app):
    '''
    When we make a GET request to the root of the API, we should get an empty list
    '''
    # Arrange
    url = '/games/'

    # Act
    response = flask_app.get(url)

    # Assert
    assert response.status_code == 200
    assert response.json['success'] == True
    assert response.json['message'] == "All games retrieved successfully"
    assert response.json['data']['games'] == []


def tests_get_all_games(flask_app, game_created):
    '''
    Given we have a list of games in the games dictionary
    When we make a GET request to the root of the API
    Then we should get a list of all games
    '''
    # Arrange
    url = '/games/'

    # Act
    response = flask_app.get(url)

    # Assert
    assert response.status_code == 200
    assert response.json['success'] == True
    assert response.json['message'] == "All games retrieved successfully"
    assert response.json['data']['games'] != []

import pytest

from app.backend.models import team
from app.backend.models.alien import Alien
from app.backend.models.board import Board
from app.backend.models.game import Game


@pytest.fixture
def init_a_default_game():
    game = Game()
    return game


def test_set_invalid_board_dimensions(init_a_default_game):
    game = init_a_default_game
    with pytest.raises(Exception) as exc_info:
        game.set_board_dimensions(3, 6)
    assert str(exc_info.value) == "Invalid dimensions. Minimum board is 4x6. Max is 25x45"

    with pytest.raises(Exception) as exc_info:
        game.set_board_dimensions(4, 5)
    assert str(exc_info.value) == "Invalid dimensions. Minimum board is 4x6. Max is 25x45"

    with pytest.raises(Exception) as exc_info:
        game.set_board_dimensions(26, 45)
    assert str(exc_info.value) == "Invalid dimensions. Minimum board is 4x6. Max is 25x45"

    with pytest.raises(Exception) as exc_info:
        game.set_board_dimensions(25, 46)
    assert str(exc_info.value) == "Invalid dimensions. Minimum board is 4x6. Max is 25x45"


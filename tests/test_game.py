import pytest

from app.backend.models.alterator import Alterator
from app.backend.models.direction import Direction
from app.backend.models.directioner import Directioner
from app.backend.models.game import Game
from app.backend.models.team import Team
from app.backend.models.teleporter import Teleporter


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


def test_set_alterator_not_enough_aliens(init_a_default_game):
    game = init_a_default_game
    with pytest.raises(Exception) as exc_info:
        game.set_alterator(Alterator.TRAP, Team.GREEN)
    assert str(exc_info.value) == "not enough aliens to put a TRAP"

    directioner = Directioner((5, 1), Direction.RIGHT)
    with pytest.raises(Exception) as exc_info:
        game.set_alterator(directioner, Team.GREEN)
    assert str(exc_info.value) == "not enough aliens to put a Directioner"

    teleporter = Teleporter((4, 1), (6, 10))
    with pytest.raises(Exception) as exc_info:
        game.set_alterator(teleporter, Team.GREEN)
    assert str(exc_info.value) == "not enough aliens to put a Teleporter"
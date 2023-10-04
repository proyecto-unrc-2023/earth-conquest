import pytest

from app.backend.models import team
from app.backend.models.alien import Alien
from app.backend.models.board import Board


@pytest.fixture
def init_a_default_board():
    board = Board()
    return board


def test_att(init_a_default_board):
    board = init_a_default_board
    assert board.rows == 10
    assert board.cols == 15
    assert board.green_ovni_range == (3, 3)
    assert board.blue_ovni_range == (6, 11)


def test_set_alien(init_a_default_board):
    board = init_a_default_board
    alien = Alien(team.Team.GREEN)
    board.set_alien(5, 5, alien)
    assert board.aliens.__len__() == 1
    assert board.aliens[(5, 5)] == [alien]

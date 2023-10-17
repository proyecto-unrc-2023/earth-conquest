import pytest

from app.backend.models import team
from app.backend.models.alien import Alien
from app.backend.models.board import Board, GREEN_OVNI_LIFE, BLUE_OVNI_LIFE
from app.backend.models.directioner import Directioner
from app.backend.models.modifier import Modifier
from app.backend.models.team import Team
from app.backend.models.teleporter import Teleporter


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


def test_blue_alien_attack_green_base(init_a_default_board):
    board = init_a_default_board
    alien = Alien(Team.BLUE, 3)
    board.set_alien(2, 2, alien)
    board.green_ovni_life = 7
    board.act_board()
    assert board.green_ovni_life == (7 - alien.eyes)
    assert not alien in board.aliens


def test_remove_alien_from_board(init_a_default_board):
    board = init_a_default_board
    alien = Alien(Team.BLUE, 3)
    board.set_alien(4, 5, alien)
    board.remove_alien_from_board(4, 5, alien)
    assert not alien in board.aliens


def test_remove_only_one_alien_from_board(init_a_default_board):
    board = init_a_default_board
    alien = Alien(Team.BLUE, 3)
    board.set_alien(4, 5, alien)
    board.set_alien(5, 5, alien)
    board.remove_alien_from_board(4, 5, alien)
    assert not board.aliens == {}
    assert board.aliens[(5, 5)][0] == alien


def test_green_alien_attack_blue_base(init_a_default_board):
    board = init_a_default_board
    alien = Alien(Team.GREEN, 3)
    board.set_alien(6, 11, alien)

    assert alien in board.get_cell(6, 11).aliens

    board.blue_ovni_life = 5
    board.act_board()

    assert board.blue_ovni_life == (5 - alien.eyes)
    assert board.aliens[6, 11] == []

    assert not alien in board.aliens
    assert not alien in board.get_cell(6, 11).aliens


def test_green_alien_in_green_base_and_blue_alien_in_blue_base(init_a_default_board):
    board = init_a_default_board
    alien = Alien(Team.GREEN, 3)
    alien2 = Alien(Team.BLUE, 3)
    board.set_alien(3, 3, alien)
    board.set_alien(6, 11, alien2)
    board.act_board()

    assert board.green_ovni_life == GREEN_OVNI_LIFE
    assert board.blue_ovni_life == BLUE_OVNI_LIFE

    assert (3, 3) in board.aliens and board.aliens[(3, 3)] == [alien]
    assert (6, 11) in board.aliens and board.aliens[(6, 11)] == [alien2]


def test_get_invalid_pos(init_a_default_board):
    board = init_a_default_board
    with pytest.raises(Exception) as exc_info:
        board.get_cell(11, 15)
    assert str(exc_info.value) == "Index out of range"
    with pytest.raises(Exception) as exc_info:
        board.get_cell(10, 16)
    assert str(exc_info.value) == "Index out of range"


def test_set_invalid_trap(init_a_default_board):
    board = init_a_default_board
    with pytest.raises(Exception) as exc_info:
        board.set_trap(1, 1)
    assert str(exc_info.value) == "Position isn't free or valid"
    with pytest.raises(Exception) as exc_info:
        board.set_trap(10, 15)
    assert str(exc_info.value) == "Position isn't free or valid"


def test_set_invalid_teleporter(init_a_default_board):
    board = init_a_default_board
    teleporter = Teleporter((1, 1), (7, 7))
    with pytest.raises(Exception) as exc_info:
        board.set_teleporter(teleporter)
    assert str(exc_info.value) == "Positions of the teleporter aren't free or valid"


def test_set_invalid_directioner(init_a_default_board):
    board = init_a_default_board
    directioner = Directioner((1, 1))
    with pytest.raises(Exception) as exc_info:
        board.set_directioner(directioner)
    assert str(exc_info.value) == "Positions of the directioner aren't free or valid"

def test_remove_alien_from_board(init_a_default_board):
    board = init_a_default_board
    alien = Alien(Team.GREEN)
    board.set_alien(1, 1, alien)
    with pytest.raises(Exception) as exc_info:
        board.remove_alien_from_board(8, 8, alien)
    assert str(exc_info.value) == "alien not found"
    board.remove_alien_from_board(1, 1, alien)
    assert board.aliens[(1, 1)] == []
    assert board.get_cell(1, 1).aliens == []

def test_cant_move_alien(init_a_default_board):
    board = init_a_default_board
    alien = Alien(Team.GREEN)
    board.set_alien(1, 1, alien)
    with pytest.raises(Exception) as exc_info:
        board.move_alien(8, 8, alien)
    assert str(exc_info.value) == "alien not found in position"








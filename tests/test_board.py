import pytest

from app.backend.models import team
from app.backend.models.alien import Alien
from app.backend.models.board import Board, GREEN_OVNI_LIFE, BLUE_OVNI_LIFE
from app.backend.models.team import Team


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


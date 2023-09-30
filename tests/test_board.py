from app.backend.models.board import Board
from app.backend.models.cell import Cell


def test_create_a_board():
    board = Board(10, 10, 2)
    assert isinstance(board.get_cell(1, 1), Cell)


from behave import *

from app.backend.models.application import Application
from app.backend.models.board import Board
from app.backend.models.game import Game
from app.backend.models.game_enum import TGame
from app.backend.models.modifier import Modifier
from app.backend.models.team import Team


@given(u'that the application was initiated')
def step_impl(context):
    context.app = Application()


@given(u'player Juan has created a game as blue player')
def step_impl(context):
    context.game = Game(10, 15)
    context.game.join_as_blue()


@given(u'player Jose has joined the game as green player')
def step_impl(context):
    context.game.join_as_green()


@given(u'the game board dimension is 10 by 15')
def step_impl(context):
    assert context.game.board.rows == 10
    assert context.game.board.cols == 15


@given(u'two randomly orientated mountains ranges are randomly generated on free positions')
def step_impl(context):
    pass


@given(u'two killers are randomly generated on free positions')
def step_impl(context):
    pass


@given(u'two multipliers are randomly generated on free positions')
def step_impl(context):
    pass


@given(u'the game has not started')
def step_impl(context):
    assert context.game.status == TGame.NOT_STARTED


@when(u'the game is started')
def step_impl(context):
    context.game.status = TGame.STARTED


@then(u'the placed modifiers end up positioned outside of each team\'s area')
def step_impl(context):
    board = context.game.board
    modifiers = []
    # ciclo toda la matriz
    for i, row in enumerate(board.board):
        for j, cell in enumerate(row):
            if cell.modifier is not None:   # si la celda tiene un modifier
                modifiers.append((i, j))
    for pos in modifiers:
        assert not board.is_free_position(pos[0], pos[1])
        assert not board.is_pos_on_any_range(pos[0], pos[1])


@then(u'six aliens of each team are setted on their respectively areas')
def step_impl(context):
    board = context.game.board
    context.game.set_initial_crew()
    blue_aliens = []
    green_aliens = []
    for position, aliens_in_position in board.aliens.items():
        for alien in aliens_in_position:
            if alien.team == Team.BLUE:
                blue_aliens.append(position)
            else:
                green_aliens.append(position)
    assert blue_aliens is not [] and green_aliens is not []
    for pos in blue_aliens:
        assert board.is_position_in_blue_range(pos[0], pos[1])

    for pos in green_aliens:
        assert board.is_position_in_green_range(pos[0], pos[1])

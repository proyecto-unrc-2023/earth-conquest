from behave import *
from app.backend.models.alien import Alien
from app.backend.models.directioner import Directioner
from app.backend.models.direction import Direction
from app.backend.models.team import Team


@given(u'the Directioner is positioned horizontally on the cells ({x1:d},{y1:d}), ({x2:d},{y2:d}) and ({x3:d},{y3:d})')
def step_impl(context, x1, y1, x2, y2, x3, y3):
    context.directioner = Directioner((x1, y1), Direction.RIGHT)
    context.game.board.set_directioner(context.directioner)


@given(u'a green alien is positioned on the cell ({row:d},{col:d})')
def step_impl(context, row, col):
    board = context.game.board
    context.alien = Alien(Team.GREEN)
    board.set_alien(row, col, context.alien)


@given(u'the alien moves to an adjacent cell, this one being cell ({row:d},{col:d})')
def step_impl(context, row, col):
    context.game.board.remove_alien_from_board(row, col-1, context.alien)
    context.game.board.set_alien(row, col, context.alien)


@then(u'the alien moves to the cell ({row:d},{col:d})')
def step_impl(context, row, col):
    new_pos = context.game.board.get_alien_position(context.alien)
    assert(new_pos == (row, col))

@then(u'the alien stays on it\'s cell (3,14)')
def step_impl(context):
    new_pos = context.game.board.get_alien_position(context.alien)
    assert(new_pos == (3, 14))



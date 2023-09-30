from behave import *

from app.backend.models.application import Application
from app.backend.models.board import Board


@given(u'that the application was initiated')
def step_impl(context):
    context.app = Application()


@given(u'player Juan has created a game as blue player')
def step_impl(context):
    context.game = context.app.new_game()
    context.game.join_as_blue()


@given(u'player Jose has joined the game as green player')
def step_impl(context):
    context.game.join_as_green()


# parameterized test
@given(u'the game board dimension is {rows:d} by {cols:d}')
def step_impl(context, rows, cols):
    context.board = Board(rows, cols)


@given(u'the game has not started')
def step_impl(context):
    context.game.set_mode('MODE.NOT_STARTED')


@when(u'the game is started')
def step_impl(context):
    context.game.set_mode('MODE.STARTED')


@when(u'a vertical mountain obstacle is randomly generated on (2,5)')
def step_impl(context):
    context.game.board.set_cell((2, 5), 'MOUNTAIN')
    context.game.board.set_cell((2, 6), 'MOUNTAIN')
    context.game.board.set_cell((2, 7), 'MOUNTAIN')


@when(u'a horizontal mountain obstacle is randomly generated on (12,5)')
def step_impl(context):
    context.game.board.set_cell((12, 5), 'MOUNTAIN')
    context.game.board.set_cell((13, 2), 'MOUNTAIN')
    context.game.board.set_cell((14, 5), 'MOUNTAIN')


# testing tablita
@then(u'both players should see the following board')
def step_impl(context):
    table = context.table

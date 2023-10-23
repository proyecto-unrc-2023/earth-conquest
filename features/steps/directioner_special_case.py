from behave import *
from app.backend.models.alien import Alien
from app.backend.models.alterator import Alterator

from app.backend.models.board import Board
from app.backend.models.game import Game
from app.backend.models.directioner import Directioner
from app.backend.models.direction import Direction
from app.backend.models.team import Team
from app.backend.models.teleporter import Teleporter
from features.environment import table_to_string



@given(u'the Directioner is positioned horizontally on the cells (3,12), (3,13) and (3,14)')
def step_impl(context):
    context.directioner = Directioner((3,12), Direction.RIGHT)
    context.game.board.set_directioner(context.directioner)


@given(u'a green alien is positioned on the cell (3,11)')
def step_impl(context):
    board = context.game.board
    context.alien = Alien(Team.GREEN)
    board.set_alien(3, 11, context.alien)


@given(u'the alien moves to an adjacent cell, this one being cell (3,12)')
def step_impl(context):
    context.game.board.remove_alien_from_board(3, 11, context.alien)
    context.game.board.set_alien(3, 12, context.alien)


@then(u'the alien moves to the cell (3,13)')
def step_impl(context):
    new_pos = context.game.board.get_alien_position(context.alien)
    assert(new_pos == (3, 13))


@then(u'the alien moves to the cell (3,14)')
def step_impl(context):
    new_pos = context.game.board.get_alien_position(context.alien)
    assert(new_pos == (3, 14))


@then(u'the alien stays on it\'s cell (3,14)')
def step_impl(context):
    new_pos = context.game.board.get_alien_position(context.alien)
    assert(new_pos == (3, 14))



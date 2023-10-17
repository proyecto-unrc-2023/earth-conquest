from behave import *
from app.backend.models.alien import Alien
from app.backend.models.alterator import Alterator

from app.backend.models.application import Application
from app.backend.models.board import Board
from app.backend.models.game import Game
from app.backend.models.directioner import Directioner
from app.backend.models.direction import Direction
from app.backend.models.team import Team
from app.backend.models.teleporter import Teleporter
from features.environment import table_to_string

@given(u'the game has started')
def step_impl(context):
    context.game = Game()
    context.game.board = Board.from_string(table_to_string(context.table))
    


@given(u'the Directioner is positioned horizontally on the cells (5,1), (5,2) and (5,3)')
def step_impl(context):
    context.directioner = Directioner((5, 1), Direction.RIGHT)
    context.game.board.set_directioner(context.directioner)


@given(u'a green alien is positioned on the cell (4, 1)')
def step_impl(context):
    board = context.game.board
    context.alien = Alien(Team.GREEN)
    board.set_alien(4, 1, context.alien)


@given(u'the alien moves to an adjacent cell, this one being cell (5,1)')
def step_impl(context):
    context.game.board.remove_alien_from_board(4, 1, context.alien)
    context.game.board.set_alien(5, 1, context.alien)


@then(u'the alien moves to the cell (5,2)')
def step_impl(context):
    new_pos = context.game.board.get_alien_position(context.alien)
    assert(new_pos == (5, 2))


@then(u'the alien moves to the cell (5, 3)')
def step_impl(context):
    new_pos = context.game.board.get_alien_position(context.alien)
    assert(new_pos == (5, 3))


@then(u'the alien moves to the cell (5, 4)')
def step_impl(context):
    new_pos = context.game.board.get_alien_position(context.alien)
    assert(new_pos == (5, 4))



# TELEPORTER
@given(u'the Teleporter\'s door and exit are positioned on the cells (4,1) and (6,10) respectively')
def step_impl(context):
    context.teleporter = Teleporter((4, 1), (6,10))
    context.game.board.set_teleporter(context.teleporter)


@given(u'a green alien is positioned on the cell (3, 1)')
def step_impl(context):
    board = context.game.board
    context.alien = Alien(Team.GREEN)
    board.set_alien(3, 1, context.alien)


@given(u'the alien moves to an adjacent cell, this one being cell (4,1)')
def step_impl(context):
    context.game.board.remove_alien_from_board(3, 1, context.alien)
    context.game.board.set_alien(4, 1, context.alien)


@then(u'the alien is teleported to the cell (6,10)')
def step_impl(context):
    new_pos = context.game.board.get_alien_position(context.alien)
    assert(new_pos == (6, 10))



# TRAP
@given(u'the Trap is positioned on the cell (4,3)')
def step_impl(context):
    context.game.board.set_trap(4,3)


@given(u'a green alien is positioned on the cell (3, 3)')
def step_impl(context):
    board = context.game.board
    context.alien = Alien(Team.GREEN)
    board.set_alien(3, 3, context.alien)


@given(u'the alien moves to an adjacent cell, this one being cell (4,3)')
def step_impl(context):
    context.game.board.remove_alien_from_board(3, 3, context.alien)
    context.game.board.set_alien(4, 3, context.alien)


@when(u'the system acts')
def step_impl(context):
    context.game.act_board()


@then(u'the alien dies')
def step_impl(context):
    new_pos = context.game.board.get_alien_position(context.alien)
    print(new_pos)
    assert(new_pos == None)
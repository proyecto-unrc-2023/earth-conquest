from behave import *
from app.backend.models.alien import Alien
from app.backend.models.alterator import Alterator

from app.backend.models.application import Application
from app.backend.models.game import Game
from app.backend.models.directioner import Directioner
from app.backend.models.direction import Direction
from app.backend.models.team import Team
from app.backend.models.teleporter import Teleporter

@given(u'the game has started')
def step_impl(context):
    context.game = Game()


@given(u'the Directioner is positioned horizontally on the cells (6,2), (6,3) and (6,4)')
def step_impl(context):
    context.directioner = Directioner((6,2), Direction.RIGHT)
    context.game.board.set_directioner(context.directioner)


@given(u'the alien is positioned on the cell (5,2)')
def step_impl(context):
    context.alien = Alien(Team.BLUE)
    context.game.board.set_alien(5, 2, context.alien)


@given(u'the alien moves to an adjacent cell, this one being cell (6,2)')
def step_impl(context):
    context.game.board.set_alien(6, 2, context.alien)
    context.game.board.remove_alien_from_board(5, 2, context.alien)


@when(u'the system refreshes')
def step_impl(context):
    context.game.refresh_board()


@then(u'the alien moves to the cell (6,3)')
def step_impl(context):
    new_pos = context.game.board.get_alien_position(context.alien)
    assert(new_pos == (6,3))


@when(u'the system refreshes again')
def step_impl(context):
    context.game.refresh_board()


@then(u'the alien moves to the cell (6,4)')
def step_impl(context):
    new_pos = context.game.board.get_alien_position(context.alien)
    assert(new_pos == (6,4))


# TELEPORTER
@given(u'the Teleporter\'s door is positioned on the cell (8,3) and it\'s tail on the cell (9,9)')
def step_impl(context):
    context.teleporter = Teleporter((8,3), (9,9))
    context.game.board.set_teleporter(context.teleporter)


@given(u'an alien is positioned on the cell (7,3)')
def step_impl(context):
    context.alien = Alien(Team.GREEN)
    context.game.board.set_alien(7, 3, context.alien)


@given(u'the alien moves to an adjacent cell, this one being cell (8,3)')
def step_impl(context):
    context.game.board.set_alien(8, 3, context.alien)
    context.game.board.remove_alien_from_board(7, 3, context.alien)


@then(u'the alien is teleported to the cell (9,9)')
def step_impl(context):
    new_pos = context.game.board.get_alien_position(context.alien)
    assert(new_pos == (9,9))


# TRAP
@given(u'the Trap is positioned on the cell (3,11)')
def step_impl(context):
    context.game.board.set_trap(3,11)
    

@given(u'the alien is positioned on the cell (2,11)')
def step_impl(context):
    context.alien = Alien(Team.BLUE)
    context.game.board.set_alien(2, 11, context.alien)


@given(u'the alien moves to an adjacent cell, this one being cell (3,11)')
def step_impl(context):
    context.game.board.set_alien(3, 11, context.alien)
    context.game.board.remove_alien_from_board(2, 11, context.alien)


@when(u'the system acts')
def step_impl(context):
    context.game.act_board()


@then(u'the alien dies')
def step_impl(context):
    new_pos = context.game.board.get_alien_position(context.alien)
    assert(new_pos == None)
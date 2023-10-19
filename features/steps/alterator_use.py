from behave import *
from app.backend.models.alien import Alien
from app.backend.models.alterator import Alterator

from app.backend.models.board import Board
from app.backend.models.game import Game, INIT_CREW
from app.backend.models.directioner import Directioner
from app.backend.models.direction import Direction
from app.backend.models.team import Team
from app.backend.models.teleporter import Teleporter
from features.environment import table_to_string


@given(u'a game has been created')
def step_impl(context):
    context.game = Game()
    context.game.board = Board.from_string(table_to_string(context.table))


@when(u'a green alien is positioned on the cell ({row:d}, {col:d})')
def step_impl(context, row, col):
    board = context.game.board
    context.alien = Alien(Team.GREEN)
    context.alien_pos = (row, col)
    board.set_alien(row, col, context.alien)


@when(u'green player set a horizontally Directioner on the cells (5,1), (5,2) and (5,3)')
def step_impl(context):
    context.directioner = Directioner((5, 1), Direction.RIGHT)
    context.game.set_alterator(context.directioner, Team.GREEN)


@when(u'green player set a Teleporter on the cell (4,1) for entry door and (6,10) for exit')
def step_impl(context):
    context.teleporter = Teleporter((4, 1), (6, 10))
    context.game.set_alterator(context.teleporter, Team.GREEN)


@when(u'green player set a Trap on the cell ({row:d}, {col:d})')
def step_impl(context, row, col):
    context.game.set_alterator(Alterator.TRAP, Team.GREEN, row, col)


@when(u'the alien moves to an adjacent cell, this one being cell ({row:d}, {col:d})')
def step_impl(context, row, col):
    x = context.alien_pos[0]
    y = context.alien_pos[1]
    context.game.board.remove_alien_from_board(x, y, context.alien)
    context.game.board.set_alien(row, col, context.alien)


@then(u'the alien moves to the cell ({row:d}, {col:d})')
def step_impl(context, row, col):
    new_pos = context.game.board.get_alien_position(context.alien)
    assert new_pos == (row, col)


@then(u'the alien dies')
def step_impl(context):
    pos = context.game.board.get_alien_position(context.alien)
    assert pos is None


@then(u'{cant:d} green aliens dies')
def step_impl(context, cant):
    green_aliens = 0
    for pos, aliens_on_cell in context.game.board.aliens.items():
        for alien in aliens_on_cell:
            if alien.team is Team.GREEN:
                green_aliens += 1
    assert INIT_CREW - cant == green_aliens

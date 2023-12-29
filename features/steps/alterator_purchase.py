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


@when(u'green player sets a Directioner horizontally on the cells (5,1), (5,2) and (5,3)')
def step_impl(context):
    context.directioner = Directioner((5, 1), Direction.RIGHT)
    context.game.set_alterator(context.directioner, Team.GREEN)


@when(u'green player sets a Teleporter on the cell (4,1) for entry door and (6,10) for exit')
def step_impl(context):
    context.teleporter = Teleporter((4, 1), (6, 10))
    context.game.set_alterator(context.teleporter, Team.GREEN)


@when(u'green player sets a Trap on the cell ({row:d}, {col:d})')
def step_impl(context, row, col):
    context.game.set_alterator(Alterator.TRAP, Team.GREEN, row, col)


@then(u'{cant:d} green aliens die')
def step_impl(context, cant):
    green_aliens = 0
    for pos, aliens_on_cell in context.game.aliens_dict().items():
        for alien in aliens_on_cell:
            if alien.team is Team.GREEN:
                green_aliens += 1
    assert INIT_CREW - cant == green_aliens
from behave import given, then, when

from app.backend.models.alien import Alien
from app.backend.models.board import Board
from app.backend.models.modifier import Modifier
from app.backend.models.team import Team


@given(u'the aliens has been generate in the board')
def step_impl(context):
    board = Board(10, 10, 2)
    context.alien = Alien(Team.BLUE)
    board.set_alien(2, 2, context.alien)
    context.board = board


@given(u'there is an "{modifier}" in the square (2, 2)')
def step_impl(context, modifier):
    if context.board.is_free_position(2, 2):
        if modifier == "multiplier":
            context.board.set_modifier(Modifier.MULTIPLIER, 2, 2)
        else:
            context.board.set_modifier(Modifier.KILLER, 2, 2)
    else:
        if modifier == "multiplier":
            context.board.board[2][2].modifier = Modifier.MULTIPLIER
        else:
            context.board.board[2][2].modifier = Modifier.KILLER


@given(u'alien arrive at the square (2, 2)')
def step_impl(context):
    alien = Alien(Team.BLUE)
    context.alien = alien
    context.board.set_alien(2, 2, alien)


@when(u'"{modifier}" activates')
def step_when(context, modifier):
    cell = context.board.get_cell(2, 2)
    cell.action()
    context.board.board[2][2] = cell


@then(u'"{action_modifier}" and "{result_modifier}"')
def step_when(context, action_modifier, result_modifier):
    cell = context.board.get_cell(2, 2)
    if cell.modifier == Modifier.MULTIPLIER:
        assert len(cell.aliens) == 2
    else:
        assert not cell.aliens

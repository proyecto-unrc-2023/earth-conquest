from behave import *

from app.backend.models.alien import Alien
from app.backend.models.board import Board


@given(u'the aliens has been generated')
def step_impl(context):
    context.alien = Alien(1, 'BLUE')


@given(u'there is an aliens in the square (2,2)')
def step_impl(context):
    board = Board()
    board[2][2].get_cell().get_aliens().add(context.alien)
    context.board = board


@given(u'aliens arrive at a \'{modifier}\'')
def step_given(context, modifier):
    if isinstance(modifier, Cloner):
        context.modifier = Cloner()
    elif isinstance(modifier, Killer):
        context.modifier = Killer()


@when(u'\'{modifier}\' activates')
def step_when(context):
    context.modifier.activate()


@then(u'\'{action_modifier}\'')
def step_then(context):
    if isinstance(context.modifier, Cloner):
        context.modifier.clone(context.alien)
    elif isinstance(context.modifier, Killer):
        context.modifier.kill(context.alien)


@then(u'in the square \'{result_modifier}\'')
def step_then_in_square(context):
    if isinstance(context.modifier, Cloner):
        aliens = context.board.get_position(2, 2).get_aliens()
        assert aliens[0].__eq__(context.alien)
        assert isinstance(aliens[1], Alien)
    elif isinstance(context.modifier, Killer):
        aliens = context.board.get_position(2, 2).get_aliens()
        assert aliens[0] is None

from behave import *

from app.backend.models.alien import Alien
from app.backend.models.board import Board
from app.backend.models.team import Team


# TODO agregar los :d o equivalente a cada parametro
# TODO mejorar los tests


@given(u'the aliens has been generated')
def step_impl(context):
    context.alien1 = Alien(Team.BLUE)
    context.alien2 = Alien(Team.GREEN)


@given(u'there are two aliens in the square (2,2)')
def step_impl(context):
    board = Board()
    board[2][2] = [context.alien1, context.alien2]
    context.board = board


@given(u'alien \'1\' is from team \'blue\'')
def step_impl(context):
    context.alien1.set_team('blue')


@given(u'alien \'2\' is from team \'green\'')
def step_impl(context):
    context.alien1.set_team('green')


@given(u'the number of eyes of alien \'1\' is "{alien1_eyes:d}"')
def step_impl(context, alien1_eyes):
    context.alien1.set_eyes(alien1_eyes)


@given(u'the number of eyes of alien \'2\' is "{alien2_eyes:d}"')
def step_impl(context, alien2_eyes):
    context.alien2.set_eyes(alien2_eyes)


@when(u'they fight')
def step_impl(context):
    context.board.get_cell(2, 2).fight()


@then(u'alien \'1\' "{outcome1}"')
def step_impl(context, outcome1):
    # TODO get aliens
    if outcome1 == "dies":
        assert (not context.alien1.is_live()) and (context.board.get_position(2, 2).aliens == context.alien2)
    elif outcome1 == "lives":
        assert (context.alien1.is_live()) and (context.board.get_position(2, 2).aliens == context.alien1)
    else:
        assert (context.board.get_position(2, 2).aliens is None) and (not context.alien1.is_alive()) and (
            not context.alien2.is_alive())


@then(u'alien \'2\' "{outcome2}"')
def step_impl(context, outcome2):
    if outcome2 == "dies":
        assert (not context.alien2.is_live()) and (context.board.get_position(2, 2).get_aliens() == context.alien1)
    elif outcome2 == "lives":
        assert (context.alien2.is_live()) and (context.board.get_position(2, 2) == context.alien2)
    else:
        assert (context.board.get_position(2, 2) is None) and (not context.alien1.is_alive()) and (
            not context.alien2.is_alive())


@then(u'I should have "{aliens_left:d}" less aliens')
def step_impl(context, aliens_left):
    actual_aliens_left = context.board.get_cant_aliens()
    expected_aliens_left = actual_aliens_left - int(aliens_left)
    assert actual_aliens_left == expected_aliens_left

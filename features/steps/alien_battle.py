from behave import given, when, then

from app.backend.models.alien import Alien
from app.backend.models.board import Board
from app.backend.models.team import Team


@given(u'the aliens has been generated')
def step_impl(context):
    context.alien1 = Alien(Team.BLUE)
    context.alien2 = Alien(Team.GREEN)


@given(u'there are two aliens in the square (2,2)')
def step_impl(context):
    board = Board(10, 10, 1)
    board.set_alien(2, 2, context.alien1)
    board.set_alien(2, 2, context.alien2)
    context.board = board


@given(u'alien 1 is from team BLUE')
def step_impl(context):
    assert context.board.get_cell(2, 2).aliens[0].team == Team.BLUE


@given(u'alien 2 is from team GREEN')
def step_impl(context):
    assert context.board.get_cell(2, 2).aliens[1].team == Team.GREEN


@given(u'that the number of eyes of alien 1 is {alien1_eyes:d}')
def step_impl(context, alien1_eyes):
    cell = context.board.get_cell(2, 2)
    alien = cell.aliens[0]
    add_aliens_eyes = int(alien1_eyes - 1)
    alien.add_eyes(add_aliens_eyes)
    alien_eyes = alien.eyes
    context.board.get_cell(2, 2).aliens[0] = alien

    assert alien_eyes == alien1_eyes


@given(u'the number of eyes of alien 2 is {alien2_eyes:d}')
def step_impl(context, alien2_eyes):
    cell = context.board.get_cell(2, 2)
    alien = cell.aliens[1]
    alien.add_eyes(alien2_eyes - 1)
    alien_eyes = alien.eyes
    context.board.get_cell(2, 2).aliens[1] = alien

    assert alien_eyes == alien2_eyes


@when(u'they fight')
def step_impl(context):
    cell = context.board.get_cell(2, 2)
    cell.fight()
    context.board.board[2][2] = cell


@then(u'alien 1 "{outcome1}"')
def step_impl(context, outcome1):
    cell = context.board.get_cell(2, 2)
    aliens = cell.aliens
    if len(aliens) > 0:
        if outcome1 == "dies":
            assert aliens[0] is context.alien2
        else:
            assert aliens[0] is context.alien1
    else:
        assert aliens == []


@then(u'alien 2 "{outcome2}"')
def step_impl(context, outcome2):
    cell = context.board.get_cell(2, 2)
    aliens = cell.aliens
    if len(aliens) > 0:
        if outcome2 == "dies":
            assert aliens[0] is context.alien1
        else:
            assert aliens[0] is context.alien2
    else:
        assert aliens == []


@then(u'I should have {aliens_left:d} less aliens')
def step_impl(context, aliens_left):
    expected_aliens = 2 - aliens_left
    actual_aliens = len(context.board.get_cell(2, 2).aliens)
    assert expected_aliens.__eq__(actual_aliens)

from behave import given, when, then

from app.backend.models.alien import Alien
from app.backend.models.board import Board
from app.backend.models.team import Team


@given(u'there are aliens in the square (2,2) of the same team')
def step_impl(context):
    board = Board(10, 10, 1)
    context.alien2 = Alien(Team.BLUE)
    board.set_alien(2, 2, context.alien1)
    board.set_alien(2, 2, context.alien2)
    context.board = board

    assert context.board.get_cell(2, 2).all_aliens_same_team()


@given(u'the number of eyes of alien 3 is {alien3_eyes:d}')
def step_impl(context, alien3_eyes):
    cell = context.board.get_cell(2, 2)
    cell.add_alien(Team.BLUE)
    alien = cell.aliens[2]
    add_aliens_eyes = int(alien3_eyes - 1)
    alien.add_eyes(add_aliens_eyes)
    alien_eyes = alien.eyes
    context.board.get_cell(2, 2).aliens[2] = alien

    assert alien_eyes == alien3_eyes


@given(u'the number of eyes of alien 4 is {alien4_eyes:d}')
def step_impl(context, alien4_eyes):
    cell = context.board.get_cell(2, 2)
    cell.add_alien(Team.BLUE)
    alien = cell.aliens[3]
    add_aliens_eyes = int(alien4_eyes - 1)
    alien.add_eyes(add_aliens_eyes)
    alien_eyes = alien.eyes
    context.board.get_cell(2, 2).aliens[3] = alien

    assert alien_eyes == alien4_eyes


@when(u'they reproduce')
def step_impl(context):
    cell = context.board.get_cell(2, 2)
    cell.reproduce()
    context.board.board[2][2] = cell


@then(u'the alien resulting from reproduction should "{survive_or_die}"')
def step_impl(context, survive_or_die):
    context.survive_or_die = survive_or_die
    if survive_or_die == "survive":
        assert len(context.board.get_cell(2, 2).aliens) == 1
        assert context.board.get_cell(2, 2).aliens[0]
    else:
        # print(context.board.get_cell(2, 2).aliens)
        # print(context.board.get_cell(2, 2).aliens[0].eyes)
        assert context.board.get_cell(2, 2).aliens == []


@then(u'if the alien survives, it should have {reproduction_eyes:d} eyes')
def step_impl(context, reproduction_eyes):
    if context.survive_or_die == "survive":
        print(context.board.get_cell(2, 2).aliens)
        print(context.board.get_cell(2, 2).aliens[0].eyes)
        assert context.board.get_cell(2, 2).aliens[0].eyes == reproduction_eyes
    else:
        pass


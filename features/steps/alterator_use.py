from behave import *
from app.backend.models.alien import Alien
from app.backend.models.game import INIT_CREW
from app.backend.models.team import Team


@when(u'a green alien is positioned on the cell ({row:d}, {col:d})')
def step_impl(context, row, col):
    context.alien_pos = (row, col)
    context.alien = Alien(Team.BLUE)
    context.game.set_alien(row, col, context.alien)


@then(u'the alien moves to the cell ({row:d}, {col:d})')
def step_impl(context, row, col):
    new_pos = context.game.get_alien_position(context.alien)
    assert new_pos == (row, col)


@then(u'the alien dies')
def step_impl(context):
    pos = context.game.get_alien_position(context.alien)
    assert pos is None


@then(u'{cant:d} green aliens dies')
def step_impl(context, cant):
    green_aliens = 0
    for pos, aliens_on_cell in context.game.aliens_dict().items():
        for alien in aliens_on_cell:
            if alien.team is Team.GREEN:
                green_aliens += 1
    assert INIT_CREW - cant == green_aliens

from behave import given, when, then

from app.backend.models.alien import Alien
from app.backend.models.board import Board
from app.backend.models.team import Team
from app.backend.models.game import Game


@given(u'that I have a game')
def step_impl(context):
    context.game = Game()

@given(u'there are two aliens in the square (6,6) of different teams')
def step_impl(context):
    context.game.board.set_alien(6, 6, Alien(Team.BLUE))
    context.game.board.set_alien(6, 6, Alien(Team.GREEN))


@given(u'that the number of eyes of alien 1 is {alien1_eyes:d}')
def step_impl(context, alien1_eyes):
    context.game.board.add_eyes_to_alien(6, 6, 0, alien1_eyes - 1)


@given(u'the number of eyes of alien 2 is {alien2_eyes:d}')
def step_impl(context, alien2_eyes):
    context.game.board.add_eyes_to_alien(6, 6, 1, alien2_eyes - 1)


@then(u'the number of aliens in the square (6,6) should be {aliens_remained:d}')
def step_impl(context, aliens_remained):
    assert context.game.board.get_num_aliens_in_position(6, 6) == aliens_remained


@then(u'I should see that alien 1 "{outcome1}" with "{alien1_eyes_after_battle:d}" eyes')
def step_impl(context, outcome1, alien1_eyes_after_battle):
    assert (alien1_eyes_after_battle == 0) or (context.game.board.get_alien_in_position(6, 6, 0).eyes == int(alien1_eyes_after_battle))


@then(u'I should see that alien 2 "{outcome2}" with "{alien2_eyes_after_battle:d}" eyes')
def step_impl(context, outcome2, alien2_eyes_after_battle):
    assert (alien2_eyes_after_battle == 0) or (context.game.board.get_alien_in_position(6, 6, 0).eyes == int(alien2_eyes_after_battle))

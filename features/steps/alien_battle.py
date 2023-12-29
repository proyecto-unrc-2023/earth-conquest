from behave import given, when, then

from app.backend.models.board import Board
from app.backend.models.team import Team
from app.backend.models.game import Game
from features.environment import table_to_string


@given(u'that I have a game with the following board')
def step_impl(context):
    context.game = Game()
    context.game.board = Board.from_string(table_to_string(context.table))


@given(u'there are two aliens in the square (6,6) of different teams')
def step_impl(context):
    context.game.create_an_alien_in_pos(6, 6, Team.BLUE)
    context.game.create_an_alien_in_pos(6, 6, Team.GREEN)


@given(u'the number of eyes of alien {i:d} is {alien_i_eyes:d}')
def step_impl(context, i, alien_i_eyes):
    context.game.add_eyes_to_alien(6, 6, i - 1, alien_i_eyes - 1)


@then(u'the number of aliens in the square (6,6) should be {aliens_remained:d}')
def step_impl(context, aliens_remained):
    assert context.game.get_num_aliens_in_position(6, 6) == aliens_remained


@then(u'I should see that alien 1 "{outcome1}" with "{alien1_eyes_after_battle:d}" eyes')
def step_impl(context, outcome1, alien1_eyes_after_battle):
    assert (alien1_eyes_after_battle == 0) or (context.game.get_alien_eyes_in_position(6, 6, 0) == alien1_eyes_after_battle)


@then(u'I should see that alien 2 "{outcome2}" with "{alien2_eyes_after_battle:d}" eyes')
def step_impl(context, outcome2, alien2_eyes_after_battle):
    assert (alien2_eyes_after_battle == 0) or (context.game.get_alien_eyes_in_position(6, 6, 0) == alien2_eyes_after_battle)

from behave import *
from app.backend.models.game import Game
from app.backend.models.team import Team
from app.backend.models.modifier import Modifier
from app.backend.models.alien import Alien


@given("a new game has started")
def step_game_started(context):
    context.game = Game()


@given("an alien is on the cell {row:d} {column:d}")
def step_an_alien_is_on_the_cell(context, row, column):
    context.alien_position = (row, column)
    context.alien = Alien(Team.GREEN)
    context.game.set_alien(row, column, context.alien)


@when("the board refreshes")
def step_game_refreshes(context):
    context.game.refresh_board()


@then("the alien moves to one of its adjoining positions")
def step_alien_moves_to_adjoining_cell(context):
    context.new_pos = context.game.get_alien_position(context.alien)
    assert (is_position_adjacent(context.alien_position, context.new_pos))


@then(u'the new alien posiiton is within the board\'s perimeter')
def step_impl(context):
    assert (context.game.is_pos_within_board_range(context.new_pos[0], context.new_pos[0]))


@then(u'the new alien position is free of mountains')
def step_impl(context):
    assert (context.game.get_cell(context.new_pos[0], context.new_pos[1]).alterator != Modifier.MOUNTAIN_RANGE)


def is_position_adjacent(original_pos, new_pos):
    return abs(original_pos[0] - new_pos[0]) + abs(original_pos[1] - new_pos[1]) == 1

from behave import *
from app.backend.models.application import Application
from app.backend.models.game import Game
from app.backend.models.board import Board
from app.backend.models.game_enum import TGame
from app.backend.models.team import Team
from app.backend.models.modifier import Modifier
from app.backend.models.alien import Alien


@given("a new game has started")
def step_game_started(context):
  context.app = Application()
  context.game = Game(10, 15)


@given("an alien is on the cell {row:d} {column:d}")
def step_an_alien_is_on_the_cell(context, row, column):
    context.alien_position = (row, column)
    context.alien = Alien(Team.BLUE)
    context.game.board.set_alien(row, column, context.alien)



# TODO: con is_free_position checkeo ademas que no haya modificador y necesito que no haya una montana nomas
#@given("the cell {end_row:d} {end_column:d} is both free of mountains and within the board's perimeter")
#def step_check_cell_is_valid(context, end_row, end_column):
  #context.game.board.is_free_position(end_row,end_column)
#  context.game.board.get_cell(end_row,end_column).alterator != Modifier.MOUNTAIN 
#  context.game.board.is_within_board_range(end_row, end_column)


@when("the game refreshes")
def step_game_refreshes(context):
  context.game.refresh_board()


# TODO tuve que crear el metodo get_alien_position()
#@then("the alien moves to the cell {end_row:d} {end_column:d}")
#def step_alien_in_expected_position(context, end_row, end_column):
#  assert(context.game.board.get_alien_position(context.alien) == (end_row, end_column))


@then("the alien moves to one of its adjoining, free of mountains and withing the board's perimeter cell")
def step_alien_moves_to_adjoining_cell(context):
  new_pos = context.game.board.get_alien_position(context.alien)
  assert(is_position_adjacent(context.alien_position,new_pos))
  assert(context.game.board.get_cell(new_pos[0],new_pos[1]).alterator != Modifier.MOUNTAIN)
  assert(context.game.board.is_within_board_range(new_pos[0], new_pos[0])) 


def is_position_adjacent(original_pos, new_pos):
   return abs(original_pos[0] - new_pos[0]) + abs(original_pos[1] - new_pos[1]) == 1
from behave import *

@given("the game is on")
def step_game_started(context):
  context.game.new_game() #esto debería ser un fixture

@given("an alien is in cell {row:d}, {column:d}")
def step_set_alien_in_cell(context, row, column):
  context.game.set_cell(row, column, content)

@given("the game is in refresh mode")
def step_impl(context):
  context.game.set_mode(context.MODE.refresh)

@given("the cell {row:d}, {column:d} is not a mountain")
def step_check_cell_not_mountain(context, end_row, end_column):
  context.game.is_valid_position(end_row, end_column)

@given("the cell {row:d}, {column:d} is within range")
def step_check_cell_within_range(context, end_row, end_column):
  context.game.is_valid_position(end_row, end_column) #puede ser la misma que isValidPosition


@when("the alien moves to {row:d}, {column:d}")
def step_alien_moves(context, end_row, end_column):
  context.alien.move_to(end_row, end_column)


@then("the alien should be in cell {row:d}, {column:d}")
def step_alien_in_expected_position(context, end_row, end_column):
  #Verificar que el alien esté en la posición esperada
  assert(context.alien.get_position() == (end_row, end_column))

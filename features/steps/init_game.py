from behave import *

from app.backend.models.board import Board
from app.backend.models.game import Game
from app.backend.models.game_enum import TGame
from app.backend.models.modifier import Modifier
from app.backend.models.team import Team


@given(u'a new game has been created')
def step_impl(context):
    context.game = Game()



@given(u'player "{name}" has joined the game as "{team}" player')
def step_impl(context, name, team):
    if team == 'green':
        context.game.join_as_green(name)
    elif team == 'blue':
        context.game.join_as_blue(name)


@given(u'player "{name}" has joined the game as green player')
def step_impl(context, name):
    context.game.join_as_green(name)


@step(u'the board dimension is {rows:d} by {cols:d}')
def step_impl(context, rows, cols):
    assert context.game.get_board_rows() == rows
    assert context.game.get_board_cols() == cols


@given(u'the game has not started')
def step_impl(context):
    assert context.game.status == TGame.NOT_STARTED


@step(u'the game is started')
def step_impl(context):
    context.game.start_game()


@when(u'the board dimension is set in {rows:d} by {cols:d}')
def step_impl(context, rows, cols):
    context.game.set_board_dimensions(rows, cols)


@then(u'the game status is set on start mode')
def step_impl(context):
    assert context.game.status == TGame.STARTED


@then(u'the placed modifiers end up positioned outside the teams areas')
def step_impl(context):
    board = context.game.board
    modifiers = []
    # ciclo toda la matriz
    for i, row in enumerate(board.board):
        for j, cell in enumerate(row):
            if cell.modifier is not None:   # si la celda tiene un modifier
                modifiers.append((i, j))
    for pos in modifiers:
        assert not context.game.is_pos_on_any_range(pos[0], pos[1])


@then(u'there are {cant:d} living one-eyed aliens per team')
def step_impl(context, cant):
    blue_aliens = []
    green_aliens = []
    for position, aliens_in_position in context.game.aliens_dict().items():
        for alien in aliens_in_position:
            assert alien.eyes == 1
            if alien.team == Team.BLUE:
                blue_aliens.append(alien)
            else:
                green_aliens.append(alien)

    assert blue_aliens.__len__() == cant
    assert green_aliens.__len__() == cant


@then(u'the aliens are set on their respective areas')
def step_impl(context):
    blue_aliens = []
    green_aliens = []
    for position, aliens_in_position in context.game.aliens_dict().items():
        for alien in aliens_in_position:
            if alien.team == Team.BLUE:
                blue_aliens.append(position)
            else:
                green_aliens.append(position)

    for pos in blue_aliens:
        assert context.game.is_position_in_blue_range(pos[0], pos[1])

    for pos in green_aliens:
        assert context.game.is_position_in_green_range(pos[0], pos[1])


@then(u'there are {cant:d} "{modifier}"')
def step_impl(context, cant, modifier):
    if modifier == "mountains":
        modifier = Modifier.MOUNTAIN_RANGE
    elif modifier == "killers":
        modifier = Modifier.KILLER
    elif modifier == "multipliers":
        modifier = Modifier.MULTIPLIER
    else:
        raise Exception("Invalid modifier")

    board = context.game.board
    modifiers = []
    # ciclo toda la matriz
    for i, row in enumerate(board.board):
        for j, cell in enumerate(row):
            if cell.modifier is modifier:
                modifiers.append(cell)

    assert modifiers.__len__() == cant


@then(u'the cells where the modifiers has been setted are occupied')
def step_impl(context):
    board = context.game.board
    modifiers = []
    # ciclo toda la matriz
    for i, row in enumerate(board.board):
        for j, cell in enumerate(row):
            if cell.modifier is not None:  # si la celda tiene un modifier
                modifiers.append((i, j))
    for pos in modifiers:
        assert not context.game.is_free_position(pos[0], pos[1])


@then(u'the dimensions of the ovnis ranges should be {range:d} by {range:d}')
def step_impl(context, range):
    assert context.game.get_base_range_dimentions() == range


@then(u'the corner position of the "{team}" ovni range should be {row:d} {col:d}')
def step_impl(context, team, row, col):
    assert context.game.get_green_ovni_range() if team == "green" else context.game.get_blue_ovni_range() == (row, col)


from behave import *

from app.backend.models.alien import Alien
from app.backend.models.board import Board
from app.backend.models.team import Team


@given(u'{blue_cant:d} blue aliens and {green_cant:d} green aliens are in the position (5,5)')
def step_set_alien(context, blue_cant, green_cant):
    context.blue_aliens = []
    context.green_aliens = []

    for _ in range(blue_cant):
        blue_alien = Alien(Team.BLUE)
        context.blue_aliens.append(blue_alien)
        
    for _ in range(green_cant):
        green_alien = Alien(Team.GREEN)
        context.green_aliens.append(green_alien)
        

    context.board = Board(10, 15, 4)
    context.board.get_cell(5, 5).modifier = None
    context.board.get_cell(5, 5).alterator = None

    for alien in context.blue_aliens:
        context.board.set_alien(5, 5, alien)

    for alien in context.green_aliens:
        context.board.set_alien(5, 5, alien)


@when(u'the cell acts')
def step_action(context):
    context.board.get_cell(5, 5).action()


@then(u'there is {blue_cant:d} blue alien left, with {eyes:d} eyes')
def step_result(context, blue_cant, eyes):
    if eyes == 0:
        assert (len(context.board.get_cell(5,5).aliens) == 0)
    else:
        assert (context.board.get_cell(5,5).aliens[0].eyes == eyes)
        assert (context.board.get_cell(5,5).aliens[0].team == Team.BLUE)



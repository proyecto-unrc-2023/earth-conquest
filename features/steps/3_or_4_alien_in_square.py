from behave import *

from app.backend.models.alien import Alien
from app.backend.models.board import Board
from app.backend.models.game import Game
from app.backend.models.team import Team


@given(u'a new game has started')
def step_game_started(context):
   context.game = Game(10, 15)


@given(u'two blue aliens and one green alien in the position (5,5)')
def step_set_alien(context):
    context.alien1 = Alien(Team.BLUE)
    context.alien2 = Alien(Team.BLUE)
    context.alien3 = Alien(Team.GREEN)
   
    board = Board(10, 15, 5)
    board.set_alien(5,5,context.alien1) 
    board.set_alien(5,5,context.alien2)
    board.set_alien(5,5,context.alien3)
    context.board = board

@when(u'the cell acts')
def step_action(context):
    context.board.get_cell(5,5).action()

@then(u'there is a blue alien left, with one eye')
def step_result(context):
    assert (context.board.get_cell(5,5).aliens[0].eyes == 1)
    assert (context.board.get_cell(5,5).aliens[0].team == Team.BLUE)


@given(u'3 aliens on the blue team, in the positions (5,5)')
def step_impl(context):
    context.alien1 = Alien(Team.BLUE)
    context.alien2 = Alien(Team.BLUE)
    context.alien3 = Alien(Team.BLUE)
   
    board = Board(10, 15, 5)
    board.set_alien(5,5,context.alien1) 
    board.set_alien(5,5,context.alien2)
    board.set_alien(5,5,context.alien3)
    context.board = board

@then(u'there is a blue alien left, with 3 eyes')
def step_impl(context):
    assert (context.board.get_cell(5,5).aliens[0].eyes == 3)
    assert (context.board.get_cell(5,5).aliens[0].team == Team.BLUE)



@given(u'3 aliens on the blue team and one green alien in the positions (5,5)')
def step_impl(context):
    context.alien1 = Alien(Team.BLUE)
    context.alien2 = Alien(Team.BLUE)
    context.alien3 = Alien(Team.BLUE)
    context.alien4 = Alien(Team.GREEN)
   
    board = Board(10, 15, 5)
    board.set_alien(5,5,context.alien1) 
    board.set_alien(5,5,context.alien2)
    board.set_alien(5,5,context.alien3)
    board.set_alien(5,5,context.alien4)
    context.board = board


@then(u'there is a blue alien left, with 2 eyes')
def step_impl(context):
    assert (context.board.get_cell(5,5).aliens[0].eyes == 2)
    assert (context.board.get_cell(5,5).aliens[0].team == Team.BLUE)


@given(u'2 aliens are on blue team and 2 on green team in the positions (5,5) with 1 eyes')
def step_impl(context):
    context.alien1 = Alien(Team.BLUE)
    context.alien2 = Alien(Team.BLUE)
    context.alien3 = Alien(Team.GREEN)
    context.alien4 = Alien(Team.GREEN)
   
    board = Board(10, 15, 5)
    board.set_alien(5,5,context.alien1) 
    board.set_alien(5,5,context.alien2)
    board.set_alien(5,5,context.alien3)
    board.set_alien(5,5,context.alien4)
    context.board = board


@then(u'there are no aliens left')
def step_impl(context):
    assert (len(context.board.get_cell(5,5).aliens) == 0)


@given(u'4 aliens are on blue team in the positions (5,5)')
def step_impl(context):
    context.alien1 = Alien(Team.BLUE)
    context.alien2 = Alien(Team.BLUE)
    context.alien3 = Alien(Team.BLUE)
    context.alien4 = Alien(Team.BLUE)
   
    board = Board(10, 15, 5)
    board.set_alien(5,5,context.alien1) 
    board.set_alien(5,5,context.alien2)
    board.set_alien(5,5,context.alien3)
    board.set_alien(5,5,context.alien4)
    context.board = board

@then(u'there is a blue alien left, with 4 eyes')
def step_impl(context):
   assert (context.board.get_cell(5,5).aliens[0].eyes == 4)
   assert (context.board.get_cell(5,5).aliens[0].team == Team.BLUE)

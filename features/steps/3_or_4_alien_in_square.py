from behave import *

@given(u'a new game has started')
def step_game_started(context):
   context.game.new_game()

@given(u'two blue aliens and one green alien in the position (5,5)')
def step_set_alien(context):
    context.alien1 = Alien(Team.BLUE)
    context.alien2 = Alien(Team.BLUE)
    context.alien3 = Alien(Team.GREEN)
   
    board = Board(10, 15)
    board.set_cell(context.alien1, 5, 5) 
    board.set_cell(context.alien2, 5, 5)
    board.set_cell(context.alien3, 5, 5)
    context.board = board

@when(u'the cell acts')
def step_action(context):
    context.cell.action()

@then(u'there is a blue alien left, with one eye')
def step_result(context):
    assert (context.board[5][5].get_alien().eyes == 1)
    assert (context.board[5][5].get_alien().team == Team.BLUE)



@given(u'3 aliens on the blue team, in the positions (5,5)')
def step_impl(context):
    context.alien1 = Alien(Team.BLUE)
    context.alien2 = Alien(Team.BLUE)
    context.alien3 = Alien(Team.BLUE)
   
    board = Board(10, 15)
    board.set_cell(context.alien1, 5, 5) 
    board.set_cell(context.alien2, 5, 5)
    board.set_cell(context.alien3, 5, 5)
    context.board = board

@then(u'there is a blue alien left, with 3 eyes')
def step_impl(context):
    assert (context.board[5][5].get_alien().eyes == 3)
    assert (context.board[5][5].get_alien().team == Team.BLUE)



@given(u'3 aliens on the blue team and one green alien in the positions (5,5)')
def step_impl(context):
    context.alien1 = Alien(Team.BLUE)
    context.alien2 = Alien(Team.BLUE)
    context.alien3 = Alien(Team.BLUE)
    context.alien4 = Alien(Team.GREEN)
   
    board = Board(10, 15)
    board.set_cell(context.alien1, 5, 5) 
    board.set_cell(context.alien2, 5, 5)
    board.set_cell(context.alien3, 5, 5)
    board.set_cell(context.alien4, 5, 5)
    context.board = board


@then(u'there is a blue alien left, with 2 eyes')
def step_impl(context):
    assert (context.board[5][5].get_alien().eyes == 2)
    assert (context.board[5][5].get_alien().team == Team.BLUE)


@given(u'2 aliens are on blue team and 2 on green team in the positions (5,5) with 1 eyes')
def step_impl(context):
    context.alien1 = Alien(Team.BLUE)
    context.alien2 = Alien(Team.BLUE)
    context.alien3 = Alien(Team.GREEN)
    context.alien4 = Alien(Team.GREEN)
   
    board = Board(10, 15)
    board.set_cell(context.alien1, 5, 5) 
    board.set_cell(context.alien2, 5, 5)
    board.set_cell(context.alien3, 5, 5)
    board.set_cell(context.alien4, 5, 5)
    context.board = board


@then(u'there are no aliens left')
def step_impl(context):
    assert (context.board[5][5].get_alien() is None)


@given(u'4 aliens are on blue team in the positions (5,5)')
def step_impl(context):
    context.alien1 = Alien(Team.BLUE)
    context.alien2 = Alien(Team.BLUE)
    context.alien3 = Alien(Team.BLUE)
    context.alien4 = Alien(Team.BLUE)
   
    board = Board(10, 15)
    board.set_cell(context.alien1, 5, 5) 
    board.set_cell(context.alien2, 5, 5)
    board.set_cell(context.alien3, 5, 5)
    board.set_cell(context.alien4, 5, 5)
    context.board = board

@then(u'there is a blue alien left, with 4 eyes')
def step_impl(context):
   assert (context.board[5][5].get_alien().eyes == 4)
   assert (context.board[5][5].get_alien().team == Team.BLUE)

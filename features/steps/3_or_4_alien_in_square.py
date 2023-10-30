from behave import *

from app.backend.models.team import Team


@given(u'{blue_cant:d} blue aliens and {green_cant:d} green aliens are in the position (5,5)')
def step_set_alien(context, blue_cant, green_cant):
    context.game.creates_aliens_in_pos(5, 5, blue_cant, Team.BLUE)
    context.game.creates_aliens_in_pos(5, 5, green_cant, Team.GREEN)
   

@when(u'the cell acts')
def step_action(context):
    context.game.act_board()


@then(u'there is {blue_cant:d} blue alien left, with {eyes:d} eyes')
def step_result(context, blue_cant, eyes):
    if eyes == 0:
        assert (context.game.get_num_aliens_in_position(5, 5) == 0)
    else:
        assert (context.game.get_num_aliens_in_position(5, 5) == 1)
        assert (context.game.get_alien_eyes_in_position(5, 5, 0) == eyes)
        assert (context.game.get_alien_team_in_position(5, 5, 0) == Team.BLUE)

from behave import given, then, when
from app.backend.models.modifier import Modifier
from app.backend.models.team import Team


@given(u'there is a "{modifier}" on the cell (11, 5)')
def step_impl(context, modifier):
    if modifier == "multiplier":
        context.game.set_modifier_in_position(Modifier.MULTIPLIER, 11, 5)
    else:
        context.game.set_modifier_in_position(Modifier.KILLER, 11, 5)


@given(u'the alien arrives on the cell (11, 5)')
def step_impl(context):
    context.game.creates_aliens_in_pos(11, 5, 1, Team.BLUE)


@when(u'"{modifier}" activates')
def step_when(context, modifier):
    context.game.act_board()


@then(u'"{action_modifier}" and "{result_modifier}"')
def step_when(context, action_modifier, result_modifier):
    if context.game.get_modifier(11,5) == Modifier.MULTIPLIER:
        assert (context.game.get_num_aliens_in_position(11,5) == 2)
    else:
        assert (context.game.get_num_aliens_in_position(11,5) == 0)


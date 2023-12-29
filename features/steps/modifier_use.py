from behave import given, then, when
from app.backend.models.modifier import Modifier
from app.backend.models.team import Team


@given(u'there is a "{modifier}" on the cell (2, 9)')
def step_impl(context, modifier):
    print(context.game.is_free_position(2,9))
    if modifier == "multiplier":
        context.game.set_modifier_in_position(Modifier.MULTIPLIER, 2, 9)
    else:
        context.game.set_modifier_in_position(Modifier.KILLER, 2, 9)


@given(u'the alien arrives on the cell (2, 9)')
def step_impl(context):
    context.game.creates_aliens_in_pos(2, 9, 1, Team.BLUE)


@when(u'"{modifier}" activates')
def step_when(context, modifier):
    context.game.act_board()


@then(u'"{action_modifier}" and "{result_modifier}"')
def step_when(context, action_modifier, result_modifier):
    if context.game.get_modifier_in_position(2,9) == Modifier.MULTIPLIER:
        assert (context.game.get_num_aliens_in_position(2,9) == 2)
    else:
        print(context.game.get_num_aliens_in_position(2,9))
        assert (context.game.get_num_aliens_in_position(2,9) == 0)


from behave import given, when, then

from app.backend.models.team import Team


@given(u'I have {aliens_cant:d} aliens in the square (6,6) of same team')
def step_impl(context, aliens_cant):
    context.game.creates_aliens_in_pos(6, 6, aliens_cant, Team.BLUE)


@then(u'the number of aliens in the square (6,6) should be {aliens_remained:d}')
def step_impl(context, aliens_remained):
    assert context.game.get_num_aliens_in_position(6, 6) == aliens_remained


@then(u'I "{should_or_not}" have an alien with {reproduction_eyes:d} eyes in the square (6,6)')
def step_impl(context, should_or_not, reproduction_eyes):
    assert (should_or_not == "should not") or (context.game.get_alien_eyes_in_position(6, 6, 0) == reproduction_eyes)
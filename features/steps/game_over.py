from behave import given, when, then

from app.backend.models.team import Team


@given(u'a base of "{attacked_team}" team with {life_points:d} points of life')
def step_impl(context, attacked_team, life_points):
    if attacked_team == "GREEN":
        context.base_attacked_team = Team.GREEN
        context.game.board.green_ovni_life = life_points
    else:
        context.base_attacked_team = Team.BLUE
        context.game.board.blue_ovni_life = life_points


@given(u'an alien of "{attacking_team}" team in the cell ({x:d}, {y:d}) with {alien_eyes:d} eyes')
def step_impl(context, attacking_team, x, y, alien_eyes):
    context.game.create_an_alien_in_pos(x, y, to_team(attacking_team))
    context.game.add_eyes_to_alien(x, y, 0, alien_eyes - 1)


@when(u'the board acts')
def step_impl(context):
    context.game.act_board()


@then(u'the base has {results_life_points:d} life points')
def step_impl(context, results_life_points):
    if context.base_attacked_team == Team.GREEN:
        assert context.game.board.green_ovni_life == results_life_points
    else:
        assert context.game.board.blue_ovni_life == results_life_points


@then(u'the alien is not in the cell ({x:d}, {y:d})')
def step_impl(context, x, y):
    assert context.game.get_aliens_in_pos(x, y) == []


@then(u'it is destroyed')
def step_impl(context):
    assert context.game.any_ovni_destroyed()


@then(u'game is over')
def step_impl(context):
    assert context.game.has_game_ended()


@then(u'"{attacking_team}" wins')
def step_impl(context, attacking_team):
    assert context.game.get_team_winner() == to_team(attacking_team)


def to_team(team):
    return Team.GREEN if team == "GREEN" else Team.BLUE

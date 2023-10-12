from behave import given, when, then

from app.backend.models.alien import Alien
from app.backend.models.team import Team


@given(u'a base of "{attacked_team}" team with {life_points:d} points of life')
def step_impl(context, attacked_team, life_points):
    if attacked_team == "green":
        context.base_attacked_team = Team.GREEN
        context.game.board.green_ovni_life = life_points
    else:
        context.base_attacked_team = Team.BLUE
        context.game.board.blue_ovni_life = life_points


@given(u'a "{attacking_team}" alien with {alien_eyes:d} eyes is positioned on the cell in the "{attacked_team}" base '
       u'range')
def step_impl(context, attacking_team, alien_eyes, attacked_team):
    if attacking_team == "green":
        context.alien = Alien(Team.GREEN, alien_eyes)
        context.game.board.set_alien(7, 11, context.alien)
    else:
        context.alien = Alien(Team.BLUE, alien_eyes)
        context.game.board.set_alien(3, 3, context.alien)


@when(u'the board acts')
def step_impl(context):
    context.game.act_board()


@then(u'the base has {results_life_points:d}')
def step_impl(context, results_life_points):
    if context.base_attacked_team == Team.GREEN:
        base_life_points = context.game.board.green_ovni_life
        assert base_life_points == results_life_points
    else:
        base_life_points = context.game.board.blue_ovni_life
        assert base_life_points == results_life_points


@then(u'it is destroyed')
def step_impl(context):
    assert context.game.board.any_ovni_destroyed()


@then(u'game is over')
def step_impl(context):
    assert context.game.has_game_ended()


@then(u'"{attacking_team}" wins')
def step_impl(context, attacking_team):
    assert context.game.get_team_winner() == to_team(attacking_team)


def to_team(team):
    return Team.GREEN if team == "green" else Team.BLUE


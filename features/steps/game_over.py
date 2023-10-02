from behave import *

@given('a new game has started')
def step_game_started(context):
    context.game.new_game()


@given('that a one-eyed blue alien from player Juan arrives at the base of green aliens from player Jose')
def step_impl(context, row, column):
    context.game.set_cell(row,column, context.alienBlue)
    


@given('the green aliens base has 1 life remaining')
def step_impl(context):
    context.game.green_base.life = 1
    


@when('the blue alien attacks')
def step_impl(context):
    context.game.action()


@then('the base is destroyed')
def step_impl(context):
    assert (context.game.green_base.life == 0)


@then('blue aliens win')
def step_impl(context):
    assert (context.game.winner == context.TEAM.BLUE)




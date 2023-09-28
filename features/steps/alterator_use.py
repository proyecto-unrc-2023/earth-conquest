from behave import *

# Definition of context to store shared data if needed
class Context:
    pass

context = Context()

@given('the game has started')
def step_game_started(context):
    context.game_started = True

@when('the player has a list of alterators to choose from and use')
def step_choose_alterator(context):
    context.alterator_list = ['Directioner', 'Teleporter', 'Booby Trap']

@then(u'the player chooses one alterator')
def step_impl(context):
    # If alterator_chosen is empty, the player hasn't chosen an alterator yet
    assert context.alterator_chosen, "Player should have at least one alterator to choose from"


@given(u'the Directioner is positioned on the cells (2,2), (2,3) and (2,4)')
def step_impl(context):
    context.board = Board()
    context.directioner = Directioner()
    context.board[2][2] = directioner
    context.board[2][3] = directioner
    context.board[2][4] = directioner
    

@given(u'the Directioner has the property that lets the alien move in a specific direction for as long as the alterator has power')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the Directioner has the property that lets the alien move in a specific direction for as long as the alterator has power')


@given(u'the alien is positioned on the cell (1,2)')
def step_impl(context):
    context.alien = Alien()
    context.board[1][2] = alien


@when(u'the system refreshes')
def step_impl(context):
    context.refresh()
    

@then(u'the alien moves to an adjacent cell, this one being cell (2,2)')
def step_impl(context):
    context.direction = down
    context.alien.moveTo(direction)
    assert alien.getPosition() == (2, 2), "Alien did not move to cell (2, 2)"


@then(u'the Directioner acts on the alien')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the Directioner acts on the alien')


@then(u'the following board is obtained')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the following board is obtained')


@when(u'the system refreshes again')
def step_impl(context):
    context.refresh()


@then(u'the alien moves to the cell (2,3)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the alien moves to the cell (2,3)')


@then(u'the alien moves to the cell (2,4)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the alien moves to the cell (2,4)')


@then(u'the alien moves to one of its free adjacent cells, not being the cell (2,3) an option')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the alien moves to one of its free adjacent cells, not being the cell (2,3) an option')


@given(u'the Teleporter\'s door is positioned on the cell (2,2)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the Teleporter\'s door is positioned on the cell (2,2)')


@given(u'the Teleporter has the property that it teleports aliens to it\'s tail.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the Teleporter has the property that it teleports aliens to it\'s tail.')


@given(u'the Teleporter\'s tail is on the cell (6,5)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the Teleporter\'s tail is on the cell (6,5)')


@given(u'an alien is positioned on the cell (1,2)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given an alien is positioned on the cell (1,2)')


@then(u'the Teleporter acts on the alien')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the Teleporter acts on the alien')


@then(u'the alien is teleported to the cell (6,5)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the alien is teleported to the cell (6,5)')


@given(u'the Trap is positioned on the cell (2,2)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the Trap is positioned on the cell (2,2)')


@given(u'the Trap has the property that it kills every alien that steps on its cell')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the Trap has the property that it kills every alien that steps on its cell')


@then(u'the Booby Trap acts on the alien')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the Booby Trap acts on the alien')


@then(u'the alien dies')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the alien dies')
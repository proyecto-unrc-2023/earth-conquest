from behave import *


@given(u'the game has started')
def step_impl(context):
    context.app = Application()
    context.game.set_status(TGame.STARTED)


@when(u'the game is in the mode Alterator_selection')
def step_impl(context):
    context.game.set_mode(TMode.ALTERATOR_SELECTION)


@then(u'the player chooses one alterator')
def step_impl(context):
    context.game.alterator_chosen(TAlterator.DIRECTIONER)


@given(u'the Directioner is positioned on the cells (2,2), (2,3) and (2,4)')
def step_impl(context):
    context.game.add_alterator(alterator_chosen(),(2,2, TOrientation.HORIZONTAL))


@given(u'the alien is positioned on the cell (1,2)')
def step_impl(context):
    context.game.add_alien_to_board(Alien(), (1,2))


@when(u'the system refreshes')
def step_impl(context):
    context.game.refresh_board()


@then(u'the alien moves to an adjacent cell, this one being cell (2,2)')
def step_impl(context):
    context.game.move_alien(Alien(), (2,2))


@then(u'the Directioner acts on the alien')
def step_impl(context):
    context.game.act_board()


@when(u'the system refreshes again')
def step_impl(context):
    context.game.refresh_board()


@then(u'the alien moves to the cell (2,3)')
def step_impl(context):
    context.game.move_alien(Alien(), (2,3))


@then(u'the alien moves to the cell (2,4)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the alien moves to the cell (2,4)')


@then(u'the alien moves to one of its free adjacent cells, not being the cell (2,3) an option')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the alien moves to one of its free adjacent cells, not being the cell (2,3) an option')


@given(u'the Teleporter\'s door is positioned on the cell (2,2)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the Teleporter\'s door is positioned on the cell (2,2)')


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


@then(u'the Trap acts on the alien')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the Trap acts on the alien')


@then(u'the alien dies')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the alien dies')
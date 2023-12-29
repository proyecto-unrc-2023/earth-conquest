"""
This module contains unit tests for the Cell class in the earth-conquest game.

The tests are organized as follows:
    - Fixtures for setting up test data
    - Tests for creating a cell and adding aliens to it
    - Tests for removing aliens from a cell
    - Tests for fighting between aliens in a cell
    - Tests for reproducing aliens in a cell
    - Tests for applying modifiers to a cell
    - Each test follows the Arrange-Act-Assert pattern
"""

# Fixtures for setting up test data

import pytest

from app.backend.models.alien import Alien
from app.backend.models.alterator import Alterator
from app.backend.models.cell import Cell
from app.backend.models.modifier import Modifier
from app.backend.models.team import Team


@pytest.fixture
def add_two_same_team_aliens_in_a_cell():
    """
    Fixture that creates a cell with two aliens of the same team.
    """
    cell = Cell()
    cell.add_alien(Alien(Team.BLUE))
    cell.add_alien(Alien(Team.BLUE))
    return cell


@pytest.fixture
def add_two_diff_team_aliens_in_a_cell():
    """
    Fixture that creates a cell with two aliens of different teams.
    """
    cell = Cell()
    cell.add_alien(Alien(Team.BLUE))
    cell.add_alien(Alien(Team.GREEN))
    return cell


# Tests for creating a cell and adding aliens to it

def test_create_a_cell():
    """
    Test that verifies a cell is created with empty lists for aliens, modifier and alterator.
    """
    # Arrange
    cell = Cell()

    # Assert
    assert cell.aliens.__eq__([])
    assert cell.modifier.__eq__(None)
    assert cell.alterator.__eq__(None)


def test_add_aliens():
    """
    Test that verifies aliens can be added to a cell.
    """
    # Arrange
    alien = Alien(Team.BLUE)
    cell = Cell()

    # Act
    cell.add_alien(alien)
    cell.add_alien(Team.GREEN)

    # Assert
    assert len(cell.aliens).__eq__(2)
    assert isinstance(cell.aliens[0], Alien)


# Tests for removing aliens from a cell

def test_remove_alien():
    """
    Test that verifies an alien can be removed from a cell.
    """
    # Arrange
    alien1 = Alien(Team.BLUE)
    cell = Cell()
    cell.add_alien(Alien(Team.GREEN))
    cell.add_alien(alien1)
    cell.add_alien(Alien(Team.GREEN))

    # Act
    cell.remove_alien(alien1)

    # Assert
    assert len(cell.aliens) == 2


def test_insert_only_aliens():
    """
    Test that verifies an error is raised when trying to add a non-alien object to a cell.
    """
    # Arrange
    cell = Cell()

    # Assert
    with pytest.raises(ValueError):
        cell.add_alien(2)


def test_remove_only_aliens():
    """
    Test that verifies an error is raised when trying to remove a non-alien object from a cell.
    """
    # Arrange
    cell = Cell()

    # Assert
    with pytest.raises(ValueError):
        cell.remove_alien(7)


# Tests for fighting between aliens in a cell

def test_for_two_aliens_fight_wins_alien1(add_two_diff_team_aliens_in_a_cell):
    """
    Test that verifies the winner of a fight between two aliens in a cell.
    """
    # Arrange
    cell = add_two_diff_team_aliens_in_a_cell
    alien1 = cell.aliens[0]
    alien2 = cell.aliens[1]
    alien1.add_eyes(2)
    eyes1 = alien1.eyes

    # Act
    cell.fight()

    # Assert
    assert cell.aliens[0] is alien1
    assert len(cell.aliens).__eq__(1)
    assert alien1.eyes.__eq__(eyes1 - alien2.eyes)


def test_for_two_aliens_fight_wins_alien2(add_two_diff_team_aliens_in_a_cell):
    """
    Test that verifies the winner of a fight between two aliens in a cell.
    """
    # Arrange
    cell = add_two_diff_team_aliens_in_a_cell
    alien1 = cell.aliens[0]
    alien2 = cell.aliens[1]
    alien2.add_eyes(2)
    eyes2 = alien2.eyes

    # Act
    cell.fight()

    # Assert
    assert cell.aliens[0] is alien2
    assert len(cell.aliens).__eq__(1)
    assert alien2.eyes.__eq__(eyes2 - alien1.eyes)


def test_for_three_aliens_fight(add_two_diff_team_aliens_in_a_cell):
    """
    Test that verifies an error is raised when trying to fight with three aliens in a cell.
    """
    # Arrange
    cell = add_two_diff_team_aliens_in_a_cell
    cell.add_alien(Alien(Team.GREEN))

    # Assert
    with pytest.raises(ValueError):
        cell.fight()


# Tests for reproducing aliens in a cell

def test_all_aliens_same_team(add_two_same_team_aliens_in_a_cell):
    """
    Test that verifies all aliens in a cell are from the same team.
    """
    # Arrange
    cell = add_two_same_team_aliens_in_a_cell

    # Assert
    assert cell.all_aliens_same_team()


def test_no_same_team(add_two_diff_team_aliens_in_a_cell):
    """
    Test that verifies there are no aliens from the same team in a cell.
    """
    # Arrange
    cell = add_two_diff_team_aliens_in_a_cell

    # Assert
    assert not cell.all_aliens_same_team()


def test_sum_aliens_eyes(add_two_same_team_aliens_in_a_cell):
    """
    Test that verifies the sum of eyes of all aliens in a cell.
    """
    # Arrange
    cell = add_two_same_team_aliens_in_a_cell
    cell.add_alien(Alien(Team.GREEN))

    # Act
    eyes = cell.sum_aliens_eyes()

    # Assert
    assert eyes.__eq__(3)


def test_two_aliens_reproduction(add_two_same_team_aliens_in_a_cell):
    """
    Test that verifies the reproduction of two aliens in a cell.
    """
    # Arrange
    cell = add_two_same_team_aliens_in_a_cell
    cell.aliens[0].eyes = 2
    cell.aliens[1].eyes = 4

    # Act
    cell.reproduce()

    # Assert
    assert len(cell.aliens) is 0


def test_three_aliens_reproduction(add_two_same_team_aliens_in_a_cell):
    """
    Test that verifies the reproduction of three aliens in a cell.
    """
    # Arrange
    cell = add_two_same_team_aliens_in_a_cell
    cell.add_alien(Team.BLUE)
    cell.aliens[2].add_eyes(2)

    # Act
    cell.reproduce()

    # Assert
    assert len(cell.aliens) is 1
    assert cell.aliens[0].eyes is 5


def test_one_alien_reproduction():
    """
    Test that verifies an error is raised when trying to reproduce with only one alien in a cell.
    """
    # Arrange
    cell = Cell()
    cell.add_alien(Team.BLUE)

    # Assert
    with pytest.raises(ValueError):
        cell.reproduce()


def test_aliens_reproduction_with_different_teams(add_two_diff_team_aliens_in_a_cell):
    """
    Test that verifies an error is raised when trying to reproduce aliens from different teams in a cell.
    """
    # Arrange
    cell = add_two_diff_team_aliens_in_a_cell

    # Assert
    with pytest.raises(ValueError):
        cell.reproduce()


def test_alien_reproduction_where_total_eyes_greater_than_five(add_two_same_team_aliens_in_a_cell):
    """
    Test that verifies an error is raised when trying to reproduce aliens with a total of eyes greater than five in a cell.
    """
    # Arrange
    cell = add_two_same_team_aliens_in_a_cell
    team = cell.aliens[0].team
    alien1 = Alien(team)
    alien2 = Alien(team)
    alien1.add_eyes(2)
    alien2.add_eyes(2)
    cell.add_alien(alien1)
    cell.add_alien(alien2)

    # Act
    cell.reproduce()

    # Assert
    assert len(cell.aliens) is 0


def test_alien_reproduction_where_total_eyes_lesser_than_five(add_two_same_team_aliens_in_a_cell):
    """
    Test that verifies the reproduction of aliens with a total of eyes lesser than five in a cell.
    """
    # Arrange
    cell = add_two_same_team_aliens_in_a_cell
    team = cell.aliens[0].team
    alien1 = Alien(team)
    alien2 = Alien(team)
    cell.add_alien(alien1)
    cell.add_alien(alien2)

    # Act
    cell.reproduce()

    # Assert
    assert len(cell.aliens) is 1
    assert cell.aliens[0].eyes is 4


# Tests for applying modifiers to a cell

def test_action_cell_3_blue_aliens_vs_1_green_aliens(add_two_same_team_aliens_in_a_cell):
    """
    Test that verifies the action of a cell with 3 blue aliens and 1 green alien.
    """
    # Arrange
    # Creo una celda con dos aliens de un mismo equipo con 1 ojo cada uno
    cell = add_two_same_team_aliens_in_a_cell
    # Se le añade un alien del mismo equipo que los anteriores, con 1 ojo
    cell.add_alien(Team.BLUE)
    # Se le añade un alien de un ojo, del otro equipo diferente
    cell.add_alien(Team.GREEN)

    # Act
    cell.action()

    # Assert
    # Deberia quedar un solo alien, del equipo azul
    assert len(cell.aliens) is 1
    # Ese alien deberia tener dos ojos, ya que el que se reprodujo en action() obtuvo 3
    assert cell.aliens[0].eyes is 2
    # menos 1 con el que peleo del equipo verde
    assert cell.aliens[0].team is Team.BLUE  # Ganador equipo azul


def test_action_cell_2_blue_aliens_vs_2_green_aliens(add_two_same_team_aliens_in_a_cell):
    """
    Test that verifies the action of a cell with 2 blue aliens and 2 green aliens.
    """
    # Arrange
    cell = add_two_same_team_aliens_in_a_cell
    cell.add_alien(Team.GREEN)
    cell.add_alien(Team.GREEN)

    # Act
    cell.action()

    # Assert
    assert len(cell.aliens) is 0


def test_action_cell_1_blue_aliens_vs_3_green_aliens(add_two_diff_team_aliens_in_a_cell):
    """
    Test that verifies the action of a cell with 1 blue alien and 3 green aliens.
    """
    # Arrange
    cell = add_two_diff_team_aliens_in_a_cell
    cell.add_alien(Team.GREEN)
    cell.add_alien(Team.GREEN)

    # Act
    cell.action()

    # Assert
    # Debera quedar un solo alien, del equipo verde
    assert len(cell.aliens) is 1
    # Ese alien debería tener dos ojos, ya que el alien verde que se reprodujo
    assert cell.aliens[0].eyes is 2
    # en action() obtuvo 3, menos 1 con el que peleo del equipo verde
    assert cell.aliens[0].team is Team.GREEN  # Ganador equipo VERDE


def test_action_cell_with_aliens_of_the_same_team(add_two_same_team_aliens_in_a_cell):
    """
    Test that verifies the action of a cell with aliens of the same team.
    """
    # Arrange
    cell = add_two_same_team_aliens_in_a_cell

    # Act
    cell.action()

    # Assert
    assert len(cell.aliens) is 1
    assert cell.aliens[0].eyes is 2


def test_cell_with_modifier_killer():
    """
    Test that verifies the action of a cell with a killer modifier.
    """
    # Arrange
    cell = Cell()
    cell.modifier = Modifier.KILLER
    cell.add_alien(Team.GREEN)

    # Act
    cell.action()

    # Assert
    assert cell.aliens == []


def test_cell_with_modifier_multiplier():
    """
    Test that verifies the action of a cell with a multiplier modifier.
    """
    # Arrange
    cell = Cell()
    cell.modifier = Modifier.MULTIPLIER
    alien = Alien(Team.GREEN)
    cell.add_alien(alien)

    # Act
    cell.action()

    # Assert
    assert cell.aliens[0] == alien
    assert isinstance(cell.aliens[1], Alien)
    assert cell.aliens[1].team == Team.GREEN
    assert cell.aliens[1].eyes == cell.aliens[0].eyes


def test_string_for_alien():
    '''
    Given a cell with an alien
    When calling __str__ method
    Then it should return 'G:1'
    '''
    # Arrange
    cell = Cell()
    alien = Alien(Team.GREEN)
    cell.add_alien(alien)

    # Act
    res = cell.__str__()

    # Assert
    assert res == 'G:1'


def test_string_for_all():
    '''
    Given a cell with all the aliens
    When calling __str__ method
    Then it should return 'B:1G:1'
    '''
    # Arrange
    cell = Cell()
    cell.add_alien(Team.GREEN)
    cell.add_alien(Team.BLUE)

    # Act
    res = cell.__str__()

    # Assert
    assert res == 'G:1B:1'


def test_str_with_modifier():
    '''
    Given a cell with a multiplier modifier
    When calling __str__ method
    Then it should return '2'
    '''
    # Arrange
    cell = Cell()
    cell.modifier = Modifier.MULTIPLIER

    # Act
    res = cell.__str__()

    # Assert
    assert res == '2'


def test_str_with_alterator():
    '''
    Given a cell with a trap alterator
    When calling __str__ method
    Then it should return 'TRAP'
    '''
    # Arrange
    cell = Cell()
    cell.alterator = Alterator.TRAP

    # Act
    res = cell.__str__()

    # Assert
    assert res == 'TRAP'


def test_str_with_nothing():
    '''
    Given a cell empty
    When calling __str__ method
    Then it should return ' '
    '''
    # Arrange
    cell = Cell()

    # Act
    res = cell.__str__()

    # Assert
    assert res == ' '


def test_from_string_with_alien():
    '''
    Given a string with an alien
    When calling from_string method
    Then it should return a cell with an alien
    '''
    # Arrange
    cell_str = 'G:1'

    # Act
    cell = Cell.from_string(cell_str)

    # Assert
    assert len(cell.aliens) == 1
    assert cell.aliens[0].team == Team.GREEN
    assert cell.aliens[0].eyes == 1


def test_from_string_empty_cell():
    # Arrange
    cell_str = '   '

    # Act
    cell = Cell.from_string(cell_str)

    # Assert
    assert len(cell.aliens) == 0
    assert cell.modifier is None
    assert cell.alterator is None


def test_from_string_blue_alien():
    # Arrange
    cell_str = 'B:1'

    # Act
    cell = Cell.from_string(cell_str)

    # Assert
    assert len(cell.aliens) == 1
    assert cell.aliens[0].team == Team.BLUE
    assert cell.aliens[0].eyes == 1
    assert cell.modifier is None
    assert cell.alterator is None


def test_from_string_green_alien():
    # Arrange
    cell_str = 'G:2'

    # Act
    cell = Cell.from_string(cell_str)

    # Assert
    assert len(cell.aliens) == 1
    assert cell.aliens[0].team == Team.GREEN
    assert cell.aliens[0].eyes == 2
    assert cell.modifier is None
    assert cell.alterator is None


def test_from_string_directioner_alterator():
    # Arrange
    cell_str = ' D '

    # Act
    cell = Cell.from_string(cell_str)

    # Assert
    assert len(cell.aliens) == 0
    assert cell.modifier is None
    assert cell.alterator == Alterator.DIRECTIONER


def test_from_string_mountain_range_modifier():
    # Arrange
    cell_str = ' M '

    # Act
    cell = Cell.from_string(cell_str)

    # Assert
    assert len(cell.aliens) == 0
    assert cell.modifier == Modifier.MOUNTAIN_RANGE
    assert cell.alterator is None


def test_from_string_killer_modifier():
    # Arrange
    cell_str = ' K '

    # Act
    cell = Cell.from_string(cell_str)

    # Assert
    assert len(cell.aliens) == 0
    assert cell.modifier == Modifier.KILLER
    assert cell.alterator is None


def test_from_string_multiplier_modifier():
    # Arrange
    cell_str = ' 2 '

    # Act
    cell = Cell.from_string(cell_str)

    # Assert
    assert len(cell.aliens) == 0
    assert cell.modifier == Modifier.MULTIPLIER
    assert cell.alterator is None


def test_from_string_invalid_cell_string():
    # Arrange
    cell_str = 'invalid'

    # Act & Assert
    with pytest.raises(ValueError):
        Cell.from_string(cell_str)


def test_from_string_green_alien_without_number():
    # Arrange
    cell_str = ' G '

    # Act
    cell = Cell.from_string(cell_str)

    # Assert
    assert len(cell.aliens) == 1
    assert cell.aliens[0].team == Team.GREEN
    assert cell.aliens[0].eyes == 1
    assert cell.modifier is None
    assert cell.alterator is None


def test_from_string_blue_alien_without_number():
    # Arrange
    cell_str = ' B '

    # Act
    cell = Cell.from_string(cell_str)

    # Assert
    assert len(cell.aliens) == 1
    assert cell.aliens[0].team == Team.BLUE
    assert cell.aliens[0].eyes == 1
    assert cell.modifier is None
    assert cell.alterator is None


def test_action_modifier_killer():
    # Arrange
    cell = Cell()
    cell.aliens = [Alien(Team.BLUE), Alien(Team.GREEN)]
    cell.modifier = Modifier.KILLER

    # Act
    cell.action_modifier()

    # Assert
    assert len(cell.aliens) == 0


def test_action_modifier_multiplier():
    # Arrange
    cell = Cell()
    cell.aliens = [Alien(Team.BLUE)]
    cell.modifier = Modifier.MULTIPLIER

    # Act
    cell.action_modifier()

    # Assert
    assert len(cell.aliens) == 2


def test_action_alterator_trap():
    # Arrange
    cell = Cell()
    cell.aliens = [Alien(Team.BLUE), Alien(Team.GREEN)]
    cell.alterator = Alterator.TRAP

    # Act
    cell.action_alterator()

    # Assert
    assert len(cell.aliens) == 0


def test_cell_with_alterator_trap():
    cell = Cell()
    cell.alterator = Alterator.TRAP
    cell.add_alien(Team.GREEN)
    cell.action()
    assert cell.aliens == []
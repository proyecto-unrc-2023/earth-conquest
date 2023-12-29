import pytest

from app.backend.models.alien import Alien
from app.backend.models.team import Team


@pytest.fixture
def reset_id():
    Alien._id_counter = 0


def test_create_alien(reset_id):
    """
    Given a team, when creating an Alien
    Then the Alien should have one eye and belong to the given team
    """
    # Arrange
    team = Team.BLUE

    # Act
    alien = Alien(team)

    # Assert
    assert alien.eyes == 1
    assert alien.team == team


def test_string_for_blue_team(reset_id):
    """
    Given an Alien belonging to the blue team
    When calling the __str__ method
    Then it should return 'B:1'
    """
    # Arrange
    team = Team.BLUE
    alien = Alien(team)

    # Act
    res = alien.__str__()

    # Assert
    assert res == 'B:1'


def test_string_for_green_team(reset_id):
    """
    Given an Alien belonging to the green team
    When calling the __str__ method
    Then it should return 'G:1'
    """
    # Arrange
    team = Team.GREEN
    alien = Alien(team)

    # Act
    res = alien.__str__()

    # Assert
    assert res == 'G:1'


def test_create_two_aliens(reset_id):
    """
    Given two teams
    When creating two Aliens, one for each team
    Then each Alien should have a different id
    """
    # Arrange
    team1 = Team.BLUE
    team2 = Team.GREEN

    # Act
    alien1 = Alien(team1)
    alien2 = Alien(team2)

    # Assert
    assert alien1.id == 1
    assert alien2.id == 2


def test_create_with_corrects_ids(reset_id):
    """
    Given a counter value of 777
    When creating two Aliens
    Then each Alien should have an id greater than 777
    """
    # Arrange
    Alien._id_counter = 777
    team1 = Team.BLUE
    team2 = Team.GREEN

    # Act
    alien1 = Alien(team1)
    alien2 = Alien(team2)

    # Assert
    assert alien1.id == 778
    assert alien2.id == 779


def test_add_eyes(reset_id):
    """
    Given an Alien
    When adding 2 eyes
    Then the Alien should have 3 eyes
    """
    # Arrange
    team = Team.BLUE
    alien = Alien(team)

    # Act
    alien.add_eyes(2)

    # Assert
    assert alien.eyes == 3


def test_elimination_alien(reset_id):
    """
    Given an Alien
    When adding 10 eyes
    Then the Alien should be eliminated
    """
    # Arrange
    team = Team.BLUE
    alien = Alien(team)

    # Act
    eliminated_object = alien.add_eyes(10)

    # Assert
    assert eliminated_object is None

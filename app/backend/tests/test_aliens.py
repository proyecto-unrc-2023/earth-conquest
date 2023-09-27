import pytest

from app.backend.models.alien import Alien, Team


@pytest.fixture
def reset_id():
    Alien._id_counter = 0


def test_create_alien(reset_id):
    alien1 = Alien(Team.BLUE)
    assert alien1.eyes.__eq__(1)
    assert alien1.team.__eq__(Team.BLUE)


def test_string_for_blue_team(reset_id):
    alien = Alien(Team.BLUE)
    res = alien.__str__()
    assert res.__eq__('BLUE')


def test_string_for_green_team(reset_id):
    alien = Alien(Team.GREEN)
    res = alien.__str__()
    assert res.__eq__('GREEN')


def test_create_two_aliens(reset_id):
    i = 1
    alien1 = Alien(Team.BLUE)
    alien2 = Alien(Team.GREEN)
    assert alien1.id.__eq__(i)
    assert alien2.id.__eq__(i+1)


def test_create_with_corrects_ids(reset_id):
    Alien._id_counter = 777
    i = 778
    alien1 = Alien(Team.BLUE)
    alien2 = Alien(Team.GREEN)
    assert alien1.id.__eq__(i)
    assert alien2.id.__eq__(i+1)


def test_add_eyes(reset_id):
    alien = Alien(Team.BLUE)
    alien.add_eyes(2)
    assert alien.eyes.__eq__(3)


def test_elimination_alien(reset_id):
    alien1 = Alien(Team.BLUE)
    eliminated_object = alien1.add_eyes(10)
    assert eliminated_object is None

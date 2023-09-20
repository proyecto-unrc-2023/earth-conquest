import pytest

from app.models.alien import Team, Alien
from app.models.cell import Cell


def test_create_a_cell():
    cell = Cell()
    assert cell.aliens.__eq__(None)
    assert cell.modifier.__eq__(None)
    assert cell.alterator.__eq__(None)


def test_add_aliens():
    alien = Alien(Team.BLUE)
    cell = Cell()
    cell.add_alien(alien)
    cell.add_alien(Team.GREEN)
    assert len(cell.aliens).__eq__(2)
    assert isinstance(cell.aliens[0], Alien)


def test_remove_alien():
    alien1 = Alien(Team.BLUE)
    cell = Cell()
    cell.add_alien(Alien(Team.GREEN))
    cell.add_alien(alien1)
    cell.add_alien(Alien(Team.GREEN))
    assert len(cell.aliens) == 3
    cell.remove_alien(alien1)
    assert len(cell.aliens) == 2


def test_insert_only_aliens():
    cell = Cell()
    with pytest.raises(ValueError):
        cell.add_alien(2)


def test_remove_only_aliens():
    cell = Cell()
    with pytest.raises(ValueError):
        cell.remove_alien(7)


def test_for_two_aliens_fight():
    alien1 = Alien(Team.BLUE)
    alien2 = Alien(Team.GREEN)
    alien1.add_eyes(2)
    eyes1 = alien1.eyes
    cell = Cell()
    cell.add_alien(alien1)
    cell.add_alien(alien2)
    cell.fight()
    assert cell.aliens.__eq__(alien1)
    assert len(cell.aliens).__eq__(1)
    assert alien1.eyes.__eq__(eyes1-alien2.eyes)


    # next test

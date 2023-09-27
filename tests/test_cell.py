import pytest

from app.models.alien import Team, Alien
from app.models.cell import Cell


@pytest.fixture
def add_two_same_team_aliens_in_a_cell():
    cell = Cell()
    cell.add_alien(Alien(Team.BLUE))
    cell.add_alien(Alien(Team.BLUE))
    return cell


@pytest.fixture
def add_two_diff_team_aliens_in_a_cell():
    cell = Cell()
    cell.add_alien(Alien(Team.BLUE))
    cell.add_alien(Alien(Team.GREEN))
    return cell


def test_create_a_cell():
    cell = Cell()
    assert cell.aliens.__eq__([])
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


def test_for_two_aliens_fight_wins_alien1(add_two_diff_team_aliens_in_a_cell):
    cell = add_two_diff_team_aliens_in_a_cell
    alien1 = cell.aliens[0]
    alien2 = cell.aliens[1]
    alien1.add_eyes(2)
    eyes1 = alien1.eyes
    cell.fight()
    assert cell.aliens[0] is alien1
    assert len(cell.aliens).__eq__(1)
    assert alien1.eyes.__eq__(eyes1 - alien2.eyes)


def test_for_two_aliens_fight_wins_alien2(add_two_diff_team_aliens_in_a_cell):
    cell = add_two_diff_team_aliens_in_a_cell
    alien1 = cell.aliens[0]
    alien2 = cell.aliens[1]
    alien2.add_eyes(2)
    eyes2 = alien2.eyes
    cell.fight()
    assert cell.aliens[0] is alien2
    assert len(cell.aliens).__eq__(1)
    assert alien2.eyes.__eq__(eyes2 - alien1.eyes)


def test_for_three_aliens_fight(add_two_diff_team_aliens_in_a_cell):
    cell = add_two_diff_team_aliens_in_a_cell
    cell.add_alien(Alien(Team.GREEN))
    with pytest.raises(ValueError):
        cell.fight()


def test_all_aliens_same_team(add_two_same_team_aliens_in_a_cell):
    cell = add_two_same_team_aliens_in_a_cell
    assert cell.all_aliens_same_team()


def test_no_same_team(add_two_diff_team_aliens_in_a_cell):
    cell = add_two_diff_team_aliens_in_a_cell
    assert not cell.all_aliens_same_team()


def test_sum_aliens_eyes(add_two_same_team_aliens_in_a_cell):
    cell = add_two_same_team_aliens_in_a_cell
    cell.add_alien(Alien(Team.GREEN))
    eyes = cell.sum_aliens_eyes()
    assert eyes.__eq__(3)


def test_two_aliens_reproduction(add_two_same_team_aliens_in_a_cell):
    cell = add_two_same_team_aliens_in_a_cell
    cell.reproduce()
    assert len(cell.aliens) is 1
    assert cell.aliens[0].eyes is 2


def test_three_aliens_reproduction(add_two_same_team_aliens_in_a_cell):
    cell = add_two_same_team_aliens_in_a_cell
    cell.add_alien(Team.BLUE)
    cell.reproduce()
    assert len(cell.aliens) is 1
    assert cell.aliens[0].eyes is 3


def test_one_alien_reproduction():
    cell = Cell()
    cell.add_alien(Team.BLUE)
    with pytest.raises(ValueError):
        cell.reproduce()


def test_aliens_reproduction_with_different_teams(add_two_diff_team_aliens_in_a_cell):
    cell = add_two_diff_team_aliens_in_a_cell
    with pytest.raises(ValueError):
        cell.reproduce()


def test_alien_reproduction_where_total_eyes_greater_than_five(add_two_same_team_aliens_in_a_cell):
    cell = add_two_same_team_aliens_in_a_cell
    team = cell.aliens[0].team
    alien1 = Alien(team)
    alien2 = Alien(team)
    alien1.add_eyes(2)
    alien2.add_eyes(2)
    cell.add_alien(alien1)
    cell.add_alien(alien2)
    cell.reproduce()
    assert len(cell.aliens) is 0


def test_alien_reproduction_where_total_eyes_lesser_than_five(add_two_same_team_aliens_in_a_cell):
    cell = add_two_same_team_aliens_in_a_cell
    team = cell.aliens[0].team
    alien1 = Alien(team)
    alien2 = Alien(team)
    cell.add_alien(alien1)
    cell.add_alien(alien2)
    cell.reproduce()
    assert len(cell.aliens) is 1
    assert cell.aliens[0].eyes is 4


def test_action_cell_3_blue_aliens_vs_1_green_aliens(add_two_same_team_aliens_in_a_cell):
    cell = add_two_same_team_aliens_in_a_cell  # Creo una celda con dos aliens de un mismo equipo con 1 ojo cada uno
    cell.add_alien(Team.BLUE)  # Se le añade un alien del mismo equipo que los anteriores, con 1 ojo
    cell.add_alien(Team.GREEN)  # Se le añade un alien de un ojo, del otro equipo diferente
    cell.action()
    assert len(cell.aliens) is 1  # Deberia quedar un solo alien, del equipo azul
    assert cell.aliens[0].eyes is 2  # Ese alien deberia tener dos ojos, ya que el que se reprodujo en action() obtuvo 3
    # menos 1 con el que peleo del equipo verde
    assert cell.aliens[0].team is Team.BLUE  # Ganador equipo azul


def test_action_cell_2_blue_aliens_vs_2_green_aliens(add_two_same_team_aliens_in_a_cell):
    cell = add_two_same_team_aliens_in_a_cell
    cell.add_alien(Team.GREEN)
    cell.add_alien(Team.GREEN)
    cell.action()
    assert len(cell.aliens) is 0


def test_action_cell_1_blue_aliens_vs_3_green_aliens(add_two_diff_team_aliens_in_a_cell):
    cell = add_two_diff_team_aliens_in_a_cell
    cell.add_alien(Team.GREEN)
    cell.add_alien(Team.GREEN)
    cell.action()
    assert len(cell.aliens) is 1  # Debera quedar un solo alien, del equipo verde
    assert cell.aliens[0].eyes is 2  # Ese alien debería tener dos ojos, ya que el alien verde que se reprodujo
    # en action() obtuvo 3, menos 1 con el que peleo del equipo verde
    assert cell.aliens[0].team is Team.GREEN  # Ganador equipo VERDE


def test_action_cell_with_aliens_of_the_same_team(add_two_same_team_aliens_in_a_cell):
    cell = add_two_same_team_aliens_in_a_cell
    cell.action()
    assert len(cell.aliens) is 1
    assert cell.aliens[0].eyes is 2

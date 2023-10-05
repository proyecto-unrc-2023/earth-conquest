from enum import Enum

from app.backend.models import modifier, directioner
from app.backend.models.alien import Alien, Team
from app.backend.models.alterator import Alterator
from app.backend.models.modifier import Modifier


class Cell:

    def __init__(self):
        self.aliens = []
        self.alterator = None
        self.modifier = None

    def add_alien(self, team_or_alien):
        if isinstance(team_or_alien, Alien):
            self.aliens.insert(len(self.aliens) + 1, team_or_alien)
        elif isinstance(team_or_alien, Team):
            self.aliens.insert(len(self.aliens) + 1, Alien(team_or_alien))
        else:
            raise ValueError(
                f'you can only insert an alien by indicating its equipment or by inserting an alien itself')

    def remove_alien(self, alien):
        if isinstance(alien, Alien):
            self.aliens.remove(alien)
        else:
            raise ValueError(f'you can only remove aliens')

    def fight(self):
        if len(self.aliens).__eq__(2) and (self.aliens[0].team != self.aliens[1].team):
            eyes1 = self.aliens[0].eyes
            eyes2 = self.aliens[1].eyes
            if eyes1 > eyes2:
                eyes1 -= eyes2
                self.aliens[0].eyes = eyes1
                self.aliens.remove(self.aliens[1])
            elif eyes2 > eyes1:
                eyes2 -= eyes1
                self.aliens[1].eyes = eyes2
                self.aliens.remove(self.aliens[0])
            else:
                self.aliens = []
        else:
            raise ValueError(f'fight is only two aliens')

    def reproduce(self):
        if self.all_aliens_same_team() and len(self.aliens) > 1:
            team = self.aliens[0].team
            eyes = self.sum_aliens_eyes()
            self.aliens = []
            alien = Alien(team)
            alien.add_eyes(eyes - 1)
            if not (eyes > 5):
                self.add_alien(alien)
        else:
            raise ValueError(f'reproduce is only with same teams aliens and more one alien')

    def action(self):
        if not self.all_aliens_same_team():
            aliens = self.divide_aliens_for_different_teams()
            aliens1 = aliens[0]
            aliens2 = aliens[1]
            cell_aux = Cell()
            self.aliens = aliens1
            cell_aux.aliens = aliens2
            if len(self.aliens) > 1:
                self.reproduce()
            if len(cell_aux.aliens) > 1:
                cell_aux.reproduce()
            for i in range(len(cell_aux.aliens)):
                self.add_alien(cell_aux.aliens[i])
            self.fight()
        elif len(self.aliens) > 1:
            self.reproduce()
        if self.modifier == Modifier.MULTIPLIER or self.modifier == Modifier.KILLER:
            self.action_modifier()
        if self.alterator == Alterator.TRAP:
            self.action_alterator()

    def sum_aliens_eyes(self):
        eyes = 0
        for i in range(len(self.aliens)):
            eyes += self.aliens[i].eyes
        return eyes

    def all_aliens_same_team(self):
        for i in range(len(self.aliens)):
            if not self.aliens[0].team == self.aliens[i].team:
                return False
        return True

    def divide_aliens_for_different_teams(self):
        aliens_team1 = []
        aliens_team2 = []
        for i in range(len(self.aliens)):
            if self.aliens[i].team == Team.BLUE:
                aliens_team1.append(self.aliens[i])
            else:
                aliens_team2.append(self.aliens[i])
        all_aliens = [aliens_team1, aliens_team2]
        return all_aliens

    def __str__(self):
        if self.aliens:
            return 'A'
        if self.modifier is modifier.Modifier.MOUNTAIN_RANGE:
            return 'M'
        if self.modifier is modifier.Modifier.KILLER:
            return 'K'
        if self.modifier is modifier.Modifier.MULTIPLIER:
            return '2'
        if self.alterator is directioner:
            return 'D'
        return ' '

    @staticmethod
    def from_string(cell_str):
        if cell_str == '   ':
            return Cell()
        elif cell_str == ' B ':
            cell = Cell()
            cell.add_alien(Team.BLUE)
            return cell
        elif cell_str == ' G ':
            cell = Cell()
            cell.add_alien(Team.GREEN)
            return cell
        elif cell_str == ' D ':
            cell = Cell()
            cell.alterator = directioner
            return cell
        elif cell_str == ' M ':
            cell = Cell()
            cell.modifier = Modifier.MOUNTAIN_RANGE
            return cell
        elif cell_str == ' K ':
            cell = Cell()
            cell.modifier = Modifier.KILLER
            return cell
        elif cell_str == ' 2 ':
            cell = Cell()
            cell.modifier = Modifier.MULTIPLIER
            return cell
        else:
            raise ValueError(f'Invalid cell string: {cell_str}')

    def action_modifier(self):
        if self.modifier == Modifier.KILLER:
            self.aliens = []
        elif self.modifier == Modifier.MULTIPLIER:
            self.aliens.append(self.aliens[0])

    def action_alterator(self):
        if self.alterator == Alterator.TRAP:
            self.aliens = []

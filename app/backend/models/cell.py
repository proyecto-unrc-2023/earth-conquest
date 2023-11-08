from marshmallow import Schema, fields

from app.backend.models import modifier, directioner
from app.backend.models import alterator
from app.backend.models.alien import Alien, Team, AlienSchema
from app.backend.models.alterator import Alterator
from app.backend.models.directioner import Directioner, DirectionerSchema
from app.backend.models.modifier import Modifier
from app.backend.models.teleporter import Teleporter, TeleporterSchema


class Cell:

    def __init__(self):
        self.aliens = []
        self.alterator = None
        self.modifier = None

    """
    Given an alien or a team, adds it to the list aliens.
    If argument is a team, a new alien from that team is created and 
    added to the aliens list.
    """

    def add_alien(self, team_or_alien):
        if isinstance(team_or_alien, Alien):
            self.aliens.insert(len(self.aliens) + 1, team_or_alien)
        elif isinstance(team_or_alien, Team):
            self.aliens.insert(len(self.aliens) + 1, Alien(team_or_alien))
        else:
            raise ValueError(
                f'you can only insert an alien by indicating its team or by inserting an alien itself')

    """
    Given an alien on the list of aliens, it removes it from the list.
    """

    def remove_alien(self, alien):
        if isinstance(alien, Alien):
            self.aliens.remove(alien)
        else:
            raise ValueError(f'you can only remove aliens')

    """
    This method makes two aliens from different teams fight with eachother.
    The aliens list is updated with the result of the fight.
    """

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
            raise ValueError(f'fight method is only applicable for two aliens')

    """
    This method makes aliens from the same team reproduce with each other.
    The aliens list is updated with the result of the reproduction.
    """

    def reproduce(self):
        if self.all_aliens_same_team() and len(self.aliens) > 1:
            team = self.aliens[0].team
            eyes = self.sum_aliens_eyes()
            self.aliens.clear()
            if not (eyes > 5):
                alien = Alien(team, eyes)
                self.aliens.append(alien)
        else:
            raise ValueError(f'this method is only applicable for aliens from the same team and for at least 2 aliens')

    """
    This method acts on the aliens list. It makes the aliens reproduce and/or fight according
    to the circumstances. If there's a modifier or trap (alterator) on the cell, it makes 
    it act on the aliens.
    """

    def action(self):
        if not self.all_aliens_same_team():
            if self.aliens.__len__() > 2:
                aliens_blue, aliens_green = self.divide_aliens_for_different_teams()    # divido aliens por equipo
                blue_eyes = self.sum_eyes_list_of_aliens(aliens_blue)   # suma de todos los ojos de cada equipos
                green_eyes = self.sum_eyes_list_of_aliens(aliens_green)
                self.aliens.clear()     # all aliens removed
                if blue_eyes > green_eyes:
                    eyes_of_winner_alien = blue_eyes - green_eyes
                    winner_alien = Alien(Team.BLUE, eyes_of_winner_alien)
                    self.aliens.append(winner_alien)
                elif green_eyes > blue_eyes:
                    eyes_of_winner_alien = green_eyes - blue_eyes
                    winner_alien = Alien(Team.GREEN, eyes_of_winner_alien)
                    self.aliens.append(winner_alien)
                # un else es que sean de igual cantidad, todos mueren, se hace arriba ya con .clear()

            else:   # two different team aliens fight
                self.fight()
        elif self.aliens.__len__() > 1:  # reproduces aliens of the same team
            self.reproduce()
        if self.aliens != [] and self.modifier == Modifier.MULTIPLIER or self.modifier == Modifier.KILLER:
            self.action_modifier()
        if self.aliens != [] and self.alterator == Alterator.TRAP:
            self.action_alterator()

    """
    Method that returns the sum of all the eyes of the aliens in the aliens list.
    """

    def sum_aliens_eyes(self):
        eyes = 0
        for i in range(len(self.aliens)):
            eyes += self.aliens[i].eyes
        return eyes

    def sum_eyes_list_of_aliens(self, aliens):
        sum = 0
        for alien in aliens:
            sum += alien.eyes
        return sum

    """
    Method that returns True if all aliens on the list of aliens are from the same team.
    """

    def all_aliens_same_team(self):
        team = self.aliens[0].team
        for alien in self.aliens:
            if alien.team is not team:
                return False
        return True

    """
    Returns a list of two lists. First list containing all the aliens on the blue team,
    second list containing all the aliens on the green team.
    """

    def divide_aliens_for_different_teams(self):
        aliens_blue = []
        aliens_green = []
        for alien in self.aliens:
            if alien.team == Team.BLUE:
                aliens_blue.append(alien)
            else:
                aliens_green.append(alien)
        return aliens_blue, aliens_green

    def __str__(self):
        if self.aliens:
            res = ""
            for i in range(len(self.aliens)):
                res += self.aliens[i].__str__()
            return res
        if self.modifier is modifier.Modifier.MOUNTAIN_RANGE:
            return 'M'
        if self.modifier is modifier.Modifier.KILLER:
            return 'K'
        if self.modifier is modifier.Modifier.MULTIPLIER:
            return '2'
        if isinstance(self.alterator, Directioner):
            return 'D'
        if isinstance(self.alterator, Teleporter):
            return 'T'
        if self.alterator is alterator.Alterator.TRAP:
            return 'TRAP'
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

    """
    Method that makes a modifier act on the current alien
    on the cell.
    """

    def action_modifier(self):
        if self.modifier == Modifier.KILLER:
            self.aliens = []
        elif self.modifier == Modifier.MULTIPLIER:
            self.aliens.append(self.aliens[0])

    """
    Method that makes a Trap act on the current alien 
    on the cell.
    """

    def action_alterator(self):
        if self.alterator == Alterator.TRAP:
            self.aliens = []


class AlteratorField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if isinstance(obj.alterator, Directioner):
            return DirectionerSchema().dump(obj.alterator)
        elif isinstance(obj.alterator, Teleporter):
            return TeleporterSchema().dump(obj.alterator)
        elif obj.alterator == Alterator.TRAP:
            return Alterator.TRAP.name
        else:
            return None


class CellSchema(Schema):
    aliens = fields.List(fields.Nested(AlienSchema()))
    modifier = fields.Enum(Modifier)
    alterator = AlteratorField()

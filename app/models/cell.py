from enum import Enum

from app.models.alien import Alien, Team


class Cell:

    def __init__(self):
        self.aliens = []
        self.alterator = None
        self.modifier = None

    def add_alien(self, team_or_alien):
        if isinstance(team_or_alien, Alien):
            self.aliens.insert(len(self.aliens) + 1, team_or_alien)
        elif isinstance(team_or_alien, Team):
            self.aliens.insert(len(self.aliens)+1, Alien(team_or_alien))
        else:
            raise ValueError(f'you can only insert an alien by indicating its equipment or by inserting an alien itself')

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
            else:
                eyes2 -= eyes1
                self.aliens[1].eyes = eyes2
                self.aliens.remove(self.aliens[0])

    #def all_aliens_same_team(self):
    #    for a in self.aliens:
    #        if not self.aliens[0].team == self.aliens[a].team:
    #            return False
    #    return True


class Alterator(Enum):
    TELEPORT = 1
    TRAP = 2
    DIRECTIONER = 3


class Modifier(Enum):
    KILLER = 1
    MULTIPLICATOR = 2
    MOUNTAIN = 3


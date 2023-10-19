 Feature: Game Over

  Background:
    Given a new game has started

  Scenario Outline: Alien of team "<attacking_team>" ATTACKS "<attacked_team>" alien base
    Given a base of "<attacked_team>" team with <life_points> points of life
    And an alien of "<attacking_team>" team in the cell (<x>, <y>) with <alien_eyes> eyes
    When the board acts
    Then the base has <results_life_points> life points
    And the alien is not in the cell (<x>, <y>)
  Examples:
    | attacking_team  | attacked_team | life_points | results_life_points | x | y   | alien_eyes |
    | GREEN           | BLUE          | 15          | 12                  | 6 | 12  | 3          |
    | BLUE            | GREEN         | 10          | 5                   | 2 | 2   | 5          |

  Scenario Outline: Alien of team "<attacking_team>" DESTROYS "<attacked_team>" alien base
    Given a base of "<attacked_team>" team with <life_points> points of life
    And an alien of "<attacking_team>" team in the cell (<x>, <y>) with <alien_eyes> eyes
    When the board acts
    Then the base has <results_life_points> life points
    And the alien is not in the cell (<x>, <y>)
    And it is destroyed
    And game is over
    And "<attacking_team>" wins
  Examples:
    | attacking_team  | attacked_team | life_points | results_life_points | x | y   | alien_eyes |
    | GREEN           | BLUE          | 3           | 0                   | 6 | 12  | 3          |
    | BLUE            | GREEN         | 2           | -2                  | 2 | 2   | 4          |
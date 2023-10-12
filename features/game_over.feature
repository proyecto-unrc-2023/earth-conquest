 Feature: Game Over

  Background:
    Given a new game has started

  Scenario Outline: Alien of team "<attacking_team>" attacks "<attacked_team>" alien base
    Given a base of "<attacked_team>" team with <life_points> points of life
    And a "<attacking_team>" alien with <alien_eyes> eyes is positioned on the cell in the "<attacked_team>" base range
    When the board acts
    Then the base has <results_life_points>
  Examples:
  | attacking_team  | attacked_team | life_points | alien_eyes | results_life_points |
  | green           | blue          | 15          | 3          | 12                  |
  | blue            | green         | 10          | 5          | 5                   |

  Scenario Outline: Alien of team "<attacking_team>" destroy "<attacked_team>" alien base
    Given a base of "<attacked_team>" team with <life_points> points of life
    And a "<attacking_team>" alien with <alien_eyes> eyes is positioned on the cell in the "<attacked_team>" base range
    When the board acts
    Then the base has <results_life_points>
    And it is destroyed
    And game is over
    And "<attacking_team>" wins
  Examples:
  | attacking_team  | attacked_team | life_points    | alien_eyes | results_life_points |
  | green           | blue          | 3              | 5          | -2                  |
  | blue            | green         | 5              | 5          | 0                   |

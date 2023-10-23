Feature: Alien Reproduction

  Background: game created and start a game
    Given that I have a game with the following board:
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14|
    |   |   |   |   |   |   |   |   |   |   |   | 2 |   |   |   |
    |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   | M |   |   |   |   |   | K |   |
    |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
    | K |   |   |   | M | M | M |   |   |   |   |   |   |   |   |
    |   |   | 2 |   |   |   |   |   |   |   |   |   |   |   |   |

  Scenario Outline: two aliens reproduce
    Given I have 2 aliens in the square (6,6) of same team
    And the number of eyes of alien 1 is <alien1_eyes>
    And the number of eyes of alien 2 is <alien2_eyes>
    When the board acts
    Then I "<should_or_not>" have an alien with <reproduction_eyes> eyes in the square (6,6)  
  Examples:
  | alien1_eyes | alien2_eyes | should_or_not | reproduction_eyes |
  | 1           | 1           | should        | 2                 |
  | 2           | 2           | should        | 4                 |
  | 3           | 3           | should not    | 6                 |
  | 4           | 4           | should not    | 8                 |

  Scenario Outline: three aliens reproduce
    Given I have 3 aliens in the square (6,6) of same team
    And the number of eyes of alien 1 is <alien1_eyes>
    And the number of eyes of alien 2 is <alien2_eyes>
    And the number of eyes of alien 3 is <alien3_eyes>
    When the board acts
    Then I "<should_or_not>" have an alien with <reproduction_eyes> eyes in the square (6,6)
  Examples:
  | alien1_eyes | alien2_eyes | alien3_eyes | should_or_not | reproduction_eyes |
  | 1           | 1           | 1           | should        | 3                 |
  | 1           | 2           | 2           | should        | 5                 |
  | 2           | 2           | 2           | should not    | 6                 |
  | 4           | 4           | 4           | should not    | 12                |

  Scenario Outline: four aliens reproduce
    Given I have 4 aliens in the square (6,6) of same team
    And the number of eyes of alien 1 is <alien1_eyes>
    And the number of eyes of alien 2 is <alien2_eyes>
    And the number of eyes of alien 3 is <alien3_eyes>
    And the number of eyes of alien 4 is <alien4_eyes>
    When the board acts
    Then I "<should_or_not>" have an alien with <reproduction_eyes> eyes in the square (6,6)
  Examples:
  | alien1_eyes | alien2_eyes | alien3_eyes | alien4_eyes | should_or_not | reproduction_eyes |
  | 1           | 1           | 1           | 1           | should        | 4                 |
  | 1           | 1           | 1           | 2           | should        | 5                 |
  | 1           | 2           | 2           | 2           | should not    | 7                 |
  | 2           | 2           | 2           | 2           | should not    | 8                 |

Feature: Alien Reproduction

  Background: game created and start a game
    Given the aliens has been generated
    And there are aliens in the square (2,2) of the same team

  Scenario Outline: two alien reproduction
    Given that the number of eyes of alien 1 is <alien1_eyes>
    And the number of eyes of alien 2 is <alien2_eyes>
    When they reproduce
    Then the alien resulting from reproduction should "<survive_or_die>"
    And if the alien survives, it should have <reproduction_eyes> eyes

    Examples:
    | alien1_eyes | alien2_eyes | reproduction_eyes | survive_or_die   |
    | 1           | 1           | 2                 | survive          |
    | 1           | 4           | 5                 | survive          |
    | 4           | 2           | 0                 | die              |
    | 5           | 5           | 0                 | die              |

  Scenario Outline: three alien reproduction
    Given that the number of eyes of alien 1 is <alien1_eyes>
    And the number of eyes of alien 2 is <alien2_eyes>
    And the number of eyes of alien 3 is <alien3_eyes>
    When they reproduce
    Then the alien resulting from reproduction should "<survive_or_die>"
    And if the alien survives, it should have <reproduction_eyes> eyes

    Examples:
    | alien1_eyes | alien2_eyes | alien3_eyes | reproduction_eyes | survive_or_die   |
    | 1           | 1           | 1           | 3                 | survive          |
    | 1           | 4           | 3           | 0                 | die              |
    | 2           | 2           | 1           | 5                 | survive          |
    | 5           | 5           | 5           | 0                 | die              |

  Scenario Outline: four alien reproduction
    Given that the number of eyes of alien 1 is <alien1_eyes>
    And the number of eyes of alien 2 is <alien2_eyes>
    And the number of eyes of alien 3 is <alien3_eyes>
    And the number of eyes of alien 4 is <alien4_eyes>
    When they reproduce
    Then the alien resulting from reproduction should "<survive_or_die>"
    And if the alien survives, it should have <reproduction_eyes> eyes

    Examples:
    | alien1_eyes | alien2_eyes | alien3_eyes | alien4_eyes | reproduction_eyes | survive_or_die   |
    | 1           | 1           | 1           | 1           | 4                 | survive          |
    | 1           | 4           | 1           | 2           | 0                 | die              |
    | 1           | 2           | 1           | 1           | 5                 | survive          |
    | 3           | 5           | 2           | 2           | 0                 | die              |
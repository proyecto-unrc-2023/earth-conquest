Feature: Alien Battle

  Background: game created and start a game
    Given the aliens has been generated
    And there are two aliens in the square (2,2)
    And alien 1 is from team BLUE
    And alien 2 is from team GREEN

  Scenario Outline: Alien battle with <alien1_eyes> eyes vs <alien2_eyes> eyes
    Given the number of eyes of alien 1 is <alien1_eyes>
    And the number of eyes of alien 2 is <alien2_eyes>
    When they fight
    Then alien 1 "<outcome1>"
    And alien 2 "<outcome2>"
    And I should have <aliens_left> less aliens

    Examples:
      | alien1_eyes | alien2_eyes | outcome1 | outcome2 | aliens_left |
      | 3           | 3           | dies     | dies     | 2           |
      | 2           | 4           | dies     | lives    | 1           |
      | 4           | 2           | lives    | dies     | 1           |
      | 1           | 5           | dies     | lives    | 1           |
Feature: Alien Battle

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
    And there are two aliens in the square (6,6) of different teams
  
  Scenario Outline: Alien battle with <alien1_eyes> eyes vs <alien2_eyes> eyes
    Given the number of eyes of alien 1 is <alien1_eyes>
    And the number of eyes of alien 2 is <alien2_eyes>
    When the board acts
    Then the number of aliens in the square (6,6) should be <aliens_remained>
    And I should see that alien 1 "<outcome1>" with "<alien1_eyes_after_battle>" eyes
    And I should see that alien 2 "<outcome2>" with "<alien2_eyes_after_battle>" eyes

    Examples:
      | alien1_eyes | alien2_eyes | outcome1 | outcome2 | aliens_remained | alien1_eyes_after_battle | alien2_eyes_after_battle |
      | 3           | 3           | dies     | dies     | 0               | 0                        | 0                        |
      | 2           | 4           | dies     | lives    | 1               | 0                        | 2                        |
      | 4           | 2           | lives    | dies     | 1               | 2                        | 0                        |
      | 1           | 5           | dies     | lives    | 1               | 0                        | 4                        |
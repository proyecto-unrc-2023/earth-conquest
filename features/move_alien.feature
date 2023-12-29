Feature: Alien Movement on the Board

  Background:
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

  Scenario Outline: alien moves to an adjoining position when the game refreshes
    Given an alien is on the cell <row> <column>
    When the board refreshes
    Then the alien moves to one of its adjoining positions
    And the new alien position is free of mountains
    And the new alien posiiton is within the board's perimeter

    Examples:
        | row    | column | 
        |     2  |      2 |
        |     5  |      5 | 
        |     3  |      8 |
        |     8  |      0 |
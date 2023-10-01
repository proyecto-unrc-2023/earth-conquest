Feature: Alien Movement on the Board

Background:
  Given a new game has started

  Scenario Outline: alien moves to an adjoining position when the game refreshes
    Given an alien is on the cell <row> <column>
    When the game refreshes
    Then the alien moves to one of its adjoining, free of mountains and within the board's perimeter cell

    Examples:
        | row    | column | 
        |     2  |      2 |
        |     5  |      5 | 
        |     3  |      7 |
        |     8  |      0 |
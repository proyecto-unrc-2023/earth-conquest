Feature: Move an alien

Background:
  Given the game is on

  Scenario Outline: alien moves to an adjoining position only
    Given an alien is in cell <row> <column>
    And the game is in refresh mode
    And the cell <end_row> <end_column> is not a mountain
    And the cell <end_row> <end_column> is within range
    When the alien moves to <end_row> <end_column>
    Then the alien should be in cell <end_row> <end_column>

    Examples:
        | row    | column | number | end_row | end_column |
        |     5  |      4 |      0 |       4 |          4 |
        |     3  |      4 |      1 |       3 |          3 |
        |     1  |      2 |      2 |       2 |          2 |
        |     2  |      2 |      3 |       2 |          3 |

Feature: Alien Movement on the Board

Background:
  Given a new game has started

  Scenario Outline: alien moves to an adjoining position when the game refreshes
    Given an alien is on the cell <row> <column>
    #And the cell <end_row> <end_column> is both free of mountains and within the board's perimeter
    When the game refreshes
    Then the alien moves to one of its adjoining, free of mountains and withing the board's perimeter cell

    Examples:
        | row    | column | 
        |     2  |      2 |
        |     5  |      5 | 
        |     3  |      7 |
        |     8  |      0 |


      #| row    | column | number | end_row | end_column |
      # |     2  |      2 |      0 |       1 |          2 |
      # |     5  |      5 |      1 |       2 |          1 |
      # |     2  |      2 |      2 |       3 |          2 |
      # |     2  |      2 |      3 |       2 |          3 |


#             1   2   3
#         1 |   |   |   |   
#         2 |   | D |   |   
#         3 |   |   |   |
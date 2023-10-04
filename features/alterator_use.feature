Feature: Alterator use

    Background: 
        Given the game has started
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

    Scenario: the alterator chosen is the Directioner and 1 alien moves to the Directioner's cell
        Given the Directioner is positioned horizontally on the cells (5,1), (5,2) and (5,3)
            | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14|
            |   |   |   |   |   |   |   |   |   |   |   | 2 |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   | K |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   | D | D | D |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            | K |   |   |   | M | M | M |   |   |   |   |   |   |   |   |
            |   |   | 2 |   |   |   |   |   |   |   |   |   |   |   |   |
        And a green alien is positioned on the cell (4, 1)
        And the alien moves to an adjacent cell, this one being cell (5,1)
            | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14|
            |   |   |   |   |   |   |   |   |   |   |   | 2 |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   | K |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |GD | D | D |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            | K |   |   |   | M | M | M |   |   |   |   |   |   |   |   |
            |   |   | 2 |   |   |   |   |   |   |   |   |   |   |   |   |
        When the board refreshes
        Then the alien moves to the cell (5,2)
            |   |   |   |   |   |   |   |   |   |   |   | 2 |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   | K |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   | D |GD | D |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            | K |   |   |   | M | M | M |   |   |   |   |   |   |   |   |
            |   |   | 2 |   |   |   |   |   |   |   |   |   |   |   |   |
        When the board refreshes
        Then the alien moves to the cell (5, 3)
            |   |   |   |   |   |   |   |   |   |   |   | 2 |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   | K |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   | D | D |GD |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            | K |   |   |   | M | M | M |   |   |   |   |   |   |   |   |
            |   |   | 2 |   |   |   |   |   |   |   |   |   |   |   |   |

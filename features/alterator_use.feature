Feature: Alterator use

    Background: 
        Given a game has been created
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
        And player "Jose" has joined the game as "green" player
        And player "Juan" has joined the game as "blue" player
        And the game is started


    Scenario: the chosen alterator is the Directioner and one alien moves to the Directioner's cell
        When green player set a horizontally Directioner on the cells (5,1), (5,2) and (5,3)
            | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14|
            |   |   |   |   |   |   |   |   |   |   |   | 2 |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   | K |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   | G |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   | D | D | D |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            | K |   |   |   | M | M | M |   |   |   |   |   |   |   |   |
            |   |   | 2 |   |   |   |   |   |   |   |   |   |   |   |   |
        Then 4 green aliens dies
        When a green alien is positioned on the cell (4, 1)
        And the alien moves to an adjacent cell, this one being cell (5, 1)
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
        And the board refreshes
        Then the alien moves to the cell (5, 2)
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
        When the board refreshes
        Then the alien moves to the cell (5, 4)
            |   |   |   |   |   |   |   |   |   |   |   | 2 |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   | K |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   | D | D | D | G |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            | K |   |   |   | M | M | M |   |   |   |   |   |   |   |   |
            |   |   | 2 |   |   |   |   |   |   |   |   |   |   |   |   |


    Scenario: the chosen alterator is the Teleporter and one alien moves to the Teleporter's door
        When green player set a Teleporter on the cell (4,1) for entry door and (6,10) for exit
            | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14|
            |   |   |   |   |   |   |   |   |   |   |   | 2 |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   | K |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   | D |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   | T |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            | K |   |   |   | M | M | M |   |   |   |   |   |   |   |   |
            |   |   | 2 |   |   |   |   |   |   |   |   |   |   |   |   |
        Then 6 green aliens dies
        When a green alien is positioned on the cell (3, 1)
        And the alien moves to an adjacent cell, this one being cell (4, 1)
            | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14|
            |   |   |   |   |   |   |   |   |   |   |   | 2 |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   | K |   |
            |   | GD|   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   | T |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            | K |   |   |   | M | M | M |   |   |   |   |   |   |   |   |
            |   |   | 2 |   |   |   |   |   |   |   |   |   |   |   |   |
        And the board refreshes
        Then the alien moves to the cell (6, 10)
            | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14|
            |   |   |   |   |   |   |   |   |   |   |   | 2 |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   | K |   |
            |   | D |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   | GT|   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            | K |   |   |   | M | M | M |   |   |   |   |   |   |   |   |
            |   |   | 2 |   |   |   |   |   |   |   |   |   |   |   |   |


    Scenario: the chosen alterator is the Trap and one alien moves to the Trap's cell
        When green player set a Trap on the cell (4, 3)
            | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14|
            |   |   |   |   |   |   |   |   |   |   |   | 2 |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   | K |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   |   |   | T |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            | K |   |   |   | M | M | M |   |   |   |   |   |   |   |   |
            |   |   | 2 |   |   |   |   |   |   |   |   |   |   |   |   |
        Then 4 green aliens dies
        When a green alien is positioned on the cell (3, 3)
        And the alien moves to an adjacent cell, this one being cell (4, 3)
            | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14|
            |   |   |   |   |   |   |   |   |   |   |   | 2 |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   | K |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   |   |   | GT|   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            | K |   |   |   | M | M | M |   |   |   |   |   |   |   |   |
            |   |   | 2 |   |   |   |   |   |   |   |   |   |   |   |   |
        And the board acts
        Then the alien dies
            | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14|
            |   |   |   |   |   |   |   |   |   |   |   | 2 |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   | K |   |
            |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
            |   |   |   | T |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            | K |   |   |   | M | M | M |   |   |   |   |   |   |   |   |
            |   |   | 2 |   |   |   |   |   |   |   |   |   |   |   |   |

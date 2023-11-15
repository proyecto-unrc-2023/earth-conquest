Feature: Alterator purchase

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


    Scenario: the purchased alterator is the Directioner
        When green player sets a Directioner horizontally on the cells (5,1), (5,2) and (5,3)
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
        Then 4 green aliens die

    
    Scenario: the purchased alterator is the Teleporter
        When green player sets a Teleporter on the cell (4,1) for entry door and (6,10) for exit
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
        Then 6 green aliens die


    Scenario: the purchased alterator is the Trap
        When green player sets a Trap on the cell (4, 3)
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
        Then 4 green aliens die
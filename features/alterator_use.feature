Feature: Alterator use

    Background: 
        Given the game has started
        When the game is in the mode Alterator_selection
        Then the player chooses one alterator 

    
    Scenario: the alterator chosen is the Directioner and 1 alien moves to the Directioner's cell
        Given the Directioner is positioned horizontally on the cells (2,2), (2,3) and (2,4)
        And the alien is positioned on the cell (1,2)
            |   | a1|   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   | D | D | D |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
        When the system refreshes
        Then the alien moves to an adjacent cell, this one being cell (2,2)
        And the Directioner acts on the alien
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |a1 | D | D |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 
        When the system refreshes again
        Then the alien moves to the cell (2,3)
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   | D | a1| D |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 
        When the system refreshes again
        Then the alien moves to the cell (2,4)
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   | D | D | a1|   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 
        When the system refreshes again
        Then the alien moves to one of its free adjacent cells, not being the cell (2,3) an option
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   | D | D | D |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   | a1|   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 

    Scenario: the alterator chosen is the Teleporter and an alien moves to the Teleporter's cell
        Given the Teleporter's door is positioned on the cell (2,2)
        And the Teleporter's tail is on the cell (6,5)
        And an alien is positioned on the cell (1,2)
            |   | a1|   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   | D |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   | T |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
        When the system refreshes
        Then the alien moves to an adjacent cell, this one being cell (2,2)
        Then the Teleporter acts on the alien 
        And the alien is teleported to the cell (6,5)
            |   | a1|   |   |    |   |   |   |   |   |   |   |   |   |   |
            |   | D |   |   |    |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |    |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |    |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |    |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |T,a1|   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |    |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |    |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |    |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |    |   |   |   |   |   |   |   |   |   |   |


Scenario: the alterator chosen is the Trap and an alien moves to the Trap's cell
        Given the Trap is positioned on the cell (2,2)
        And the alien is positioned on the cell (1,2)
            |   | a1|   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   | BT|   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
        When the system refreshes
        Then the alien moves to an adjacent cell, this one being cell (2,2)
        Then the Trap acts on the alien
        And the alien dies
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   | BT|   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
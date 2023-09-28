Feature: Alterator use

    Background: 
        Given the game has started
        When the player has a list of alterators to choose from and use
        Then the player chooses one alterator 

    Scenario: the alterator chosen is the Directioner and 1 alien moves to the Directioner's cell
        Given the Directioner is positioned on the cells (2,2), (2,3) and (2,4)
        And the Directioner has the property that lets the alien move in a specific direction for as long as the alterator has power
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
        And the following board is obtained
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
        And the following board is obtained
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
        And the following board is obtained
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


    Scenario: the alterator chosen is the Teleporter and an alien moves to the Teleporter's cell
        Given the Teleporter's door is positioned on the cell (2,2)
        And the Teleporter has the property that it teleports aliens to it's tail.
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
        And the following board is obtained
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


Scenario: the alterator chosen is the Booby Trap and an alien moves to the Trap's cell
        Given the Trap is positioned on the cell (2,2)
        And the Trap has the property that it kills every alien that steps on its cell
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
        Then the Booby Trap acts on the alien
        And the alien dies
        Then the following board is obtained
            |   |   |   |   |   |
            |   |BT |   |   |   |
            |   |   |   |   |   |
            |   |   |   |   |   |
            |   |   |   |   |   |
            |   |   |   |   |   |
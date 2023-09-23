Feature: 3 or 4 aliens on a same cell

Background: 
  Given a new game has started
  And 4 aliens are next to the cell (5,5)

  Scenario: 3 aliens are on the cell (5,5), 2 of them are on the blue team and the other is green team
    Given two blue aliens, in the position (4,5) and (5,4) and one alien from the green team in the position (6,5)
    When they are moved and positioned on the same cell (5,5) <F>
    Then the two aliens from the same team reproduce themselves
    And the product of the reproduction figths with the green alien

 
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   | B |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   | B | F |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   | G |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |


  Scenario: 3 aliens are on the same cell, 2 of them are on the blue team, the other one on the green team and the cell is a modifier or alterator
    Given two blue aliens, in the position (4,5) and (5,4) and one alien from the green team in the position (6,5)
    When they are moved and positioned on the same cell (5,5)
    And  this position is a modifer or alterator
    Then the two aliens from the blue team reproduce themselves
    And the new blue alien, if is alive, figths with the green alien
    And the modifier or alterator acts on the winner of this battle
  

   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   | B |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   | B |FyA|   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   | G |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

  
  Scenario: 3 aliens of the blue team are on the cell (5,5)
    Given 3 aliens on the blue team, in the positions (4,5), (5,4) and (6,5)
    When they are moved and positioned on the same cell (5,5)
    Then the first two aliens reproduce themselves
    And the product of the reproduction, reproduces with the last alien 


 
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   | B |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   | B | R |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   | B |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
  
  
  Scenario: 3 aliens of the same team are on the cell (5,5), this cell is a modifier or alterator
    Given 3 aliens on the blue team, in the positions (4,5), (5,4) and (6,5)
    When they are moved and positioned on the same cell (5,5)
    Then the first two aliens reproduce themselves
    Then the product of the reproduction reproduces with the last alien 
    And the modifier or alterator acts on the new alien

          
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   | B |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   | B |RyA|   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   | B |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
    
    
  Scenario: 4 aliens are on the same cell, 3 are on the blue team, the other is on the green team
    Given 3 aliens on the blue team, in the positions (4,5), (5,4) and (6,5) 
    And one from the other team in the position (5,6)
    When they are moved and positioned on the same cell (5,5)
    Then two aliens from the blue team reproduce themselves
    And the new blue alien, if the number of eyes is less than 5, reproduce with the third alien
    And if the number of eyes of the new alien is less than 5,the product of this reproduction figths with the last alien

    
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   | B |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   | B | F | G |   |   |   |   |   |   |   |   |   |
   |   |   |   |   | B |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
  

  Scenario: 4 aliens are on the same cell, 3 are on the blue team, the other is on the green team and the cell is a modifier or alterator
    Given 3 aliens on the blue team, in the positions (4,5), (5,4) and (6,5) 
    And one from the other team in the position (5,6)
    When they are moved and positioned on the same cell (5,5)
    Then two aliens from the blue team reproduce themselves
    And the new blue alien, if the number of eyes is less than 5, reproduce with the third alien
    And if the number of eyes of the new alien is less than 5,the product of this reproduction figths with the last alien
    And the modifier or alterator acts on the winner of the fight

       
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   | B |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   | B |FyA| G |   |   |   |   |   |   |   |   |   |
   |   |   |   |   | B |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  



  Scenario: 4 aliens are on the same cell, two are on the blue team, two are on the green team
    Given 2 aliens are on blue team in the positions (4,5), (5,4) 
    And the rest on green team, in the positions (6,5), (5,6)
    When they are moved and positioned on the same cell (5,5)
    Then the two blue aliens repoduce themselves
    And the two green aliens repoduce themselves
    And if the number of eyes is less than 5, the product of the two reproductions fight with eachother
   

   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   | B |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   | B | F | G |   |   |   |   |   |   |   |   |   |
   |   |   |   |   | G |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
  

  Scenario: 4 aliens are on the same cell, which is a modifer or alterator, 2 are on blue team, the rest on the green team
    Given 2 aliens are on blue team in the positions (4,5), (5,4) 
    And the rest on green team, in the positions (6,5), (5,6)
    When they are moved and positioned on the same cell (5,5)
    Then the two blue aliens repoduce themselves
    And the two green aliens repoduce themselves
    And if the number of eyes is less than 5, the product of the two reproductions fight with eachother
    And the modifier or alterator acts on the winner of the fight


   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   | B |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   | B |FyA| G |   |   |   |   |   |   |   |   |   |
   |   |   |   |   | G |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |


  Scenario: 4 aliens of the same team are on the same cell
    Given 4 aliens are on blue team in the positions (4,5), (5,4), 6,5), (5,6)
    When they are moved and positioned on the same cell (5,5)
    Then the two blue aliens repoduce themselves
    And the two green aliens repoduce themselves
    And if the number of eyes is less than 5, the product of the two reproductions, reproduce with eachother
   

   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   | B |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   | B | F | B |   |   |   |   |   |   |   |   |   |
   |   |   |   |   | B |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
  

  Scenario: 4 aliens of the same team are on the same cell
    Given 4 aliens are on blue team in the positions (4,5), (5,4), 6,5), (5,6)
    When they are moved and positioned on the same cell (5,5)   

   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   | B |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   | B | F | B |   |   |   |   |   |   |   |   |   |
   |   |   |   |   | B |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
    Then the two blue aliens repoduce themselves
    And the two green aliens repoduce themselves
    And if the number of eyes is less than 5, the product of the two reproductions, reproduce with eachother
    And the modifier or alterator acts on the winner of the fight


   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   |   | B |   |   |   |   |   |   |   |   |   |   |   
   |   |   |   | B |FyA| B |   |   |   |   |   |   |   |   |   |
   |   |   |   |   | B |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
Feature: 3 or 4 aliens on a same cell

Background: 
  Given a new game has started



  Scenario: 3 aliens with one eyes, are on the cell (5,5), 2 of them are on the blue team and the other is green team
    Given two blue aliens and one green alien in the position (5,5) 
    When the cell acts
    Then there is a blue alien left, with one eye
 
      
  
  Scenario: 3 aliens with one eyes, of the blue team, are on the cell (5,5)
    Given 3 aliens on the blue team, in the positions (5,5)
    When the cell acts
    Then there is a blue alien left, with 3 eyes

    
    
  Scenario: 4 aliens with one eyes, are on the same cell, 3 are on the blue team, the other is on the green team
    Given 3 aliens on the blue team and one green alien in the positions (5,5)
    When the cell acts
    Then there is a blue alien left, with 2 eyes



  Scenario: 4 aliens are on the same cell, two are on the blue team, two are on the green team
    Given 2 aliens are on blue team and 2 on green team in the positions (5,5) with 1 eyes
    When the cell acts
    Then there are no aliens left 
   


  Scenario: 4 aliens of the same team are on the same cell
    Given 4 aliens are on blue team in the positions (5,5)
    When the cell acts
    Then there is a blue alien left, with 4 eyes

Feature: 3 or 4 aliens on a same cell

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

  Scenario: 3 aliens with one eye, are on the cell (5,5), 2 of them are on the blue team and the other is on green team
    Given 2 blue aliens and 1 green aliens are in the position (5,5) 
    When the cell acts
    Then there is 1 blue alien left, with 1 eyes
  
  Scenario: 3 aliens with one eye, of the blue team, are on the cell (5,5)
    Given 3 blue aliens and 0 green aliens are in the position (5,5)
    When the cell acts
    Then there is 1 blue alien left, with 3 eyes
    
  Scenario: 4 aliens with one eye, are on the same cell, 3 are on the blue team, the other is on the green team
    Given 3 blue aliens and 1 green aliens are in the position (5,5)
    When the cell acts
    Then there is 1 blue alien left, with 2 eyes

  Scenario: 4 aliens are on the same cell, two are on the blue team, two are on the green team
    Given 2 blue aliens and 2 green aliens are in the position (5,5)
    When the cell acts
    Then there is 0 blue alien left, with 0 eyes

  Scenario: 4 aliens of the same team are on the same cell
    Given 4 blue aliens and 0 green aliens are in the position (5,5)
    When the cell acts
    Then there is 1 blue alien left, with 4 eyes

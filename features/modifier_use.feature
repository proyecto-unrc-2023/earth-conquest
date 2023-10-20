Feature: Modifier use

  Background:
    Given a game has been created
              | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14|
              |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
              |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
              |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
              |   |   |   |   |   |   |   | M |   |   |   |   |   |   |   |
              |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
              |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
              |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
              |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
              |   |   |   |   | M | M | M |   |   |   |   |   |   |   |   |
              |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |


  Scenario Outline: alien on the modifier <modifier>
    Given there is a "<modifier>" on the cell (2, 9)
    And the alien arrives on the cell (2, 9)
    When "<modifier>" activates
    Then "<action_modifier>" and "<result_modifier>"

    Examples:
      | modifier      | action_modifier                       | result_modifier                     	      |
      | multiplier    | generates a clone on the same cell    | there are two identical aliens     	        |
      | killer        | kills the alien                       | there are no aliens left on the cell 	      |



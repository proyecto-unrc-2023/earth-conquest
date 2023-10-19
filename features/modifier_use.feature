Feature: Modifier use

  Background:
    Given the game has started
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
    Given there is a "<modifier>" on the cell (11, 5)
    And the alien arrives on the cell (11, 5)
    When "<modifier>" activates
    Then "<action_modifier>" and "<result_modifier>"

    Examples:
      | modifier      | action_modifier                       | result_modifier                     	      |
      | multiplier    | generates a clone on the same cell    | there are two identical aliens     	        |
      | killer        | kills the alien                       | there are no aliens left on the cell 	      |



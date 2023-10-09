Feature: Modifier use

  Background: Game creation and starting a game
    Given the aliens has been generate in the board

  Scenario Outline: alien on the modifier <modifier>
    Given there is an "<modifier>" in the square (2, 2)
    And alien arrive at the square (2, 2)
    When "<modifier>" activates
    Then "<action_modifier>" and "<result_modifier>"

    Examples:
      | modifier      | action_modifier                     | result_modifier                     	    |
      | multiplier    | generate a clone in the same square | there are two identical aliens     	    |
      | killer        | kill the alien                      | there are no aliens in the square 	    |



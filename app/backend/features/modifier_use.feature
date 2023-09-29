Feature: Modifier use

  Background: Game creation and starting a game
    Given the aliens has been generated
    And there is an aliens in the square (2,2)

  Scenario Outline: alien on the modifier <modifier>
    Given aliens arrive at a '<modifier>'
    When '<modifier>' activates
    Then '<action_modifier>'
    And in the square '<result_modifier>'

    Examples:
      | modifier | action_modifier                     | result_modifier                     	|
      | cloner   | generate a clone in the same square | there are two identical aliens     	|
      | killer   | kill the alien                      | there are no aliens in the square 	|



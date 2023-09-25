 Feature: Game Over

  Background:
    Given a new game has started
    And a base is short-lived

  Scenario: Blue Alien Destroys Green Alien Base
    Given that a one-eyed blue alien from player Juan arrives at the base of green aliens from player Jose
    And the green aliens base has 1 life remaining
    When the blue alien attacks
    Then the base is destroyed
    And blue aliens win
    And a victory message is displayed for player Juan
    And a defeat message is displayed for player Jose







  
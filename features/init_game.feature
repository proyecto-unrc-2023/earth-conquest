Feature: Init Game

Background: flask app is up

	Scenario: Init a party
  	Given a player is in main menu
  	When the player select 'init party'
  	Then a random map is generated
    And alien's bases are colocated on opposite corners
    And the initial crew are generated on the base range

  Scenario: Postion of the modifiers
    Given the game has started
    When a modifier is setted on a cell
    Then it can't be setted another modifier on that cell
  
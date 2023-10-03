Feature: Game initialization

	Background:
		Given that the application was initiated
		And player "Juan" has created a game as blue player
		And player "Jose" has joined the game as green player
		And the game has not started

	Scenario: Initial board creation
        When the game is started
        Then the board dimension is 10 by 15
		And there are 6 "mountains"
		And there are 2 "killers"
		And there are 2 "multipliers"
		And the cells where the modifiers has been setted are occupied
		And the placed modifiers end up positioned outside the teams areas

	Scenario: Launch of the initial crew
		Given the board dimension is 10 by 15
		When the game is started
		Then the game status is set on start mode
		And there are 6 living one-eyed aliens per team
		And the aliens are set on their respective areas

	Scenario: Dimensions of the areas
		When the board dimension is set in 25 by 45
		Then the dimensions of the ovnis ranges should be 11 by 11
		And the range of the "green" ovni should be 10 10
		And the range of the "blue" ovni should be 14 34

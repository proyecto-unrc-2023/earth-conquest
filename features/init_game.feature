Feature: Game initialization

	Background:
		Given a new game has been created
		And player "Juan" has joined the game as "blue" player
		And player "Jose" has joined the game as "green" player
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
		When the board dimension is set in 25 by 45
		And the game is started
		Then the game status is set on start mode
		And there are 6 living one-eyed aliens per team
		And the aliens are set on their respective areas

	Scenario Outline: Dimensions of the areas
		When the board dimension is set in <rows> by <cols>
		Then the dimensions of the ovnis ranges should be <range> by <range>
		And the corner position of the "green" ovni range should be <green_row> <green_col>
		And the corner position of the "blue" ovni range should be <blue_row> <blue_col>

		Examples:
		  | rows | cols | range | green_row | green_col | blue_row | blue_col |
		  |  25  |  45  |   11  |    10     |     10    |     14   |    34    |
		  |  10  |  15  |   4   |    3      |     3     |     6    |    11    |
		  |  4   |  6   |   2   |    1      |     1     |     2    |    4     |


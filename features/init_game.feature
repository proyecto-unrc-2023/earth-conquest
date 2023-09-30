Feature: Game initialization
	Scenario: Initial board creation 
		Given that the application was initiated
		And player Juan has created a game as blue player
		And player Jose has joined the game as green player
		And the game board dimension is 10 by 15
        And two randomly orientated mountains ranges are randomly generated on free positions
		And two killers are randomly generated on free positions
        And two multipliers are randomly generated on free positions
		And the game has not started
		When the game is started
        Then the placed modifiers end up positioned outside of each team's area
        Then six aliens of each team are setted on their respectively areas

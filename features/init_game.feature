Feature: Game initialization
	Scenario: Initial board creation 
		Given that the application was initiated
		And player Juan has created a game as blue player
		And player Jose has joined the game as green player
		And the game board dimension is 10 by 15
		And the game has not started
		When the game is started
		And a vertical mountain obstacle is randomly generated on (4,1)
		And a horizontal mountain obstacle is randomly generated on (4,11)
		Then both players should see the following board
          | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14|
          |GB |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
          |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
          |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
          |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
          |   | M | M | M |   |   |   |   |   |   |   | M |   |   |   |
          |   |   |   |   |   |   |   |   |   |   |   | M |   |   |   |
          |   |   |   |   |   |   |   |   |   |   |   | M |   |   |   |
          |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
          |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
          |   |   |   |   |   |   |   |   |   |   |   |   |   |   | BB|

import { useState } from 'react'
// import { Game } from './components/Game/Game'
import { Menu } from './components/Menu/Menu'
import { gameStatus } from './constants'

function App () {
  const [statusGame, setStatusGame] = useState(null)
  const [gameId, setGameId] = useState(null)
  const [message, setMessage] = useState('')
  const CREATE_GAME = 'http://127.0.0.1:5000/games/create_game'

  const createGame = async () => {
    try {
      const response = await fetch(CREATE_GAME, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        }
      })
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()
      setGameId(data.data.gameId)
      setStatusGame(gameStatus.notStarted)
      setMessage(data.message)
    } catch (error) {
      console.error('Error fetching data:', error)
    }
  }

  return (
    <main>
      {
        statusGame !== gameStatus.started &&
          <Menu createGame={createGame} setStatusGame={setStatusGame} gameId={gameId} message={message} />
      }
      {
        // statusGame === gameStatus.started && */
        // <Game gameId={gameId} />
      }

    </main>
  )
}

export default App

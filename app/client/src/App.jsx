import { useState } from 'react'
import { Game } from './components/Game/Game'
import { Menu } from './components/Menu/Menu'
import { gameStatus } from './constants'

function App () {
  const [statusGame, setStatusGame] = useState(gameStatus.notStarted)
  const [gameId, setGameId] = useState(null)

  const createGame = async () => {
    try {
      console.log('hice click')
      const response = await fetch('')
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()
      setGameId(data.gameId)
      setStatusGame(gameStatus.started)
    } catch (error) {
      console.error('Error fetching data:', error)
    }
  }
  return (
    <>
      {
        statusGame === gameStatus.notStarted &&
          <Menu createGame={createGame} setStatusGame={setStatusGame} />
      }
      {
        statusGame === gameStatus.started &&
          <Game gameId={gameId} />
      }

    </>
  )
}

export default App

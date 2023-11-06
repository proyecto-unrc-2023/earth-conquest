import { useState } from 'react'
import { Game } from './components/Game/Game'
import { Menu } from './components/Menu/Menu'
import { gameStatus } from './constants'

function App () {
  const [board, setBoard] = useState(null)
  const [statusGame, setStatusGame] = useState(gameStatus.NOT_STARTED)
  const [gameId, setGameId] = useState(null)
  const [message, setMessage] = useState('')
  const [host, setHost] = useState(null)
  const [greenOvniRange, setGreenOvniRange] = useState(null)
  const [blueOvniRange, setBlueOvniRange] = useState(null)

  const CREATE_GAME = 'http://127.0.0.1:5000/games/'
  const START_GAME = 'http://127.0.0.1:5000/games/start_game'
  const GET_GAME = 'http://127.0.0.1:5000/games'

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
      console.log('CREATE GAME:', data)
      setHost(true)
      setMessage(data.message)
      setGameId(data.data.gameId)
      setGreenOvniRange(data.data.game.board.green_ovni_range)
      setBlueOvniRange(data.data.game.board.blue_ovni_range)
    } catch (error) {
      console.error('Error fetching data:', error)
    }
  }

  const startGame = async (gameId) => {
    try {
      const response = await fetch(`${START_GAME}/${gameId}`, {
        method: 'PUT'
      })
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()
      console.log('START GAME:', data)
      setStatusGame(gameStatus.STARTED)
    } catch (error) {
      console.error('Error fetching data: ', error)
    }
  }

  const getGame = async (gameId) => {
    try {
      const response = await fetch(`${GET_GAME}/${gameId}`)
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()
      console.log('GET BOARD:', data)
    } catch (error) {
      console.error('Error spawn aliens in base:', error)
    }
  }

  window.addEventListener('storage', function (event) {
    if (event.key === 'guestPlayer') {
      getGame(gameId)
    }
  })

  return (
    <main>
      {
        statusGame !== gameStatus.STARTED &&
          <Menu
            createGame={createGame}
            getGame={getGame}
            setGameId={setGameId}
            startGame={startGame}
            setHost={setHost}
            gameId={gameId}
            message={message}
          />
      }
      {
        statusGame === gameStatus.STARTED &&
          <Game
            gameId={gameId}
            setStatusGame={setStatusGame}
            greenOvniRange={greenOvniRange}
            blueOvniRange={blueOvniRange}
            startGame={startGame}
            board={board}
            host={host}
            setBoard={setBoard}
          />
      }

    </main>
  )
}

export default App

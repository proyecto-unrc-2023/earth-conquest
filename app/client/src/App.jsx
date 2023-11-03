import { useState } from 'react'
import { Game } from './components/Game/Game'
import { Menu } from './components/Menu/Menu'
import { gameStatus } from './constants'

function App () {
  const [board, setBoard] = useState(null)
  const [statusGame, setStatusGame] = useState(null)
  const [gameId, setGameId] = useState(null)
  const [message, setMessage] = useState('')
  const [host, setHost] = useState(null)
  const CREATE_GAME = 'http://127.0.0.1:5000/games/'
  const START_GAME = 'http://127.0.0.1:5000/games/start_game'
  const GET_GAME = 'http://127.0.0.1:5000/games/'

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
      setGameId(data.data.gameId)
      // setStatusGame(gameStatus.notStarted)
      setMessage(data.message)
      // setBoard(data.data.game.board)
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
      // if (data.success) {
      //   setStatusGame(gameStatus.started)
      //   // setBoard(data.data.game.board)
      // }
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
      setBoard(data.data.game.board.board)
      setStatusGame(gameStatus.started)
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
        statusGame !== gameStatus.started &&
          <Menu createGame={createGame} getGame={getGame} startGame={startGame} setGameId={setGameId} setHost={setHost} gameId={gameId} message={message} />
      }
      {
        statusGame === gameStatus.started &&
          <Game gameId={gameId} getGame={getGame} board={board} host={host} setBoard={setBoard} />
      }

    </main>
  )
}

export default App

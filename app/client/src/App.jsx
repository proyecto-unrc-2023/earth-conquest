import { useState, useEffect, useRef } from 'react'
import { Game } from './components/Game/Game'
import { Menu } from './components/Menu/Menu'
import { gameStatus } from './constants'

function App () {
  const [board, setBoard] = useState(null)
  const [statusGame, setStatusGame] = useState(null)
  const [gameId, setGameId] = useState(null)
  const [message, setMessage] = useState('')
  const [host, setHost] = useState(null)
  const [greenOvniRange, setGreenOvniRange] = useState(null)
  const [blueOvniRange, setBlueOvniRange] = useState(null)

  const [playerGreen, setPlayerGreen] = useState(null)
  const [playerBlue, setPlayerBlue] = useState(null)
  const gameIdRef = useRef(null)

  const CREATE_GAME = 'http://127.0.0.1:5000/games/'
  const START_GAME = 'http://127.0.0.1:5000/games/start_game'
  const GET_GAME = 'http://127.0.0.1:5000/games/'

  /*
    'CREATE GAME:'
 data:

  {
    success: true,
    message: 'Game created successfully',
    data: {
      gameId: 6,
      game: {
        status: 'NOT_STARTED',
        green_player: null,
        blue_player: null,
        board: {
          blue_ovni_range: [ 6, 11 ],
          green_ovni_range: [ 3, 3 ],
          base_range_dimentions: 4,
          board: Array(10) [
            Array(15) [
              { aliens: [], modifier: null, alterator: null },
  */

  useEffect(() => {
    if (gameId) {
      const sse = new EventSource(`http://localhost:5000/games/sse/${gameId}`)
      console.log('SSE ACTIVO')
      sse.onmessage = e => {
        const data = JSON.parse(e.data)
        setStatusGame(data.status)
        if (data.status !== gameStatus.STARTED) {
          console.log(data)
          setBoard(data.board.board)
          setGreenOvniRange(data.board.green_ovni_range)
          setBlueOvniRange(data.board.blue_ovni_range)
          setPlayerGreen(data.green_player)
          setPlayerBlue(data.blue_player)
          console.log('PLAYER BLUE: ', playerBlue)
          console.log('PLAYER GREEN: ', playerGreen)
          if (playerBlue && playerGreen) {
            console.log('STARTEO DESDE SSE')
            if (!host) startGame(gameId)
          }
        }
      }

      sse.onerror = () => {
      // error log here
        sse.close()
      }

      return () => {
        sse.close()
      }
    } else {
      console.log('Entre al else del sse')
      gameIdRef.current = gameId
    }
  }, [playerBlue, playerGreen])

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
    } catch (error) {
      console.error('Error fetching data:', error)
    }
  }

  const startGame = async (currentGameId) => {
    try {
      const response = await fetch(`${START_GAME}/${currentGameId}`, {
        method: 'PUT'
      })
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()
      console.log('START GAME:', data)
    } catch (error) {
      console.error('Error fetching data: ', error)
    }
  }

  const getGame = async (currentGameId) => {
    try {
      const response = await fetch(`${GET_GAME}/${currentGameId}`)
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()
      console.log('GET BOARD:', data)
    } catch (error) {
      console.error('Error get game:', error)
    }
  }

  // window.addEventListener('storage', function (event) {
  //   if (event.key === 'guestPlayer') {
  //     startGame(gameId)
  //   }
  // })

  return (
    <main>
      {
        statusGame !== gameStatus.STARTED &&
          <Menu
            createGame={createGame}
            setGameId={setGameId}
            gameId={gameId}
            startGame={startGame}
            setPlayerGreen={setPlayerGreen}
            setPlayerBlue={setPlayerBlue}
            setHost={setHost}
            message={message}
          />
      }
      {
        statusGame === gameStatus.STARTED &&
          <Game
            gameId={gameId}
            setStatusGame={setStatusGame}
            playerGreen={playerGreen}
            playerBlue={playerBlue}
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

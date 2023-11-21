import { useState, useEffect } from 'react'
import { Game } from './components/Game/Game'
import { Menu } from './components/Menu/Menu'
import { gameStatus } from './constants'
import { startGame } from './services/appService'

function App () {
  const [game, setGame] = useState({
    gameId: null,
    board: null,
    cleanBoard: null,
    statusGame: null,
    host: null,
    playerBlue: null,
    playerGreen: null,
    teamPlayer: null,
    greenOvniRange: null,
    blueOvniRange: null,
    blueOvniLife: null,
    greenOvniLife: null,
    aliveGreenAliens: null,
    aliveBlueAliens: null
  })
  const [originalBoard, setOriginalBoard] = useState(null)

  useEffect(() => {
    let sse

    const handleGameUpdate = (data) => {
      setGame((prevState) => ({
        ...prevState,
        statusGame: data.status
      }))
      setOriginalBoard(data.board.grid)

      if (data.status !== gameStatus.STARTED) {
        setGame((prevState) => ({
          ...prevState,
          board: data.board.grid,
          cleanBoard: data.board.grid,
          greenOvniRange: data.board.green_ovni_range,
          blueOvniRange: data.board.blue_ovni_range,
          playerBlue: data.blue_player,
          playerGreen: data.green_player
        }))
        if (game.playerBlue && game.playerGreen) {
          console.log('STARTEO DESDE SSE')
          if (!game.host) startGame(game.gameId)
          setGame((prevState) => ({
            ...prevState,
            statusGame: gameStatus.STARTED
          }))
          sse.close()
        }
      }
    }

    const startSEE = () => {
      sse = new window.EventSource(`http://localhost:5000/games/sse/${game.gameId}`)
      console.log('SSE ACTIVO')
      sse.onmessage = e => {
        const data = JSON.parse(e.data)
        handleGameUpdate(data)
      }

      sse.onerror = () => {
        // error log here
        sse.close()
      }
    }

    if (game.gameId) {
      startSEE()
    } else {
      console.log('Entre al else del sse')
    }

    return () => {
      console.log('SE CERRO SSE DE APP CON RETURN')
      if (sse) {
        sse.close()
      }
    }
  }, [game.playerBlue, game.playerGreen])

  return (
    <main>
      {
        game.statusGame !== gameStatus.STARTED &&
          <Menu
            game={game}
            setGame={setGame}
          />
      }
      {
        game.statusGame === gameStatus.STARTED &&
          <Game
            game={game}
            setGame={setGame}
            startGame={startGame}
            originalBoard={originalBoard}
          />
      }

    </main>
  )
}

export default App

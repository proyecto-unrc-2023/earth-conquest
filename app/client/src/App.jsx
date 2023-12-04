import { useState, useEffect } from 'react'
import { Game } from './components/Game/Game'
import { Menu } from './components/Menu/Menu'
import { gameStatus } from './constants'
import { startGame, API } from './services/appService'
import { GameOver } from './components/GameOver/GameOver'

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
    aliveBlueAliens: null,
    winner: null
  })
  const [originalBoard, setOriginalBoard] = useState(null)

  /*
    Funcion que reproduce sonidos pasando la ruta como parametro
  */
  const playSound = (sound) => {
    // eslint-disable-next-line no-undef
    const audio = new Audio(sound)
    audio.play()
    return audio
  }

  useEffect(() => {
    let sse
    // actualiza atributos de game
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
      sse = new window.EventSource(API + `games/sse/${game.gameId}`)
      sse.onmessage = e => {
        const data = JSON.parse(e.data)
        handleGameUpdate(data)
      }

      sse.onerror = () => {
        sse.close()
      }
    }

    if (game.gameId) {
      startSEE()
    }

    return () => {
      if (sse) {
        sse.close()
      }
    }
  }, [game.playerBlue, game.playerGreen])

  return (
    <main>
      {
        (game.statusGame === gameStatus.NOT_STARTED || game.statusGame === null) &&
          <Menu
            game={game}
            setGame={setGame}
            playSound={playSound}
          />
      }
      {
        game.statusGame === gameStatus.STARTED &&
          <Game
            game={game}
            setGame={setGame}
            startGame={startGame}
            playSound={playSound}
            originalBoard={originalBoard}
          />
      }
      {game.statusGame === gameStatus.OVER &&
        <GameOver
          game={game}
        />}

    </main>
  )
}

export default App

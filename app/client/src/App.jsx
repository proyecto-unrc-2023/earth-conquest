import { useState, useEffect } from 'react'
import { Game } from './components/Game/Game'
import { Menu } from './components/Menu/Menu'
import { gameStatus } from './constants'
import { startGame } from './services/appService'

function App () {
  const [game, setGame] = useState({
    gameId: null,
    board: null,
    statusGame: gameStatus.NOT_STARTED,
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
  /*
  setGame((prevState) => ({
    ...prevState,
    board: nuevoValorDeLaTabla,
  }))
  */

  /*
  const hash = {
    '(6, 14)': {
      aliens: [],
      modifier: null,
      alterator: null
    },
    '(6, 13)': {
      aliens: [
        {
          id: 38,
          eyes: 1,
          team: 'BLUE'
        }
      ],
      modifier: null,
      alterator: null
    }
  }
  */
  /*
  const actualizarBoardConHash = (nuevoHash) => {
    const newBoard = [...game.board]
    for (const position in nuevoHash) {
      if (nuevoHash.hasOwnProperty(position)) {
        const [row, col] = position
          .slice(1, -1)
          .split(', ')
          .map(coord => Number(coord))

        // Actualizar la matriz board con los datos de la celda correspondiente.
        newBoard[row][col] = nuevoHash[position]
      }
    }
  }
  */

  useEffect(() => {
    if (game.gameId) {
      // eslint-disable-next-line no-undef
      const sse = new EventSource(`http://localhost:5000/games/sse/${game.gameId}`)
      console.log('SSE ACTIVO')

      sse.onmessage = e => {
        const data = JSON.parse(e.data)
        setGame((prevState) => ({
          ...prevState,
          statusGame: data.status
        }))
        if (data.status !== gameStatus.STARTED) {
          console.log(data)
          setGame((prevState) => ({
            ...prevState,
            greenOvniRange: data.board.green_ovni_range,
            blue_ovni_range: data.board.blue_ovni_range,
            playerBlue: data.blue_player,
            playerGreen: data.green_player
          }))
          actualizarBoardConHash(data.board.cells)
          if (game.playerBlue && game.playerGreen) {
            console.log('STARTEO DESDE SSE')
            if (!game.host) startGame(game.gameId)
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
            />
        }

    </main>
  )
}

export default App

import { useState, useEffect } from 'react'
import { Board } from '../Board/Board'
import { Panel } from '../Panel/Panel'
import { StatsGame } from '../StatGame/StatsGame'
import { nextState } from '../../services/appService'
import { handleHash, handleAliens, getAliensDirections } from '../../services/alienService'
import './Game.css'

export function Game ({ game, setGame, originalBoard }) {
  const [alter, setAlterator] = useState(null)
  const [teleporterEnabled, setTeleporterEnabled] = useState(true)
  const [teleportIn, setTeleportIn] = useState([{ row: null, col: null }])
  const [teleportOut, setTeleportOut] = useState([{ row: null, col: null }])
  const [aliensDirections, setAliensDirections] = useState([])
  const [aliensPosition, setAliensPosition] = useState([])
  useEffect(() => {
    let sse
    const handleGameUpdate = (data) => {
      setGame((prevState) => ({
        ...prevState,
        board: handleHash(data.board.cells, originalBoard, setTeleportIn, setTeleportOut),
        setStatusGame: data.status,
        blueOvniLife: data.board.blue_ovni_life,
        greenOvniLife: data.board.green_ovni_life,
        aliveGreenAliens: data.alive_green_aliens,
        aliveBlueAliens: data.alive_blue_aliens
      }))
    }

    const moveAliens = (cells) => {
      const newAliensPosition = handleAliens(aliensPosition, cells)
      setAliensPosition(newAliensPosition)
      console.log('NEW ALIENS POSITION: ', aliensPosition)
      const newAliensDirections = getAliensDirections(newAliensPosition)
      setAliensDirections(newAliensDirections)
    }

    const startSSE = () => {
      // eslint-disable-next-line no-undef
      sse = new EventSource(`http://localhost:5000/games/sse/${game.gameId}`)
      sse.onmessage = (e) => {
        const data = JSON.parse(e.data)
        moveAliens(data.board.cells) // lo hace en el refresh y el act aca, necesito una bandera para que solo lo haga en el refresh
        handleGameUpdate(data)
      }

      sse.onerror = (e) => {
        console.error('Error en el sse de game', e)
        sse.close()
      }
    }

    startSSE()

    return () => {
      if (sse) {
        sse.close()
      }
    }
  }, [])

  async function countdown () {
    if (game.host) {
      console.log('HAGO NEXT STATE')
      await nextState(game.gameId)
      setTimeout(countdown, 3000)
    }
  }

  return (
    <>
      <Board
        game={game}
        teleportIn={teleportIn}
        teleportOut={teleportOut}
        newAlterator={alter}
        setAlter={setAlterator}
        setTeleporterEnabled={setTeleporterEnabled}
        teleporterEnabled={teleporterEnabled}
        aliensDirections={aliensDirections}
      />
      <section className='statsGame'>
        <StatsGame team='green' lifeOvni={game.greenOvniLife} liveAliens={game.aliveGreenAliens} playerName={game.playerGreen} />
        <StatsGame team='blue' lifeOvni={game.blueOvniLife} liveAliens={game.aliveBlueAliens} playerName={game.playerBlue} />
      </section>
      <button onClick={() => countdown()}>PLAY</button>
      <Panel setAlter={setAlterator} teleporterEnabled={teleporterEnabled} />
    </>
  )
}

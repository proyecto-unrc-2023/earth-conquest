import { useState, useEffect } from 'react'
import { Board } from '../Board/Board'
import { Panel } from '../Panel/Panel'
import { StatsGame } from '../StatGame/StatsGame'
import { nextState } from '../../services/appService'
import { handleHash } from '../../services/alienService'
import './Game.css'

export function Game ({ game, setGame, originalBoard }) {
  const [alter, setAlterator] = useState(null)
  const [aliens, setAliens] = useState([])
  const [teleporterEnabled, setTeleporterEnabled] = useState(true)

  useEffect(() => {
    // eslint-disable-next-line no-undef
    const sse = new EventSource(`http://localhost:5000/games/sse/${game.gameId}`)
    sse.onmessage = e => {
      const data = JSON.parse(e.data)
      console.log('ACA VIENE EN EL SSE', 'HOST: ', game.host, 'DATA: ', data)
      // actualizar board con hash
      console.log('SSE ACTIVO BOARD', originalBoard)
      setGame((prevState) => ({
        ...prevState,
        board: handleHash(aliens, data.board.cells, originalBoard),
        setStatusGame: data.status,
        blueOvniLife: data.board.blue_ovni_life,
        greenOvniLife: data.board.green_ovni_life,
        aliveGreenAliens: data.alive_green_aliens,
        aliveBlueAliens: data.alive_blue_aliens
      }))
    }

    sse.onerror = (e) => {
      console.error('Error en el sse de game', e)
      sse.close()
    }

    return () => {
      console.log('SE CERRO SSE DE GAME')
      // sse.close()
    }
  }, [])

  useEffect(() => {
    if (game.host) {
      const timeoutId = setTimeout(() => {
        nextState(game.gameId)
        console.log('HICE EL NEXT STATE')
      }, 5000)
      return () => {
        clearTimeout(timeoutId)
      }
    }
  }, [game.board])

  return (
    <>
      <Board
        game={game}
        newAlterator={alter}
        setAlter={setAlterator}
        setTeleporterEnabled={setTeleporterEnabled}
        teleporterEnabled={teleporterEnabled}
      />
      <section className='statsGame'>
        <StatsGame team='green' lifeOvni={game.greenOvniLife} liveAliens={game.aliveGreenAliens} playerName={game.playerGreen} />
        <StatsGame team='blue' lifeOvni={game.blueOvniLife} liveAliens={game.aliveBlueAliens} playerName={game.playerBlue} />
      </section>
      <Panel setAlter={setAlterator} teleporterEnabled={teleporterEnabled} />
    </>
  )
}

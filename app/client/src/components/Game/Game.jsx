import { useState, useEffect } from 'react'
import { Board } from '../Board/Board'
import { Panel } from '../Panel/Panel'
import { StatsGame } from '../StatGame/StatsGame'
import { refresh, act, spawnAliens } from '../../services/appService'
import './Game.css'

export function Game ({ game, setGame, startGame }) {
  const [alter, setAlterator] = useState(null)
  const [teleporterEnabled, setTeleporterEnabled] = useState(true)
  const [changeTic, setChangeTic] = useState(true)
  const [tic, setTic] = useState(0)

  useEffect(() => {
    // eslint-disable-next-line no-undef
    const sse = new EventSource(`http://localhost:5000/games/sse/${gameId}`)

    sse.onmessage = e => {
      const data = JSON.parse(e.data)
      console.log(data)
      setGame((prevState) => ({
        ...prevState,
        setStatusGame: data.status,
        board: data.board.board,
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
      console.log('SE CERRO SSE')
      sse.close()
    }
  }, [])

  useEffect(() => {
    if (game.host) {
      const timeoutId = setTimeout(() => {
        refresh()
        act()
        spawnAliens()
      }, 1000)
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

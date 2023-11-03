import { useState, useEffect } from 'react'
import { Board } from '../Board/Board'
import { Panel } from '../Panel/Panel'
import { StatsGame } from '../StatGame/StatsGame'
import './Game.css'

export function Game ({ gameId, board, host, setBoard, getGame }) {
  const [alter, setAlterator] = useState(null)
  const [teleporterEnabled, setTeleporterEnabled] = useState(true)
  const [changeTic, setChangeTic] = useState(true)
  const [tic, setTic] = useState(0)
  const [winner, setWinner] = useState(null)
  const NOMBRE_G = 'Nombre_player_green'
  const NOMBRE_B = 'Nombre_player_blue'

  const REFRESH = 'http://127.0.0.1:5000/games/refresh_board'
  const ACT = 'http://127.0.0.1:5000/games/act_board'
  const SPAWN_ALIENS = 'http://127.0.0.1:5000/games/spawn_aliens'

  // vida de las bases
  let lifeGreenOvni
  let lifeBlueOvni

  // cantidad de aliens vivos
  let liveBlueAliens
  let liveGreenAliens

  const refresh = async (gameId) => {
    setTic(tic + 1)
    try {
      const response = await fetch(`${REFRESH}/${gameId}`, {
        method: 'PUT'
      })
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json() // esto no haría falta pq no hace nada, solo manda a refrescar a la api
      console.log('REFRESH: ', data)
    } catch (error) {
      console.error('Error fetching data in refresh:', error)
    }
  }

  const act = async (gameId) => {
    try {
      const response = await fetch(`${ACT}/${gameId}`, {
        method: 'PUT'
      })
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()
      console.log('ACTUUUAAAAA: ', data)
      /*
      ESTO IRIA EN EL ONMESSAGE
      setBoard(data.board)
      lifeGreenOvni = data.green_ovni_life
      lifeBlueOvni = data.blue_ovni_life
      liveBlueAliens = data.live_blue_aliens
      liveGreenAliens = data.live_green_aliens
      if (data.winner) {
        setWinner(data.winner.team)
        // aca habría que hacer el game over
      }
      */
    } catch (error) {
      console.error('Error fetching data in act:', error)
    }
  }

  const spawnAliens = async (gameId) => {
    try {
      const response = await fetch(`${SPAWN_ALIENS}/${gameId}`, {
        method: 'PUT'
      })
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json() // esto tampoco haría falta
      console.log('SPAWN ALIENS:', data)
    } catch (error) {
      console.error('Error spawn aliens in base:', error)
    }
  }

  useEffect(() => {
    const timeoutId = setTimeout(() => {
      if (host) {
        if (changeTic) {
          refresh(gameId)
        } else {
          act(gameId)
          if (tic === 2) {
            spawnAliens(gameId)
            setTic(0)
          }
        }
      }
      getGame(gameId)
      setChangeTic(!changeTic)
    }, 3000)
    return () => clearTimeout(timeoutId)
  }, [board])

  const setAlter = (newAlterator) => {
    setAlterator(newAlterator)
  }

  return (
    <>

      <Board board={board} setBoard={setBoard} newAlterator={alter} setAlter={setAlter} setTeleporterEnabled={setTeleporterEnabled} teleporterEnabled={teleporterEnabled} gameId={gameId} />

      <section className='statsGame'>
        <StatsGame team='green' lifeOvni={lifeGreenOvni} liveAliens={liveGreenAliens} greenName={NOMBRE_G} />
        <StatsGame team='blue' lifeOvni={lifeBlueOvni} liveAliens={liveBlueAliens} blueName={NOMBRE_B} />
      </section>
      <Panel setAlter={setAlter} teleporterEnabled={teleporterEnabled} />

    </>
  )
}

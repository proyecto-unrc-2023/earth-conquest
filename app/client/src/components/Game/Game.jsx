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
  // const [winner, setWinner] = useState(null)

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

  // eslint-disable-next-line no-undef
  const source = new EventSource(`http://localhost:5000/games/sse/${gameId}`)

  const refresh = async (gameId) => {
    setTic(tic + 1)
    try {
      const response = await fetch(`${REFRESH}/${gameId}`, {
        method: 'PUT'
      })
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      // esto se deberia mover a useEffect
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
      // if (data.winner) {
      // setWinner(data.winner.team)
      // aca habría que hacer el game over
      // }
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
    } catch (error) {
      console.error('Error spawn aliens in base:', error)
    }
  }

  useEffect(() => {
    const timeoutId = setTimeout(() => {
      if (host) {
        if (changeTic) {
          if (tic === 2) {
            spawnAliens(gameId)
            setTic(0)
          } else {
            refresh(gameId)
          }
        } else {
          act(gameId)
        }
        source.onmessage = function (event) {
          const data = JSON.parse(event.data)
          setBoard(data)
          /*
          lifeGreenOvni = data.green_ovni_life
          lifeBlueOvni = data.blue_ovni_life
          liveBlueAliens = data.live_blue_aliens
          liveGreenAliens = data.live_green_aliens
          */
        }
        source.onerror = function (event) {
          console.error('Error en la conexión SSE:', event)
        }
      }
      getGame(gameId)
      console.log('Aca esta el board de host:', host, '\n', board)
      setChangeTic(!changeTic)
    }, 10000)
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
      <img src='../public/panel_left.jpg' className='panel_left' />
      <img src='../public/panel_right.jpg' className='panel_right' />

    </>
  )
}

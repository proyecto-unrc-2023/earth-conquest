import { useState, useEffect } from 'react'
import { Board } from '../Board/Board'
import { Panel } from '../Panel/Panel'
import { StatsGame } from '../StatGame/StatsGame'
import { gameStatus } from '../../constants'
import './Game.css'

export function Game ({ gameId, playerBlue, playerGreen, setStatusGame, board, host, setBoard, greenOvniRange, blueOvniRange }) {
  const [alter, setAlterator] = useState(null)
  const [blueOvniLife, setBlueOvniLife] = useState(null)
  const [greenOvniLife, setGreenOvniLife] = useState(null)
  const [aliveGreenAliens, setAliveGreenAliens] = useState(null)
  const [aliveBlueAliens, setAliveBlueAliens] = useState(null)
  const [teleporterEnabled, setTeleporterEnabled] = useState(true)
  const [changeTic, setChangeTic] = useState(true)
  const [tic, setTic] = useState(0)

  const REFRESH = 'http://127.0.0.1:5000/games/refresh_board'
  const ACT = 'http://127.0.0.1:5000/games/act_board'
  const SPAWN_ALIENS = 'http://127.0.0.1:5000/games/spawn_aliens'

  const refresh = async (gameId) => {
    try {
      const response = await fetch(`${REFRESH}/${gameId}`, {
        method: 'PUT'
      })
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
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
    const sse = new EventSource(`http://localhost:5000/games/sse/${gameId}`)

    sse.onmessage = e => {
      const data = JSON.parse(e.data)
      console.log(data)
      setStatusGame(data.status)
      setBoard(data.board.board)
      setBlueOvniLife(data.board.green_ovni_life)
      setGreenOvniLife(data.board.blue_ovni_life)
      setAliveGreenAliens(data.alive_green_aliens)
      setAliveBlueAliens(data.alive_blue_aliens)
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
    if (host) {
      const timeoutId = setTimeout(() => {
        if (changeTic) {
          refresh(gameId)
        } else {
          act(gameId)
        }
      }, 1000)
      setChangeTic(!changeTic)
      return () => {
        clearTimeout(timeoutId)
      }
    }
  }, [board])

  return (
    <>
      <Board board={board} greenOvniRange={greenOvniRange} blueOvniRange={blueOvniRange} setBoard={setBoard} newAlterator={alter} setAlter={setAlterator} setTeleporterEnabled={setTeleporterEnabled} teleporterEnabled={teleporterEnabled} gameId={gameId} />

      <section className='statsGame'>
        <StatsGame team='green' lifeOvni={greenOvniLife} liveAliens={aliveGreenAliens} playerName={playerGreen} />
        <StatsGame team='blue' lifeOvni={blueOvniLife} liveAliens={aliveBlueAliens} playerName={playerBlue} />
      </section>
      <Panel setAlter={setAlterator} teleporterEnabled={teleporterEnabled} />
      <img src='../public/panel_left.jpg' className='panel_left' />
      <img src='../public/panel_right.jpg' className='panel_right' />
    </>
  )
}

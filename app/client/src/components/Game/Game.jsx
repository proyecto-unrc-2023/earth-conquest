import { useState, useEffect, useCallback } from 'react'
import { Board } from '../Board/Board'
import { Panel } from '../Panel/Panel'
import { StatsGame } from '../StatGame/StatsGame'
import './Game.css'

export function Game ({ gameId, board, host, setBoard, getGame}) {
  const [alter, setAlterator] = useState(null)
  const [teleporterEnabled, setTeleporterEnabled] = useState(true)
  const [changeTic, setChangeTic] = useState(true)
  const [tic, setTic] = useState(0)

  const NOMBRE_G = 'Nombre_player_green'
  const NOMBRE_B = 'Nombre_player_blue'

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
      const parsedData = JSON.parse(e.data)
      setBoard(parsedData.board.board)
    }
  
    sse.onerror = () => {
      // error log here
      sse.close();
    }
  
    return () => {
      sse.close();
    }
    
  }, [])
  
  useEffect(() => {
    if (host) {
      if (changeTic) {
        refresh(gameId)
      } else {
        act(gameId)
      }
      setChangeTic(prevChangeTic => !prevChangeTic)
    }
  }, [board])

  return (
    <>
      <Board board={board} setBoard={setBoard} newAlterator={alter} setAlter={setAlterator} setTeleporterEnabled={setTeleporterEnabled} teleporterEnabled={teleporterEnabled} gameId={gameId} />

      <section className='statsGame'>
        <StatsGame team='green' lifeOvni={0} liveAliens={0} greenName={NOMBRE_G} />
        <StatsGame team='blue' lifeOvni={0} liveAliens={0} blueName={NOMBRE_B} />
      </section>
      <Panel setAlter={setAlterator} teleporterEnabled={teleporterEnabled} />
      <img src='../public/panel_left.jpg' className='panel_left' />
      <img src='../public/panel_right.jpg' className='panel_right' />
    </>
  )
}

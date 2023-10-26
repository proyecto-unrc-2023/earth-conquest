import { useState, useEffect } from 'react'
import data2 from '../../data2.json'
import { Board } from '../Board/Board'
import { Panel } from '../Panel/Panel'
import { StatsGame } from '../StatGame/StatsGame'
import './Game.css'

export function Game ({ gameId }) {
  const [alter, setAlterator] = useState(null)
  const [teleporterEnabled, setTeleporterEnabled] = useState(true)
  const [board, setBoard] = useState(data2.grid)
  const [changeTic, setChangeTic] = useState(true)
  const [winner, setWinner] = useState(null)

  let CONT_TICS = 0
  const REFRESH = 'http://127.0.0.1:5000/games/refresh_board'
  const ACT = 'http://127.0.0.1:5000/games/act_board'
  const SPAWN_ALIENS = 'http://127.0.0.1:5000/games//spawn_aliens/'

  // vida de las bases
  let lifeGreenOvni
  let lifeBlueOvni

  // cantidad de aliens vivos
  let liveBlueAliens
  let liveGreenAliens

  const refresh = async () => {
    try {
      const response = await fetch(`${REFRESH}/${gameId}`)
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()

      CONT_TICS = CONT_TICS + 1
      if (CONT_TICS === 5) {
        spawnAliens()
        CONT_TICS = 0
      } else {
        setBoard(data.board)
      }
    } catch (error) {
      console.error('Error fetching data in refresh:', error)
    }
  }

  const act = async () => {
    try {
      const response = await fetch(`${ACT}/${gameId}`)
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()

      setBoard(data.board)
      lifeGreenOvni = data.green_ovni_life
      lifeBlueOvni = data.blue_ovni_life
      liveBlueAliens = data.live_blue_aliens
      liveGreenAliens = data.live_green_aliens

      if (lifeGreenOvni === 0) {
        setWinner('Green')
      } else {
        setWinner('Blue')
      }
    } catch (error) {
      console.error('Error fetching data in act:', error)
    }
  }

  const spawnAliens = async () => {
    try {
      const response = await fetch(`${SPAWN_ALIENS}/${gameId}`)
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()
      setBoard(data.board)
    } catch (error) {
      console.error('Error spawn aliens in base:', error)
    }
  }

  useEffect(() => {
    const timeoutId = setTimeout(() => {
      if (changeTic) {
        refresh()
      } else {
        act()
      }
      setChangeTic(!changeTic)
    }, 1000)
    return () => clearTimeout(timeoutId)
  }, [board])

  const setAlter = (newAlterator) => {
    setAlterator(newAlterator)
  }

  return (
    <>
      <h1>Earth conquest</h1>
      <Board board={board} setBoard={setBoard} newAlterator={alter} setAlter={setAlter} setTeleporterEnabled={setTeleporterEnabled} teleporterEnabled={teleporterEnabled} gameId={gameId} />
      <section className='statsGame'>
        <StatsGame team='green' lifeOvni={lifeGreenOvni} liveAliens={liveGreenAliens} />
        <StatsGame team='blue' lifeOvni={lifeBlueOvni} liveAliens={liveBlueAliens} />
      </section>
      <Panel setAlter={setAlter} teleporterEnabled={teleporterEnabled} />
    </>
  )
}

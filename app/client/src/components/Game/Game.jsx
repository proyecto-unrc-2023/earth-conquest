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

  // vida de las bases
  let lifeGreenOvni
  let lifeBlueOvni

  // cantidad de aliens vivos
  let liveBlueAliens
  let liveGreenAliens

  const refresh = async () => {
    try {
      const response = await fetch(`/game/${gameId}`)
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()

      setBoard(data.board)
    } catch (error) {
      console.error('Error fetching data in refresh:', error)
    }
  }

  const act = async () => {
    try {
      const response = await fetch('ruta para el act')
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()

      setBoard(data.board)
      lifeGreenOvni = data.green_ovni_life
      lifeBlueOvni = data.blue_ovni_life
      liveBlueAliens = data.live_blue_aliens
      liveGreenAliens = data.live_green_aliens
    } catch (error) {
      console.error('Error fetching data in act:', error)
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

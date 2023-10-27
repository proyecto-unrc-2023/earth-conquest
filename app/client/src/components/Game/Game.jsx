import { useState /*, useEffect */ } from 'react'
import data2 from '../../data2.json'
import { Board } from '../Board/Board'
import { Panel } from '../Panel/Panel'
import { StatsGame } from '../StatGame/StatsGame'
import './Game.css'

export function Game ({ gameId }) {
  const [alter, setAlterator] = useState(null)
  const [permisoTeleport, setPermisoTeleport] = useState(true)
  const [board, setBoard] = useState(data2.grid)

  const NOMBRE_G = 'Nombre_player_green'
  const NOMBRE_B = 'Nombre_player_blue'
  // pide el refresco
  /*
  const fetchData = async () => {
    try {
      const response = await fetch(`/game/${gameId}`)
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()

      setBoard(data.board)
    } catch (error) {
      console.error('Error fetching data:', error)
    }
  }

  useEffect(() => {
    const timeoutId = setTimeout(() => {
      fetchData()
    }, 1000)
    return () => clearTimeout(timeoutId)
  }, [board])
  */
  const setAlter = (newAlterator) => {
    setAlterator(newAlterator)
  }

  const lifeGreenOvni = data2.green_ovni_life
  const lifeBlueOvni = data2.blue_ovni_life

  const liveBlueAliens = data2.live_blue_aliens
  const liveGreenAliens = data2.live_green_aliens

  return (
    <>
      <Board board={board} setBoard={setBoard} newAlterator={alter} setAlter={setAlter} setPermiso={setPermisoTeleport} permiso={permisoTeleport} />
      <section className='statsGame'>
        <StatsGame team='green' lifeOvni={lifeGreenOvni} liveAliens={liveGreenAliens} greenName={NOMBRE_G} />
        <StatsGame team='blue' lifeOvni={lifeBlueOvni} liveAliens={liveBlueAliens} blueName={NOMBRE_B} />
      </section>
      <Panel setAlter={setAlter} permiso={permisoTeleport} />
      <img src='../public/panel_left.jpg' className='panel_left' />
      <img src='../public/panel_right.jpg' className='panel_right' />
    </>
  )
}

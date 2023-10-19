import { useState } from 'react'
import data2 from '../data2.json'
import { Board } from './Board'
import { Panel } from './Panel'
import { StatsGame } from './StatsGame'

// leer el js
console.log(data2.grid)

export function Game () {
  const [alter, setAlterator] = useState(null)
  const [permisoTeleport, setPermisoTeleport] = useState(true)
  const [board, setBoard] = useState(data2.grid)

  /*
  pide el refresco
  const fetchData = async () => {
    try {
      const response = await fetch('ruta de la api');
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();

      setBoard(data.board);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  }

  useEffect(() => {
    const timeoutId = setTimeout(() => {
      fetchData()
      setGrid(nextBoard);
    }, 1000);
    return () => clearTimeout(timeoutId);
  }, [board]);
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
      <h1>Earth conquest</h1>
      <Board board={board} setBoard={setBoard} newAlterator={alter} setAlter={setAlter} setPermiso={setPermisoTeleport} />
      <section className='statsGame'>
        <StatsGame team='green' lifeOvni={lifeGreenOvni} liveAliens={liveGreenAliens} />
        <StatsGame team='blue' lifeOvni={lifeBlueOvni} liveAliens={liveBlueAliens} />
      </section>
      <Panel setAlter={setAlter} permiso={permisoTeleport} />
    </>
  )
}

import { useState } from 'react'
import data2 from '../data2.json'
import { Board } from './Board'
import { Panel } from './Panel'
import { StatsGame } from './StatsGame'

// leer el js
console.log(data2.grid)

export function Game () {
  const [alterator, setAlterator] = useState(null)

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
      <Board newAlterator={alterator} />
      <section className='statsGame'>
        <StatsGame team='green' lifeOvni={lifeGreenOvni} liveAliens={liveGreenAliens} />
        <StatsGame team='blue' lifeOvni={lifeBlueOvni} liveAliens={liveBlueAliens} />
      </section>
      <Panel setAlter={setAlter} />
    </>
  )
}

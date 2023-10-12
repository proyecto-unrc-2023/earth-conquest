import { alterator } from '../constants.js'
import { useState } from 'react'

export const Panel = ({ setAlter }) => {
  const [showDirections, setShowDirections] = useState(false)
  const handleAlterator = (newAlterator) => {
    setAlter(newAlterator)
  }

  return (
    <section className='modifiers'>
      <h1>Alteradores</h1>
      <button onClick={() => handleAlterator('trap')} value={alterator.trap}>Trap</button>
      <button onClick={() => handleAlterator('teleport')} value={alterator.teleport_in}>Teleport</button>
      <button onClick={() => setShowDirections(!showDirections)}>Directioner</button>
      <>
        {
          showDirections &&
            <div>
              <button onClick={() => handleAlterator('directioner_up')} value={alterator.directioner_up}>Up</button>
              <button onClick={() => handleAlterator('directioner_down')} value={alterator.directioner_down}>Down</button>
              <button onClick={() => handleAlterator('directioner_right')} value={alterator.directioner_right}>Right</button>
              <button onClick={() => handleAlterator('directioner_left')} value={alterator.directioner_left}>Left</button>
            </div>
        }
      </>
    </section>
  )
}

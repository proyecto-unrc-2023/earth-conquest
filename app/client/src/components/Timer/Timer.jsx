import { useState, useEffect } from 'react'
import './Timer.css'

import timmer from '../../sound/timer.mp3'
import start from '../../sound/start.mp3'

export function Timer ({ playSound }) {
  const [counter, setCounter] = useState(4)

  useEffect(() => {
    if ([1, 2, 3].includes(counter)) {
      playSound(timmer)
    }
    if (counter === 0) playSound(start)
    if (counter > -1) {
      const interval = setInterval(() => {
        setCounter((prevCounter) => prevCounter - 1)
      }, 1000)

      return () => clearInterval(interval)
    }
  }, [counter])

  return (
    <section className='box-timer'>
      {[3, 2, 1, 0].map((num) => (
        <img
          key={num}
          src={`../${num}.png`}
          className={`image ${counter === num ? 'show' : ''}`}
          alt={num.toString()}
        />
      ))}
    </section>
  )
}

import { useState, useEffect } from 'react'

export function Timer () {
  const [counter, setCounter] = useState(0)

  if (counter <= 3) {
    useEffect(() => {
      const interval = setInterval(() => {
        setCounter((prevCounter) => prevCounter + 1)
      }, 1000)

      return () => clearInterval(interval)
    }, [counter])
  }

  return (
    <section className='box-timer'>
      {counter === 1 && <img src='../1.png' className='image' alt='1' />}
      {counter === 2 && <img src='../2.png' className='image' alt='2' />}
      {counter === 3 && <img src='../3.png' className='image' alt='3' />}
    </section>
  )
}

import { gameStatus } from '../../constants'
import { useState } from 'react'
import './Menu.css'

export function Menu ({ createGame, setStatusGame, gameId }) {
  const [nameGreen, setNameGreen] = useState('')
  const [nameBlue, setNameBlue] = useState('')

  const JOIN_AS = 'ruta del endpoint'
  const START_GAME = 'http://127.0.0.1:5000/games/start_game'

  const startGame = async () => {
    try {
      const response = await fetch(`${START_GAME}/1`, {
        method: 'PUT'
      })
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      // const data = await response.json()
      // console.log(data)
      setStatusGame(gameStatus.started)
    } catch (error) {
      console.error('Error fetching data: ', error)
    }
  }

  const joinAs = async (team, playerName) => {
    /*
    try {
      const response = await fetch(`${JOIN_AS}/${gameId}/${team}/${playerName}`, {
        method: 'PUT',
        // También se puede enviar el nombre del jugador en el cuerpo
        body: JSON.stringify({ playerName }),
      })
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }

      console.log(`seteo jugador ${playerName} al equipo ${team}`)
    } catch (error) {
      console.error('Error fetching data: ', error)
    }
    */
    console.log(`seteo jugador ${playerName} al equipo ${team}`)
  }

  return (
    <>
      <h2>Main menu</h2>
      <button onClick={createGame}>New Game!</button>
      {
        gameId !== null && // revisar esto
          <>
            <label>
              <input
                type='text'
                placeholder='Insert name'
                value={nameGreen}
                onChange={(e) => {
                  setNameGreen(e.target.value) // TODO: falta controlar nombres vacíos
                }}
              />
              <button onClick={() => joinAs('green', nameGreen)}>Join as Green Player</button>
            </label>
            <label>
              <input
                type='text'
                placeholder='Insert name'
                value={nameBlue}
                onChange={(e) => setNameBlue(e.target.value)}
              />
              <button onClick={() => joinAs('blue')}>Join as Blue Player</button>
            </label>
            <button onClick={startGame}>Start Game</button>
          </>
      }
    </>
  )
}

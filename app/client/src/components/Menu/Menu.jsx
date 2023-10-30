import { gameStatus } from '../../constants'
import { Lobby } from '../Lobby/Lobby'
import { useState } from 'react'
import './Menu.css'

export function Menu ({ createGame, setStatusGame, gameId, message }) {
  const [nameGreen, setNameGreen] = useState('')

  const [allGames, setAllGames] = useState([])
  const JOIN_AS = 'http://127.0.0.1:5000/games/'
  const START_GAME = 'http://127.0.0.1:5000/games/start_game'
  const GET_ALL_GAMES = 'http://127.0.0.1:5000/games/get_all_games'

  const getAllGames = async () => {
    try {
      const response = await fetch(GET_ALL_GAMES)
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()
      const newGames = data.data.games
      setAllGames(newGames)
      console.log(newGames)
    } catch (error) {
      console.error('Error fetching data: ', error)
    }
  }

  const startGame = async () => {
    try {
      const response = await fetch(`${START_GAME}/1`, {
        method: 'PUT'
      })
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()
      console.log(data)
      if (data.success) {
        setStatusGame(gameStatus.started)
      }
    } catch (error) {
      console.error('Error fetching data: ', error)
    }
  }

  const joinAs = async (team, playerName, gameId) => {
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
    if (team === 'green') {
      const hostPlayer = { host: true, playerName, team, gameId }
      // eslint-disable-next-line no-undef
      localStorage.setItem('hostPlayer', JSON.stringify(hostPlayer))
      // eslint-disable-next-line no-undef
      console.log('local storage: ', localStorage.getItem('hostPlayer'))
    } else {
      const guestPlayer = { host: false, playerName, team, gameId }
      // eslint-disable-next-line no-undef
      localStorage.setItem('guestPlayer', JSON.stringify(guestPlayer))
      // eslint-disable-next-line no-undef
      console.log('local storage: ', localStorage.getItem('guestPlayer'))
    }
    console.log(`seteo jugador ${playerName} al equipo ${team}`)
  }

  return (
    <>
      <h2>Main menu</h2>
      <button onClick={createGame}>New Game</button>
      <button onClick={getAllGames}>Join game</button>
      {
        message.length !== 0 &&
          <>
            <p className='message'>{message}</p>
            <p className='message'>Game id: {gameId}</p>
          </>
      }
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
              <button
                onClick={() => joinAs('green', nameGreen, gameId)}
                disabled={!nameGreen}
              >Join
              </button>
            </label>
          </>
      }
      {
        allGames.length > 0 && <Lobby allGames={allGames} joinAs={joinAs} />
      }
    </>
  )
}
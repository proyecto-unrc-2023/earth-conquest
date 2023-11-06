import { Lobby } from '../Lobby/Lobby'
import { useState } from 'react'
import './Menu.css'

export function Menu ({ createGame, startGame, setGameId, setHost, getGame, gameId, message }) {
  const [nameGreen, setNameGreen] = useState('')
  const [allGames, setAllGames] = useState([])
  const [newGameClicked, setNewGameClicked] = useState(false)
  const [joinGameClicked, setJoinGameClicked] = useState(false)

  const JOIN_AS = 'http://127.0.0.1:5000/games/join'
  const GET_ALL_GAMES = 'http://127.0.0.1:5000/games'

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

  const joinAs = async (team, playerName, gameId) => {
    try {
      const response = await fetch(`${JOIN_AS}/${gameId}?team=${team}&player_name=${playerName}`, {
        method: 'PUT'
      })
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()
      console.log(data)
      if (team === 'GREEN') {
        setHost(true)
      } else {
        setHost(false)
        const guestPlayer = { host: false, playerName, team, gameId }
        // eslint-disable-next-line no-undef
        localStorage.setItem('guestPlayer', JSON.stringify(guestPlayer))
      }
      console.log(`seteo jugador ${playerName} al equipo ${team}`)
    } catch (error) {
      console.error('Error fetching data: ', error)
    }
  }

  const handleNewGameClick = () => {
    createGame()
    setJoinGameClicked(true)
  }

  const handleJoinGameClick = () => {
    getAllGames()
    setNewGameClicked(true)
    document.getElementById('join').innerText = 'Refresh games'
  }

  return (
    <>
      <h2>Main menu</h2>
      <button onClick={handleNewGameClick} disabled={newGameClicked}>New Game</button>
      <button onClick={handleJoinGameClick} disabled={joinGameClicked} id='join'>Join game</button>
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
                  setNameGreen(e.target.value)
                }}
              />
              <button
                onClick={() => joinAs('GREEN', nameGreen, gameId)}
                disabled={!nameGreen}
              >Join
              </button>
            </label>
          </>
      }
      {
        allGames.length > 0 && <Lobby allGames={allGames} setGameId={setGameId} joinAs={joinAs} />
      }
    </>
  )
}

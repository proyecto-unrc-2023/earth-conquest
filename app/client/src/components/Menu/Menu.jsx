import { Lobby } from '../Lobby/Lobby'
import { useState } from 'react'
import { createGame, getAllGames, API } from '../../services/appService'
import './Menu.css'

export function Menu ({ game, setGame }) {
  const [nameGreen, setNameGreen] = useState('')
  const [allGames, setAllGames] = useState([])
  const [newGameClicked, setNewGameClicked] = useState(false)
  const [joinGameClicked, setJoinGameClicked] = useState(false)
  const [message, setMessage] = useState('')
  const JOIN_AS = `${API}games/join`

  const joinAs = async (team, playerName, currentGameId) => {
    console.log('JOIN AS: ', JOIN_AS, currentGameId, team, playerName)
    try {
      const response = await fetch(`${JOIN_AS}/${currentGameId}?team=${team}&player_name=${playerName}`, {
        method: 'PUT'
      })
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()
      console.log(data)
      if (team === 'GREEN') {
        setGame((prevState) => ({
          ...prevState,
          host: true,
          playerGreen: playerName
        }))
        console.log(`seteo jugador ${playerName} al equipo ${team}, gameId: ${currentGameId}`)
      } else {
        setGame((prevState) => ({
          ...prevState,
          host: false,
          teamPlayer: 'BLUE',
          playerBlue: playerName,
          gameId: currentGameId
        }))
        // const guestPlayer = { playerName, team, game.gameId }
        // // eslint-disable-next-line no-undef
        // localStorage.setItem('guestPlayer', JSON.stringify(guestPlayer))
      }
    } catch (error) {
      console.error('Error fetching data: ', error)
    }
  }

  const handleNewGameClick = async () => {
    const data = await createGame()
    console.log('CREATE GAME: ', data)
    setGame((prevState) => ({
      ...prevState,
      board: data.game.board.grid, // ver bien como llega
      host: true,
      teamPlayer: 'GREEN',
      gameId: data.gameId
    }))
    setMessage(data.message)
    setJoinGameClicked(true)
  }

  const handleJoinGameClick = async () => {
    const games = await getAllGames()
    setAllGames(games)
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
            <p className='message'>Game id: {game.gameId}</p>
          </>
      }
      {
        game.gameId !== null && // revisar esto
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
                onClick={() => joinAs('GREEN', nameGreen, game.gameId)}
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

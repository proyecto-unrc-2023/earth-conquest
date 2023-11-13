import { Lobby } from '../Lobby/Lobby'
import { useState } from 'react'
import { createGame, getAllGames, joinAs } from '../../services/appService'
import './Menu.css'

export function Menu ({ game, setGame }) {
  const [nameGreen, setNameGreen] = useState('')
  const [allGames, setAllGames] = useState([])
  const [newGameClicked, setNewGameClicked] = useState(false)
  const [joinGameClicked, setJoinGameClicked] = useState(false)

  const handleNewGameClick = async () => {
    const data = await createGame()
    console.log('CREATE GAME: ', data)
    setGame((prevState) => ({
      ...prevState,
      board: data.game.board.grid,
      host: true,
      teamPlayer: 'GREEN',
      gameId: data.gameId
    }))
    setJoinGameClicked(true)
  }

  const handleJoinGameClick = async () => {
    const games = await getAllGames()
    setAllGames(games)
    setNewGameClicked(true)
    document.getElementById('join').innerText = 'Refresh games'
  }

  const cuandoSeJoinea = (team, name, currentId) => {
    joinAs(team, name, currentId)
    if (team === 'GREEN') {
      setGame((prevState) => ({
        ...prevState,
        host: true,
        playerGreen: name
      }))
    } else {
      setGame((prevState) => ({
        ...prevState,
        host: false,
        teamPlayer: team,
        playerBlue: name,
        gameId: currentId
      }))
      const guestPlayer = { name, team, currentId }
      // eslint-disable-next-line no-undef
      localStorage.setItem('guestPlayer', JSON.stringify(guestPlayer))
    }
  }

  return (
    <>
      <h2>Main menu</h2>
      <button onClick={handleNewGameClick} disabled={newGameClicked}>New Game</button>
      <button onClick={handleJoinGameClick} disabled={joinGameClicked} id='join'>Join game</button>
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
                onClick={() => cuandoSeJoinea('GREEN', nameGreen, game.gameId)}
                disabled={!nameGreen}
              >Join
              </button>
            </label>
          </>
      }
      {
        allGames.length > 0 && <Lobby allGames={allGames} cuandoSeJoinea={cuandoSeJoinea} />
      }
    </>
  )
}

import { Lobby } from '../Lobby/Lobby'
import { useState } from 'react'
import { createGame, getAllGames, joinAs, getGame } from '../../services/appService'
import hoverSound from '../../sound/select.mp3' // ver

import './Menu.css'

export function Menu ({ game, setGame }) {
  const [nameGreen, setNameGreen] = useState('')
  const [allGames, setAllGames] = useState([])
  const [newGameClicked, setNewGameClicked] = useState(false)
  const [joinGameClicked, setJoinGameClicked] = useState(false)
  const [message, setMessage] = useState({ gameMessage: '', joinMessage: '' })

  const playHoverSound = () => {
    // eslint-disable-next-line no-undef
    const audio = new Audio(hoverSound)
    audio.play()
  }

  const handleNewGameClick = () => {
    createGame().then((data) => {
      console.log('CREATE GAME: ', data)
      setMessage((prevState) => ({
        ...prevState,
        gameMessage: data.message
      }))
      setGame((prevState) => ({
        ...prevState,
        gameId: data.data.gameId
      }))
      setJoinGameClicked(true)
    })
  }

  const handleJoinGameClick = async () => {
    const games = await getAllGames()
    setAllGames(games)
    setNewGameClicked(true)
    document.getElementById('join').innerText = 'Refresh games'
  }

  const cuandoSeJoinea = (team, name, currentId) => {
    joinAs(team, name, currentId).then((data) => {
      setMessage((prevState) => ({
        ...prevState,
        joinMessage: data.message
      }))
    })
    getGame(currentId).then((game) => {
      console.log('GAME: ', game)
      if (team === 'GREEN') {
        setGame((prevState) => ({
          ...prevState,
          host: true,
          board: game.board.grid,
          teamPlayer: team,
          playerGreen: name
        }))
      } else {
        setGame((prevState) => ({
          ...prevState,
          host: false,
          teamPlayer: team,
          cleanBoard: game.board.grid,
          board: game.board.grid,
          playerBlue: name,
          gameId: currentId
        }))
      }
    })
  }

  return (
    <>
      <h1 className='tittle-main'>EARTH CONQUEST </h1>
      <h2>  MENU  </h2>
      <button className='btn' onClick={handleNewGameClick} disabled={newGameClicked} onMouseEnter={playHoverSound}>NEW GAME</button>
      {message.gameMessage?.length > 0 && <p className='message'>{message.gameMessage}</p>}
      <button className='btn' onClick={handleJoinGameClick} disabled={joinGameClicked} onMouseEnter={playHoverSound} id='join'>JOIN GAME</button>
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
            {
              message.joinMessage.length > 0 && <p className='message'>{message.joinMessage}</p>
            }
          </>
      }
      {
        allGames.length > 0 && <Lobby allGames={allGames} cuandoSeJoinea={cuandoSeJoinea} />
      }
    </>
  )
}

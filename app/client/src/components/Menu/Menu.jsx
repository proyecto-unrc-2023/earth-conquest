import { Lobby } from '../Lobby/Lobby'
import { Login } from '../Login/Login'
import { useState } from 'react'
import { createGame, getAllGames, joinAs, getGame } from '../../services/appService'
import buttonSound from '../../sound/select.mp3'

import './Menu.css'

export function Menu ({ game, setGame }) {
  const [nameGreen, setNameGreen] = useState('')
  const [allGames, setAllGames] = useState([])
  const [newGameClicked, setNewGameClicked] = useState(false)
  const [joinGameClicked, setJoinGameClicked] = useState(false)
  const [message, setMessage] = useState({ gameMessage: '', joinMessage: '' })
  const [showLogin, setShowLogin] = useState(false)
  const [showLobby, setShowLobby] = useState(false)

  const playSound = () => {
    // eslint-disable-next-line no-undef
    const audio = new Audio(buttonSound)
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
      setShowLogin(true)
    })
  }

  const handleJoinGameClick = async () => {
    const games = await getAllGames()
    setAllGames(games)
    setNewGameClicked(true)
    document.getElementById('join').innerText = 'REFRESH GAMES'
    if (!showLobby) setShowLobby(true)
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
      <img className='tittle-main' src='../tittle.png' alt='tittle' />
      {!showLogin && !showLobby && (
        <>
          <h2>MENU</h2>
          <button className='btn' onClick={handleNewGameClick} disabled={newGameClicked} onMouseEnter={playSound}>
            NEW GAME
          </button>
          {message.gameMessage?.length > 0 && <p className='message'>{message.gameMessage}</p>}
          <button className='btn' onClick={handleJoinGameClick} disabled={joinGameClicked} onMouseEnter={playSound} id='join'>
            JOIN GAME
          </button>

        </>
      )}
      {
      showLogin &&
        <Login
          game={game}
          setNameGreen={setNameGreen}
          cuandoSeJoinea={cuandoSeJoinea}
          nameGreen={nameGreen}
          message={message}
          playSound={playSound}
        />
      }
      {
        showLobby && (
          <>
            <button className='btn' onClick={handleJoinGameClick} disabled={joinGameClicked} onMouseEnter={playSound} id='join'>
              REFRESH GAMES
            </button>
            {
              allGames.length > 0 && <Lobby allGames={allGames} cuandoSeJoinea={cuandoSeJoinea} />
            }
          </>
        )
      }
    </>
  )
}

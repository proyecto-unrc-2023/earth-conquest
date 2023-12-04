import { Lobby } from '../Lobby/Lobby'
import { Login } from '../Login/Login'
import { useState } from 'react'
import toast, { Toaster } from 'react-hot-toast'
import { createGame, getAllGames, joinAs, getGame } from '../../services/appService'
import buttonSound from '../../sound/select.mp3'

import './Menu.css'

export function Menu ({ game, setGame, playSound }) {
  const [nameGreen, setNameGreen] = useState('')
  const [allGames, setAllGames] = useState([])
  const [newGameClicked, setNewGameClicked] = useState(false)
  const [joinGameClicked, setJoinGameClicked] = useState(false)
  const [showLogin, setShowLogin] = useState(false)
  const [showLobby, setShowLobby] = useState(false)

  // Crea un nuevo juego
  const handleNewGameClick = () => {
    createGame().then((data) => {
      toast.success(data.message) // mensaje de inicio de juego creado
      setGame((prevState) => ({
        ...prevState,
        gameId: data.data.gameId
      }))
      setJoinGameClicked(true)
      setShowLogin(true)
    })
  }

  // Entra a un juego
  const handleJoinGameClick = async () => {
    const games = await getAllGames()
    setAllGames(games)
    setNewGameClicked(true)
    document.getElementById('join').innerText = 'REFRESH GAMES'
    if (!showLobby) setShowLobby(true)
  }

  // Joinea a un usuario a un juego creado
  const cuandoSeJoinea = (team, name, currentId) => {
    joinAs(team, name, currentId).then((data) => {
      toast.success(data.message) // mensaje de 'join success'
    })

    getGame(currentId).then((game) => {
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
          <button className='btn' onClick={handleNewGameClick} disabled={newGameClicked} onMouseEnter={() => playSound(buttonSound)}>
            NEW GAME
          </button>
          <button className='btn' onClick={handleJoinGameClick} disabled={joinGameClicked} onMouseEnter={() => playSound(buttonSound)} id='join'>
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
          playSound={playSound}
        />
      }
      {
        showLobby && (
          <>
            <button className='btn' onClick={handleJoinGameClick} disabled={joinGameClicked} onMouseEnter={() => playSound(buttonSound)} id='join'>
              REFRESH GAMES
            </button>
            {
              allGames.length > 0 && <Lobby allGames={allGames} cuandoSeJoinea={cuandoSeJoinea} playSound={playSound} />
            }
          </>
        )
      }
      <Toaster />
    </>
  )
}

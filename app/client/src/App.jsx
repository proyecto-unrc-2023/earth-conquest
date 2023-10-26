import { useState } from 'react'
import { Game } from './components/Game/Game'
import { Menu } from './components/Menu/Menu'
import { gameStatus } from './constants'
import { GamesTable } from './components/GamesTable/GamesTable'

function App () {
  const [statusGame, setStatusGame] = useState(null)
  const [gameId, setGameId] = useState(null)
  const [message, setMessage] = useState('')
  const [allGames, setAllGames] = useState([])
  const CREATE_GAME = 'http://127.0.0.1:5000/games/create_game'
  const GET_ALL_GAMES = 'http://127.0.0.1:5000/games/get_all_games'

  const createGame = async () => {
    try {
      const response = await fetch(CREATE_GAME, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        // cache: no-cache, *default, reload, force-cache, only-if-cached
        // credentials: omit, *same-origin, include
        headers: {
          'Content-Type': 'application/json'
        }
      })
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()
      console.log(data)
      setGameId(data.gameId)
      setStatusGame(gameStatus.notStarted)
      setMessage(data.message)
    } catch (error) {
      console.error('Error fetching data:', error)
    }
  }

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

  return (

    <main>
      {
        statusGame !== gameStatus.started &&
          <Menu createGame={createGame} setStatusGame={setStatusGame} gameId={gameId} message={message} />
      }
      {
        // statusGame === gameStatus.started && */
        // <Game gameId={gameId} />
      }
      <button onClick={getAllGames}>Join game</button>

      {
        allGames.length > 0 && <GamesTable allGames={allGames} />
      }

    </main>
  )
}

export default App

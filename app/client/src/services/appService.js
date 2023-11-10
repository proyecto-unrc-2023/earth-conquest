export const API = 'http://127.0.0.1:5000/'
const CREATE_GAME = 'games/'
const START_GAME = 'games/start_game/'
const GET_GAME = `${API}games/`
const GET_ALL_GAMES = `${API}games`
const FREE_POSITION = `${API}games/is_free_position`
const SEND_ALTERATOR = `${API}games/set_alterator`
const REFRESH = `${API}games/refresh_board`
const ACT = `${API}games/act_board`
const SPAWN_ALIENS = `${API}games/spawn_aliens`



export const createGame = async () => {
  try {
    const response = await fetch(API + CREATE_GAME, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      }
    })
    if (!response.ok) {
      throw new Error('Network response was not ok')
    }
    const data = await response.json()
    return data.data
  } catch (error) {
    console.error('Error fetching data:', error)
  }
}

export const startGame = async (currentGameId) => {
  try {
    const response = await fetch(API + START_GAME + currentGameId, {
      method: 'PUT'
    })
    if (!response.ok) {
      throw new Error('Network response was not ok')
    }
    const data = await response.json()
    console.log('START GAME:', data)
  } catch (error) {
    console.error('Error fetching data: ', error)
  }
}

export const getAllGames = async () => {
  try {
    const response = await fetch(GET_ALL_GAMES)
    if (!response.ok) {
      throw new Error('Network response was not ok')
    }
    const data = await response.json()
    const newGames = data.data.games
    return newGames
  } catch (error) {
    console.error('Error fetching data: ', error)
  }
}

export const isFreePosition = async (row, col, gameId) => {
  try {
    const response = await fetch(`${FREE_POSITION}/${gameId}?x=${row}&y=${col}`)
    if (!response.ok) {
      throw new Error('Network response was not ok')
    }
    const data = await response.json()
    return (data.success)
  } catch (error) {
    console.error('Error is valid position', error)
  }
}

export const sendAlterator = async (newAlterator) => {
  console.log('esto es lo que mando a la api: ', JSON.stringify(newAlterator))
  try {
    const response = await fetch(`${SEND_ALTERATOR}/${game.gameId}`, {
      method: 'PUT',
      headers:
      {
        'Content-Type': 'application/json;charset=UTF-8'
      },
      body: JSON.stringify(newAlterator)
    })
    if (!response.ok) {
      throw new Error('Network response was not ok')
    }
    const data = await response.json()
    console.log(data)
  } catch (error) {
    console.error('Error set alterator', error)
  }
}


export const refresh = async (gameId) => {
  try {
    const response = await fetch(REFRESH + gameId, {
      method: 'PUT'
    })
    if (!response.ok) {
      throw new Error('Network response was not ok')
    }
  } catch (error) {
    console.error('Error fetching data in refresh:', error)
  }
}

export const act = async (gameId) => {
  try {
    const response = await fetch(ACT + gameId, {
      method: 'PUT'
    })
    if (!response.ok) {
      throw new Error('Network response was not ok')
    }
  } catch (error) {
    console.error('Error fetching data in act:', error)
  }
}

export const spawnAliens = async (gameId) => {
  try {
    const response = await fetch(SPAWN_ALIENS  + gameId, {
      method: 'PUT'
    })
    if (!response.ok) {
      throw new Error('Network response was not ok')
    }
  } catch (error) {
    console.error('Error spawn aliens in base:', error)
  }
}

const getGame = async (currentGameId) => {
  try {
    const response = await fetch(GET_GAME + currentGameId)
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()
      console.log('GET BOARD:', data)
    } catch (error) {
      console.error('Error get game:', error)
    }
  }
}

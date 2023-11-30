import { useState, useEffect } from 'react'
import { Board } from '../Board/Board'
import { Panel } from '../Panel/Panel'
import { Timer } from '../Timer/Timer'
import { StatsGame } from '../StatGame/StatsGame'
import { nextState, API } from '../../services/appService'
import { handleHash } from '../../services/alienService'
import gameSound from '../../sound/game.mp3'
import './Game.css'

export function Game ({ game, setGame, originalBoard, playSound }) {
  const [alter, setAlterator] = useState(null)
  const [aliens, setAliens] = useState([])
  const [teleporterEnabled, setTeleporterEnabled] = useState(true)
  const [teleportIn, setTeleportIn] = useState([{ row: null, col: null }])
  const [teleportOut, setTeleportOut] = useState([{ row: null, col: null }])
  const [showTimer, setShowTimer] = useState(true)
  // eslint-disable-next-line no-undef
  const [audio] = useState(new Audio(gameSound))
  const [isPlaying, setIsPlaying] = useState(true)

  useEffect(() => {
    let sse
    let timer

    // arranca el contador luego de mostrar los numeros
    if (showTimer) {
      timer = setTimeout(() => {
        setShowTimer(false)
      }, 5500)
    } else {
      countdown()
      audio.loop = true
      audio.play()
    }

    // Actualiza constantemente los datos del juego
    const handleGameUpdate = (data) => {
      setGame((prevState) => ({
        ...prevState,
        board: handleHash(aliens, data.board.cells, originalBoard, setTeleportIn, setTeleportOut),
        statusGame: data.status,
        blueOvniLife: data.board.blue_ovni_life,
        greenOvniLife: data.board.green_ovni_life,
        aliveGreenAliens: data.alive_green_aliens,
        aliveBlueAliens: data.alive_blue_aliens,
        winner: data.winner
      }))
    }

    const startSSE = () => {
      // eslint-disable-next-line no-undef
      sse = new EventSource(API + `games/sse/${game.gameId}`)
      sse.onmessage = (e) => {
        const data = JSON.parse(e.data)
        handleGameUpdate(data)
      }

      sse.onerror = (e) => {
        console.error('Error en el sse de game', e)
        sse.close()
      }
    }

    startSSE()

    return () => {
      clearTimeout(timer)
      if (sse) {
        sse.close()
      }
    }
  }, [showTimer])

  const toggleSound = () => {
    if (isPlaying) {
      audio.pause()
    } else {
      audio.play()
    }
    setIsPlaying(!isPlaying)
  }

  // Funcion que pide el nextState
  async function countdown () {
    if (game.host) {
      await nextState(game.gameId)
      setTimeout(countdown, 500)
    }
  }

  return (
    <>
      {showTimer && <Timer playSound={playSound} />}
      <Board
        game={game}
        teleportIn={teleportIn}
        teleportOut={teleportOut}
        newAlterator={alter}
        setAlter={setAlterator}
        setTeleporterEnabled={setTeleporterEnabled}
        teleporterEnabled={teleporterEnabled}
        playSound={playSound}
      />
      <section className='statsGame'>
        <StatsGame
          team='green'
          lifeOvni={game.greenOvniLife}
          liveAliens={game.aliveGreenAliens}
          playerName={game.playerGreen}
        />
        <StatsGame
          team='blue'
          lifeOvni={game.blueOvniLife}
          liveAliens={game.aliveBlueAliens}
          playerName={game.playerBlue}
        />
      </section>
      <button onClick={toggleSound} className='btn-play-pause'>
        {isPlaying
          ? <img src='../pause.png' alt='pause' className='icons-play-pause' />
          : <img src='../play.png' alt='pause' className='icons-play-pause' />}
      </button>
      <Panel setAlter={setAlterator} teleporterEnabled={teleporterEnabled} team={game.teamPlayer} />
    </>
  )
}

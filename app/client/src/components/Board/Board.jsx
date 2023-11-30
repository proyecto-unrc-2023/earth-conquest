import { Cell } from '../Cell/Cell'
import { alterator, team } from '../../constants.js'
import './Board.css'
import { useState } from 'react'
import toast, { Toaster } from 'react-hot-toast'
import { isFreePosition, sendAlterator } from '../../services/appService'
import directSound from '../../sound/directioner.mp3'
import trapSound from '../../sound/trap.mp3'
import inSound from '../../sound/in.mp3'
import uotSound from '../../sound/out.mp3'

export const Board = ({ game, teleportIn, teleportOut, newAlterator, setAlter, setTeleporterEnabled, teleporterEnabled, playSound }) => {
  const [teleportX, setTeleportX] = useState(null)
  const [teleportY, setTeleportY] = useState(null)
  const TELEPORT_RANGE = 4

  // Variable para habilitar el sonido si la peticion fue correcta
  let sound = false

  // Funcion para dar el rango de teleport
  const outOfTeleportRange = (row, col, x, y) => {
    return (Math.abs(row - x) >= TELEPORT_RANGE || Math.abs(col - y) >= TELEPORT_RANGE)
  }

  // Funcion para dar el rango de la base segun el team
  const isBase = (row, col, x, y, teamBase) => {
    if (teamBase === team.GREEN) {
      return (row <= x && col <= y)
    } else {
      return (row >= x && col >= y)
    }
  }

  // Genera un objeto Alterador, dependiendo que alterador se haya elegido
  const generateAlterator = (nameObj, posInit, posEnd, dir, teamObj) => {
    const newObject =
     {
       alterator: {
         name: nameObj,
         positionInit: posInit,
         positionEnd: posEnd,
         direction: dir
       },
       team: teamObj
     }
    return newObject
  }

  // Envia a la API el nuevo alterador
  const updateBoard = async (row, col) => {
    if (newAlterator === null) return
    if (!await isFreePosition(row, col, game.gameId)) {
      toast.error('This is not a free position')
      return
    }
    if ((newAlterator === alterator.TELEPORTER_OUT) && outOfTeleportRange(row, col, teleportX, teleportY)) return

    const newBoard = [...game.board]
    setAlteratorInCell(row, col, newAlterator, newBoard)
  }

  const setAlteratorInCell = async (row, col, newAlterator, newBoard) => {
    if (newAlterator === alterator.TRAP) {
      const newTrap = generateAlterator(newAlterator, { x: row, y: col }, { x: -1, y: -1 }, '-', game.teamPlayer)
      const data = await sendAlterator(game.gameId, newTrap)
      sound = data.success
      if (data.errors) toast.error(data.errors)

      if (sound) playSound(trapSound)
    } else {
      const alteratorSplit = newAlterator.split('_')
      const alteratorName = alteratorSplit[0]
      const alteratorDirection = alteratorSplit[1]

      if (alteratorName === 'DIRECTIONER') {
        const newDirectioner = generateAlterator(alteratorName, { x: row, y: col }, { x: -1, y: -1 }, alteratorDirection, game.teamPlayer)

        const data = await sendAlterator(game.gameId, newDirectioner)
        sound = data.success
        if (data.errors) toast.error(data.errors)

        if (sound) playSound(directSound)
      } else if (alteratorName === 'TELEPORTER') {
        if (alteratorDirection === 'IN') {
          newBoard[row][col].alterator = newAlterator
          playSound(inSound)
          setAlter(alterator.TELEPORTER_OUT)
          setTeleporterEnabled(false)
          setTeleportX(row)
          setTeleportY(col)
        } else {
          const newTeleport = generateAlterator(alteratorName, { x: teleportX, y: teleportY }, { x: row, y: col }, alteratorDirection, game.teamPlayer)

          const data = await sendAlterator(game.gameId, newTeleport)
          sound = data.success
          if (data.errors) toast.error(data.errors)

          if (sound) playSound(uotSound)
          setAlter(null)
          setTeleporterEnabled(true)
        }
      }
    }
  }

  return (
    <section className='board'>
      {
        game.board.map((row, i) => {
          return (
            row.map((cell, j) => {
              return (
                <Cell
                  key={j}
                  col={j}
                  row={i}
                  updateBoard={updateBoard}
                  greenBase={game.greenOvniRange}
                  blueBase={game.blueOvniRange}
                  teleporterEnabled={teleporterEnabled}
                  teleportX={teleportX}
                  teleportY={teleportY}
                  teleportOut={teleportOut}
                  teleportIn={teleportIn}
                  isBase={isBase}
                  outOfTeleportRange={outOfTeleportRange}
                >
                  {cell}
                </Cell>

              )
            })
          )
        })
      }
      <Toaster />
    </section>
  )
}

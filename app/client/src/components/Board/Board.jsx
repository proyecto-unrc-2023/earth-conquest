import { Cell } from '../Cell/Cell'
import { alterator, team } from '../../constants.js'
import './Board.css'
import { useState } from 'react'
import { isFreePosition, sendAlterator } from '../../services/appService'
import directSound from '../../sound/directioner.mp3'
import trapSound from '../../sound/trap.mp3'
import inSound from '../../sound/in.mp3'
import uotSound from '../../sound/out.mp3'


export const Board = ({ game, teleportIn, teleportOut, newAlterator, setAlter, setTeleporterEnabled, teleporterEnabled, playSound }) => {
  console.log('ESTE ES EL BOARD QUE LLEGA A BOARD', game.board)
  const [teleportX, setTeleportX] = useState(null)
  const [teleportY, setTeleportY] = useState(null)
  const TELEPORT_RANGE = 4

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

  const updateBoard = async (row, col) => {
    if (newAlterator === null) return
    if (!await isFreePosition(row, col, game.gameId)) return
    if ((newAlterator === alterator.TELEPORTER_OUT) && outOfTeleportRange(row, col, teleportX, teleportY)) return

    const newBoard = [...game.board]
    setAlteratorInCell(row, col, newAlterator, newBoard)
  }

  const setAlteratorInCell = async (row, col, newAlterator, newBoard) => {
    if (newAlterator === alterator.TRAP) {
      const newTrap = {
        alterator: {
          name: newAlterator,
          positionInit: { x: row, y: col },
          positionEnd: { x: -1, y: -1 },
          direction: '-'
        },
        team: game.teamPlayer
      }
      sound = await sendAlterator(game.gameId, newTrap)
      if (sound) playSound(trapSound)
    } else {
      const alteratorSplit = newAlterator.split('_')
      const alteratorName = alteratorSplit[0]
      const alteratorDirection = alteratorSplit[1]

      if (alteratorName === 'DIRECTIONER') {
        const newDirectioner = {
          alterator: {
            name: alteratorName,
            positionInit: { x: row, y: col },
            positionEnd: { x: -1, y: -1 },
            direction: alteratorDirection
          },
          team: game.teamPlayer
        }

        sound = await sendAlterator(game.gameId, newDirectioner)
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
          const newTeleport = {
            alterator: {
              name: alteratorName,
              positionInit: { x: teleportX, y: teleportY },
              positionEnd: { x: row, y: col },
              direction: alteratorDirection
            },
            team: game.teamPlayer
          }
          // esto retorna si se seteo
          sound = await sendAlterator(game.gameId, newTeleport)
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
    </section>
  )
}

import { Cell } from '../Cell/Cell'
import { alterator, team } from '../../constants.js'
import './Board.css'
import { useState } from 'react'
import { isFreePosition, sendAlterator } from '../../services/appService'

export const Board = ({ game, newAlterator, setAlter, setTeleporterEnabled, teleporterEnabled }) => {
  const [teleportX, setTeleportX] = useState(null)
  const [teleportY, setTeleportY] = useState(null)
  const TELEPORT_RANGE = 4

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
      await sendAlterator(newTrap)
    } else {
      const alteratorSplit = newAlterator.split('_')
      const alteratorName = alteratorSplit[0]
      const alteratorDirection = alteratorSplit[1]

      if (alteratorName === 'DIRECTIONER') {
        console.log('entre a un directioner')
        const newDirectioner = {
          alterator: {
            name: alteratorName,
            positionInit: { x: row, y: col },
            positionEnd: { x: -1, y: -1 },
            direction: alteratorDirection
          },
          team: game.teamPlayer
        }

        await sendAlterator(newDirectioner)
      } else if (alteratorName === 'TELEPORTER') {
        console.log('entre a un teleporter')
        if (alteratorDirection === 'IN') {
          newBoard[row][col].alterator = newAlterator
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
          await sendAlterator(newTeleport)
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

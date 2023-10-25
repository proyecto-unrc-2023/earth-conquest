import data2 from '../../data2.json'

import { Cell } from '../Cell/Cell'
import { alterator, team } from '../../constants.js'
import './Board.css'
import { useState } from 'react'

export const Board = ({ board, setBoard, newAlterator, setAlter, setTeleporterEnabled, teleporterEnabled, gameId }) => {
  const VALID_POSITION = 'http://127.0.0.1:5000/games/isValidPosition' // verificar
  const SEND_ALTERATOR = 'http://127.0.0.1:5000/games/setAlterator' // verificar
  const [teleportX, setTeleportX] = useState(null)
  const [teleportY, setTeleportY] = useState(null)
  const TELEPORT_RANGE = 4

  const greenOvniRange = data2.green_ovni_range
  const blueOvniRange = data2.blue_ovni_range

  // Funcion para dar el rango de teleport
  const outOfTeleportRange = (row, col, x, y) => {
    return (Math.abs(row - x) >= TELEPORT_RANGE || Math.abs(col - y) >= TELEPORT_RANGE)
  }

  // Funcion para dar el rango de la base segun el team
  const isBase = (row, col, x, y, teamBase) => {
    if (teamBase === team.green) {
      return (row <= x && col <= y)
    } else {
      return (row >= x && col >= y)
    }
  }

  const updateBoard = (row, col) => {
    if (newAlterator === null) return
    if (board[row][col].alterator !== null || board[row][col].modifier !== null) return
    if (row <= data2.green_ovni_range.x && col <= data2.green_ovni_range.y) return
    if (row >= data2.blue_ovni_range.x && col >= data2.blue_ovni_range.y) return
    if (
      (outOfTeleportRange(row, col, teleportX, teleportY) &&
      (isBase(row, col, greenOvniRange.x, greenOvniRange.y, team.green) ||
      isBase(row, col, blueOvniRange.x, blueOvniRange.y, team.blue)))
    ) return
    if (outOfTeleportRange(row, col, teleportX, teleportY) && (newAlterator === alterator.teleport_out)) return

    const newBoard = [...board]
    setAlteratorInCell(row, col, newAlterator, newBoard)
    setBoard(newBoard)
    console.log(board)
    // TODO: controlar ganador.
  }
  const sendAlterator = async (row, col, newAlterator) => {
    try {
      const response = await fetch(`${SEND_ALTERATOR}/${row}/${col}`, {
        method: 'PUT',
        body: JSON.stringify({ alterator: newAlterator })
      })
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
    } catch (error) {
      console.error('Error set trap', error)
    }
  }
  const isValidPosition = async (row, col) => {
    try {
      const response = await fetch(`${VALID_POSITION}/${gameId}/${row}/${col}`)
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()
      if (data.success) {
        return true
      } else {
        return false
      }
    } catch (error) {
      console.error('Error is valid position', error)
    }
  }

  const setAlteratorInCell = async (row, col, newAlterator, newBoard) => {
    if (await isValidPosition(row, col)) {
      if (newAlterator === alterator.trap) {
        const newTrap = {
          name: newAlterator,
          positionInit: { x: row, y: col },
          positionEnd: null,
          direction: null
        }
        await sendAlterator(row, col, newTrap)
      } else {
        const alteratorSplit = newAlterator.split('_')
        const alteratorName = alteratorSplit[0]
        const alteratorDirection = alteratorSplit[1]

        if (alteratorName === 'directioner') {
          const newDirectioner = {
            name: alteratorName,
            positionInit: { x: row, y: col },
            positionEnd: null,
            direction: alteratorDirection
          }
          await sendAlterator(row, col, newDirectioner)
        } else if (alteratorName === 'teleport') {
          const newTeleport = {
            name: alteratorName,
            positionInit: { x: row, y: col },
            positionEnd: null,
            direction: alteratorDirection
          }
          if (alteratorDirection === 'in') {
            newBoard[row][col].alterator = newAlterator
            // cambia estado a teleport out
            setAlter(alterator.teleport_out)
            setTeleporterEnabled(false)
            setTeleportX(row)
            setTeleportY(col)
          } else {
            newTeleport.positionEnd.x = row
            newTeleport.positionEnd.y = col
            await sendAlterator(row, col, newTeleport)
            setAlter(null)
            setTeleporterEnabled(true)
          }
        }
      }
    }
  }

  return (
    <section className='board' style={{ gridTemplateColumns: `repeat(${board[0].length}, 1fr)` }}>
      {
          board.map((row, i) => {
            return (
              row.map((cell, j) => {
                return (
                  <Cell
                    key={j}
                    col={j}
                    row={i}
                    updateBoard={updateBoard}
                    greenBase={greenOvniRange}
                    blueBase={blueOvniRange}
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

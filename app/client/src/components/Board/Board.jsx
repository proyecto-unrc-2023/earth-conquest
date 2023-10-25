import data2 from '../../data2.json'
import { Cell } from '../Cell/Cell'
import { alterator, team } from '../../constants.js'
import './Board.css'
import { useState } from 'react'

export const Board = ({ board, setBoard, newAlterator, setAlter, setPermiso, permiso }) => {
  const [teleportX, setTeleportX] = useState(null)
  const [teleportY, setTeleportY] = useState(null)
  const TELEPORT_RANGE = 4

  const greenOvniRange = data2.green_ovni_range
  const blueOvniRange = data2.blue_ovni_range

  // Funcion para dar el rango de teleport
  const isTeleportRange = (row, col, x, y) => {
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
      (isTeleportRange(row, col, teleportX, teleportY) &&
      (isBase(row, col, greenOvniRange.x, greenOvniRange.y, team.green) ||
      isBase(row, col, blueOvniRange.x, blueOvniRange.y, team.blue)))
    ) return
    if (isTeleportRange(row, col, teleportX, teleportY) && (newAlterator === alterator.teleport_out)) return

    const newBoard = [...board]
    setAlteratorInCell(row, col, newAlterator, newBoard)
    setBoard(newBoard)
    console.log(board)
  }

  const setAlteratorInCell = (row, col, newAlterator, newBoard) => {
    // mandarle a la api para preguntarle si la posición es valida
    if (newAlterator === alterator.directioner_up) {
      newBoard[row - 2][col].alterator = newAlterator
      newBoard[row - 1][col].alterator = newAlterator
      newBoard[row][col].alterator = newAlterator
    } else if (newAlterator === alterator.directioner_down) {
      newBoard[row + 2][col].alterator = newAlterator
      newBoard[row + 1][col].alterator = newAlterator
      newBoard[row][col].alterator = newAlterator
    } else if (newAlterator === alterator.directioner_right) {
      newBoard[row][col + 2].alterator = newAlterator
      newBoard[row][col + 1].alterator = newAlterator
      newBoard[row][col].alterator = newAlterator
    } else if (newAlterator === alterator.directioner_left) {
      newBoard[row][col - 2].alterator = newAlterator
      newBoard[row][col - 1].alterator = newAlterator
      newBoard[row][col].alterator = newAlterator
    } else if (newAlterator === alterator.teleport_in) {
      // aca preguntar si es posición válida
      newBoard[row][col].alterator = newAlterator
      // cambia estado a teleport out
      setAlter(alterator.teleport_out)
      setPermiso(false)
      setTeleportX(row)
      setTeleportY(col)
    } else if (newAlterator === alterator.teleport_out) {
      newBoard[row][col].alterator = newAlterator
      setAlter(null)
      setPermiso(true)
    } else {
      newBoard[row][col].alterator = newAlterator
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
                    permiso={permiso}
                    teleportX={teleportX}
                    teleportY={teleportY}
                    isBase={isBase}
                    isTeleportRange={isTeleportRange}
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

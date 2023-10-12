import data2 from '../data2.json'
import { Cell } from './Cell'
import { alterator } from '../constants.js'
import { useState } from 'react'

export const Board = ({ newAlterator }) => {
  const [board, setBoard] = useState(data2.grid)

  const setAlteratorInCell = (row, col, newAlterator, newBoard) => {
    if (newAlterator === alterator.directioner_up) {
      newBoard[row - 2][col].alterator = newAlterator
      newBoard[row - 1][col].alterator = newAlterator
      newBoard[row][col].alterator = newAlterator
    }
    if (newAlterator === alterator.directioner_down) {
      newBoard[row + 2][col].alterator = newAlterator
      newBoard[row + 1][col].alterator = newAlterator
      newBoard[row][col].alterator = newAlterator
    }
    if (newAlterator === alterator.directioner_right) {
      newBoard[row][col + 2].alterator = newAlterator
      newBoard[row][col + 1].alterator = newAlterator
      newBoard[row][col].alterator = newAlterator
    }
    if (newAlterator === alterator.directioner_left) {
      newBoard[row][col - 2].alterator = newAlterator
      newBoard[row][col - 1].alterator = newAlterator
      newBoard[row][col].alterator = newAlterator
    }
  }

  const updateBoard = (row, col) => {
    if (newAlterator === null) return
    if (board[row][col].alterator !== null || board[row][col].modifier !== null) return
    if (row <= data2.green_ovni_range.x && col <= data2.green_ovni_range.y) return
    if (row >= data2.blue_ovni_range.x && col >= data2.blue_ovni_range.y) return
    const newBoard = [...board]

    setAlteratorInCell(row, col, newAlterator, newBoard)

    setBoard(newBoard)
    console.log(board)
  }

  return (
    <section className='board'>
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
                    greenBase={data2.green_ovni_range}
                    blueBase={data2.blue_ovni_range}
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

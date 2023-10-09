import data2 from "./data2.json"
import {Cell} from "./Cell"
import { useState } from "react"

export const Board = ({alterator}) => {
    const [board, setBoard] = useState(data2.grid)
    
    const updateBoard = (row, col) => {
        if (alterator === null) return
        if (board[row][col].alterator !== null) return
        if (board[row][col].modifier !== null ) return
        const newBoard = [...board]
      
        
        newBoard[row][col].alterator =  alterator
        
        setBoard(newBoard)
        console.log(board)
      }
      
    return (
    <section className="board">
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
                    green_base={data2.green_ovni_range}
                    blue_base={data2.blue_ovni_range}>
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
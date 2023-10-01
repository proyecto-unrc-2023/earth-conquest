import { useState } from "react"

//futuro componente celda
const Cell = ({ updateBoard, alien, row, col, elem }) => {
  const handleClick = () => {
    updateBoard(row, col, elem);
  }

  return (
    <div onClick={handleClick} className="cell" row={row} col={col}>
      {elem && 
        <Alien/>
      }
    </div>
  )
}

const Alien = () => {
  //const className = `${hayAlien ? 'alien' : ''}`
  return (
    <div className="alien"/>
  )
}

function App() {

  const [winner, setWinner] = useState(null)
  const [alien, setAlien] = useState(false)
  
  const grid = [Array(3).fill(false),
                Array(3).fill(false),
                Array(3).fill(false)]
  
  const [board, setBoard] = useState(grid)
  console.log(board)
  
  const updateBoard = (row, col, elem) => {
    console.log(board)
    const newBoard = [...board]
    newBoard[row][col] = !elem
    console.log(board)
    setBoard(newBoard)
  }

  return (
    <>
      <h1>Earth conquest</h1>
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
                    elem={board[i][j]}
                    updateBoard={updateBoard}>
                      {cell}
                  </Cell>
                  )
                })
            )
          })
        }
      </section>
      <section className="modifiers">
        
      </section>
    </>
  )
}

export default App

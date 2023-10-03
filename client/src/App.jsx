import { useState } from "react"
import data from "./data.json"
import {modifier} from "./constants.js"



//leer el js 
console.log(data.grid)

//futuro componente celda
const Cell = ({ updateBoard, aliens, row, col, elem, cell_modifier }) => {
  const handleClick = () => {
    updateBoard(row, col, alien);
  }

  const checkContent = () => {
    if (aliens.length !== 0) {
      return("Alien")
      
    } else if (cell_modifier === "modifier.mountain"){
      return("Modifier")
    }
  }

  return (
    <div onClick={handleClick} className="cell" row={row} col={col}>
      <{
        checkContent
      }/>
    </div>
  )

}

const Alien = () => {
  //const className = `${hayAlien ? 'alien' : ''}`
  return (
    <div className="alien"/>
  )
}

const Modifier = () => {
  //const className = `${hayAlien ? 'alien' : ''}`
  return (
    <div> M </div>
  )
}

function App() {

  const [winner, setWinner] = useState(null)
  const [alien, setAlien] = useState(false)
  
  
  const [board, setBoard] = useState(data.grid)
  
  const updateBoard = (row, col, elem) => {
    const newBoard = [...board]
    newBoard[row][col] = !elem
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
                    aliens={cell.aliens}
                    cell_modifier={cell.modifier}
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
        <h1>Modificadores</h1>
        
      </section>
    </>
  )
}

export default App

import { useState } from "react"
import data from "./data.json"
import {modifier} from "./constants.js"



//leer el js 
console.log(data.grid)

//futuro componente celda
const Cell = ({ updateBoard, aliens, row, col, elem, cell_modifier, cell_alterator}) => {
  const handleClick = () => {
    updateBoard(row, col, alien);
  }

  return(
   <div className="cell" row={row} col={col}>
      { 
        <Content aliens={aliens} cell_modifier={cell_modifier} cell_alterator={cell_alterator}/>
      }
    </div>
  )

}

const Content = ({ aliens, cell_modifier, cell_alterator}) =>{

  if (aliens.length !== 0) {
    return(
    <Alien/>
    )
    
  } 
  if (cell_modifier === "modifier.mountain"){
    return(
    <Modifier/>
    )
  }

  if (cell_alterator === null){
    return(
    <Alterator/>
    )
  }
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

const Alterator = () => {
  //const className = `${hayAlien ? 'alien' : ''}`
  return (
    <div> A </div>
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
                    cell_alterator={cell.alterator}
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

import { useState } from "react"
import data from "./data.json"
import {alterator, modifier} from "./constants.js"



//leer el js 
console.log(data.grid)

//futuro componente celda
const Cell = ({ updateBoard, row, col, children}) => {
  const handleClick = () => {
    updateBoard(row, col);
  }

  return(
   <div onClick={handleClick} className="cell" row={row} col={col}>
      { 
        <Content aliens={children.aliens} cell_modifier={children.modifier} cell_alterator={children.alterator}/>
      }
      
    </div>
  )

}



const Content = ({ aliens, cell_modifier, cell_alterator}) =>{
  return (
    <>
      {
        cell_modifier &&
        <Modifier/>   
      }
      {          
       aliens.map((alien, index) => {
        return(
          <Alien key={index}></Alien>
        )
       })
      }
      { cell_alterator && <Alterator/> }
  </>
  )
}


const Alien = () => {
  //const className = `${hayAlien ? 'alien' : ''}`
  return (
    <>
      <div className="alien">
        <div className="oneEye"/>
        <div className="oneEye"/>
      </div>
    </>
  )
}

const Modifier = () => {
  return (
    //<div className="modifier"/>
    <div> M </div>
  )
}

const Alterator = ({setAlter}) => {
  //agrega un alterador seleccionado por el usuario, para despues setearlo al tablero
  const agregarAlt = () => {
    setAlter(alterator.trap)
  }

  return (
    <div className="alterator" onClick={agregarAlt}> A </div>
  )
}




function App() {

  const [winner, setWinner] = useState(null)
  const [alien, setAlien] = useState(false)
  const [alterator, setAlterator] = useState(null)
  
  //setea el board con la grilla del JSON
  const [board, setBoard] = useState(data.grid)
  
  const setAlter = (newAlterator) => {
    setAlterator(newAlterator)
  }

  const updateBoard = (row, col) => {
    if (alterator === null) return
    if (board[row][col].alterator !== null) return
    if (board[row][col].modifier !== null ) return
    const newBoard = [...board]
  
    
    newBoard[row][col].alterator =  alterator
    
    setBoard(newBoard)
    console.log(board)
  }

  

  console.log(alterator)
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
        <h1>Alteradores</h1> 
        <div className="alter"> <Alterator setAlter={setAlter} /> </div>
        
      </section>
    </>
    //TODO: como seleccionar diferentes alteradores y pasarlo como parametros
  )
}

export default App

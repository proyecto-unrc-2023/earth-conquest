import { useState } from "react"
import data from "./data.json"
import {alterator, modifier} from "./constants.js"

//leer el js 
console.log(data.grid)

//futuro componente celda
const Cell = ({ updateBoard, row, col, children }) => {
  const handleClick = () => {
    updateBoard(row, col);
  }

  return(
   <div onClick={handleClick} className="cell" row={row} col={col}>
      {<>
        {
          children.modifier &&
          <Modifier/>   
        }
        
        {          
          children.aliens.map((alien, index) => {
          return(
            <Alien key={index}></Alien>
          )
        })
        }
        { children.alterator && <Alterator/> }
      </>}
      
    </div>
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

const Panel = ({setAlter}) => {
  
  const handleAlterator = (id) => {
    setAlter(id)
  }
  return (
  <section className="modifiers">
    <h1>Alteradores</h1> 
    <button onClick={()=>handleAlterator("trap")} value={alterator.trap}>Trap</button>
    <button onClick={()=>handleAlterator("teleport")}  value={alterator.teleport}>Teleport</button>
    <button onClick={()=>handleAlterator("directioner")} value={alterator.directioner}>Directioner</button>
    
  </section>

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
      
      <Panel setAlter={setAlter}/>
    </>
    //TODO: como seleccionar diferentes alteradores y pasarlo como parametros
  )
}

export default App

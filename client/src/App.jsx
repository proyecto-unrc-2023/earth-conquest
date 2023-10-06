import { useState } from "react"
import data from "./data.json"
import data2 from "./data2.json"
import {alterator, modifier} from "./constants.js"

//leer el js 
console.log(data2.grid)

//futuro componente celda
const Cell = ({ updateBoard, row, col, children, blue_base, green_base }) => {
  const handleClick = () => {
    updateBoard(row, col);
  }

  return(
   <div onClick={handleClick} className="cell" row={row} col={col}>
      {<>
        {
          children.modifier && <Modifier type={children.modifier}/>   
        }
        
        {          
          children.aliens.map((alien, index) => {
          return(
            <Alien key={index} color={alien.team}></Alien>
          )
        })
        }

        { children.alterator && <Alterator tipo={children.alterator}/> }

        {
          (row <= blue_base.x && col <= blue_base.y ) && <Base/>   
        }
        {
          (row >= green_base.x && col >= green_base.y) && <Base/>   
        }
      </>}
      
    </div>
  )
}

const Base = () => {
  return (
    <div className="Base"> Base</div>
  )
}

const Alien = ({color}) => {
  if (color === "blue"){
    return (
      <div className="alien">
        <img src={"../public/blue_alien.png"} className="img_blue_alien" alt="" />
      </div>
    )
  } else {
    return (
      <div className="alien">
        <img src={"../public/green_alien.png"} className="img_green_alien" alt="" />
      </div>
    )
  }
}

const Modifier = ({type}) => {
  if(type === modifier.mountain){
    return (
      <div className="modifier"> 
        <img src={"../public/mountain.png"} className="img_mountain" alt="" />
      </div>
    )
  }
  if(type === modifier.killer){
    return (
      <div className="modifier"> 
        <img src={"../public/killer.png"} className="img_killer" alt="" />
      </div>
    )
  }
  if(type === modifier.multiplier){
    return (
      <div className="modifier"> 
        <img src={"../public/multiplier.png"} className="img_multiplier" alt="" />
      </div>
    )
  }
}

const Alterator = ({setAlter, tipo}) => {
  //agrega un alterador seleccionado por el usuario, para despues setearlo al tablero
  const agregarAlt = () => {
    setAlter(tipo)
  }

  if(tipo === alterator.trap){
    return (
      <div className="alterator" onClick={agregarAlt}> 
        <img src={"../public/trap.png"} className="img_trap" alt="" />
      </div>
    )
  }
  if(tipo === alterator.directioner){
    return (
      <div className="alterator" onClick={agregarAlt}> 
        <img src={"../public/directioner.png"} className="img_directiorer" alt="" />
      </div>
    )
  }
  if(tipo === alterator.teleport){
    return (
      <div className="alterator" onClick={agregarAlt}> 
        <img src={"../public/teleporter.gif"} className="img_teleporter" alt="" />
      </div>
    )
  }
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
  const [board, setBoard] = useState(data2.grid)
  
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
      
      <Panel setAlter={setAlter}/>
    </>
    //TODO: como seleccionar diferentes alteradores y pasarlo como parametros
  )
}

export default App

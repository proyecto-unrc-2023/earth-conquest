import { useState } from "react"
import data2 from "./data2.json"
import {Board} from "./Board"
import {Panel} from "./Panel"

//leer el js 
console.log(data2.grid)


function App() {

  const [alterator, setAlterator] = useState(null)
    
  const setAlter = (newAlterator) => {
    setAlterator(newAlterator)
  }

  
  console.log(alterator)
  return (
    <>
      <h1>Earth conquest</h1>
      <Board alterator={alterator}/> 
      
      <Panel setAlter={setAlter}/>
    </>
  )
}

export default App

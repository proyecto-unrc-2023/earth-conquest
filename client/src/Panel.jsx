import {alterator} from "./constants.js"

export const Panel = ({setAlter}) => {

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
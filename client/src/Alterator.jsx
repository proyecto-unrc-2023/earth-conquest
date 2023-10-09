import {alterator} from "./constants.js"


export const Alterator = ({setAlter, tipo}) => {
    const agregarAlt = () => {
      setAlter(tipo)
    }
  
    return (    
      <div className="alterator" onClick={agregarAlt}> 
        {
          (tipo === alterator.trap) && <img src={"../public/trap.png"} className="img_trap" alt="" />
        }
        {
          (tipo === alterator.directioner) &&  <img src={"../public/directioner.png"} className="img_directiorer" alt="" />
        }
        {
          (tipo === alterator.teleport) && <img src={"../public/teleporter.gif"} className="img_teleporter" alt="" />
        }
      </div>
    )
  }
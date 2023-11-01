import { alterator } from '../../constants.js'
import './Alterator.css'

export const Alterator = ({ setAlter, tipo }) => {
  const agregarAlt = () => {
    setAlter(tipo)
  }

  return (
    <div className='alterator' onClick={agregarAlt}>
      {
        (tipo === alterator.trap) && <img src='../public/trap.png' className='img_trap' alt='' />
      }
      {
        (tipo === alterator.directioner_up) && <img src='../public/directioner_up.png' className='img_directioner' alt='' />
      }
      {
        (tipo === alterator.directioner_down) && <img src='../public/directioner_down.png' className='img_directioner' alt='' />
      }
      {
        (tipo === alterator.directioner_left) && <img src='../public/directioner_left.png' className='img_directioner' alt='' />
      }
      {
        (tipo === alterator.directioner_right) && <img src='../public/directioner_right.png' className='img_directioner' alt='' />
      }
      {
        (tipo === alterator.teleporter_in) && <img src='../public/teleport_in.gif' className='img_teleporter' alt='' />
      }
      {
        (tipo === alterator.teleporter_out) && <img src='../public/teleport_out.gif' className='img_teleporter' alt='' />
      }
    </div>
  )
}

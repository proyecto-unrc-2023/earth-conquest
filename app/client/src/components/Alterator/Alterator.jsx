import { alterator } from '../../constants.js'
import './Alterator.css'

export const Alterator = ({ tipo }) => {
  return (
    <div className='alterator'>
      {
        (tipo === alterator.TRAP) && <img src='../trap.png' className='img_trap' alt='' />
      }
      {
        (tipo === alterator.DIRECTIONER_UPWARDS) && <img src='../directioner_up.png' className='img_directioner' alt='' />
      }
      {
        (tipo === alterator.DIRECTIONER_DOWNWARDS) && <img src='../directioner_down.png' className='img_directioner' alt='' />
      }
      {
        (tipo === alterator.DIRECTIONER_LEFT) && <img src='../directioner_left.png' className='img_directioner' alt='' />
      }
      {
        (tipo === alterator.DIRECTIONER_RIGHT) && <img src='../directioner_right.png' className='img_directioner' alt='' />
      }
      {
        (tipo === alterator.TELEPORTER_IN) && <img src='../teleport_in.gif' className='img_teleporter' alt='' />
      }
      {
        (tipo === alterator.TELEPORTER_OUT) && <img src='../teleport_out.gif' className='img_teleporter' alt='' />
      }
    </div>
  )
}

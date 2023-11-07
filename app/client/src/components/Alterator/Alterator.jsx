import { alterator } from '../../constants.js'
import './Alterator.css'

export const Alterator = ({ tipo }) => {
  return (
    <div className='alterator'>
      {
        (tipo === alterator.TRAP) && <img src='../public/trap.png' className='img_trap' alt='' />
      }
      {
        (tipo === alterator.DIRECTIONER_UP) && <img src='../public/directioner_up.png' className='img_directioner' alt='' />
      }
      {
        (tipo === alterator.DIRECTIONER_DOWN) && <img src='../public/directioner_down.png' className='img_directioner' alt='' />
      }
      {
        (tipo === alterator.DIRECTIONER_LEFT) && <img src='../public/directioner_left.png' className='img_directioner' alt='' />
      }
      {
        (tipo === alterator.DIRECTIONER_RIGHT) && <img src='../public/directioner_right.png' className='img_directioner' alt='' />
      }
      {
        (tipo === alterator.TELEPORTER_IN) && <img src='../public/teleport_in.gif' className='img_teleporter' alt='' />
      }
      {
        (tipo === alterator.TELEPORTER_OUT) && <img src='../public/teleport_out.gif' className='img_teleporter' alt='' />
      }
    </div>
  )
}

import { alterator } from '../../constants.js'
import './Alterator.css'

export const Alterator = ({ tipo }) => {
  return (
    <div className='alterator'>
      {
        (tipo === alterator.TRAP) && <img src='../trap.png' className='img_trap' alt='' />
      }
      {
        (tipo === alterator.TELEPORTER_IN) && <img src='../teleport_in.gif' className='img_teleporter' alt='' />
      }
      {
        (tipo === alterator.TELEPORTER_OUT) && <img src='../teleport_out.gif' className='img_teleporter' alt='' />
      }
      {
        (tipo.name === 'DIRECTIONER' && tipo.direction === 'UPWARDS') && <img src='../directioner_up.png' className='img_directioner' alt='' />
      }
      {
        (tipo.name === 'DIRECTIONER' && tipo.direction === 'DOWNWARDS') && <img src='../directioner_down.png' className='img_directioner' alt='' />
      }
      {
        (tipo.name === 'DIRECTIONER' && tipo.direction === 'LEFT') && <img src='../directioner_left.png' className='img_directioner' alt='' />
      }
      {
        (tipo.name === 'DIRECTIONER' && tipo.direction === 'RIGHT') && <img src='../directioner_right.png' className='img_directioner' alt='' />
      }
    </div>
  )
}

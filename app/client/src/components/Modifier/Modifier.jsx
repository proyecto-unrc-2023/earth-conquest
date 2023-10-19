import { modifier } from '../../constants.js'
import './Modifier.css'

export const Modifier = ({ type }) => {
  return (
    <div className='modifier'>
      {
          (type === modifier.mountain) && <img src='../public/mountain.png' className='img_mountain' alt='' />
        }
      {
          (type === modifier.killer) && <img src='../public/killer.png' className='img_killer' alt='' />
        }
      {
          (type === modifier.multiplier) && <img src='../public/multiplier.png' className='img_multiplier' alt='' />
        }
    </div>
  )
}

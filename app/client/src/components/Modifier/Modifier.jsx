import { modifier } from '../../constants.js'
import './Modifier.css'

export const Modifier = ({ type }) => {
  const t = type.toLowerCase()
  return (
    <div className='modifier'>
      {
          (t === modifier.mountain_range) && <img src='../public/mountain.png' className='img_mountain' alt='' />
        }
      {
          (t === modifier.killer) && <img src='../public/killer.png' className='img_killer' alt='' />
        }
      {
          (t === modifier.multiplier) && <img src='../public/multiplier.png' className='img_multiplier' alt='' />
        }
    </div>
  )
}

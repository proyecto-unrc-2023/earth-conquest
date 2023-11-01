import { modifier } from '../../constants.js'
import './Modifier.css'

export const Modifier = ({ type }) => {
  const typeLower = type.toLowerCase()
  return (
    <div className='modifier'>
      {
          (typeLower === modifier.mountain_range) && <img src='../public/mountain.png' className='img_mountain' alt='' />
        }
      {
          (typeLower === modifier.killer) && <img src='../public/killer.png' className='img_killer' alt='' />
        }
      {
          (typeLower === modifier.multiplier) && <img src='../public/multiplier.png' className='img_multiplier' alt='' />
        }
    </div>
  )
}

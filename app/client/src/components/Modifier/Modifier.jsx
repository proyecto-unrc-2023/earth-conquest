import { modifier } from '../../constants.js'
import './Modifier.css'

export const Modifier = ({ type }) => {
  return (
    <div className='modifier'>
      {
          (type === modifier.MOUNTAIN_RANGE) && <img src='../public/mountain.png' className='img_mountain' alt='' />
        }
      {
          (type === modifier.KILLER) && <img src='../public/killer.png' className='img_killer' alt='' />
        }
      {
          (type === modifier.MULTIPLIER) && <img src='../public/multiplier.png' className='img_multiplier' alt='' />
        }
    </div>
  )
}

import { Alien } from '../Alien/Alien'
import { Modifier } from '../Modifier/Modifier'
import { Alterator } from '../Alterator/Alterator'
import { team } from '../../constants.js'
import './Cell.css'

export const Cell = ({ updateBoard, row, col, children, blueBase, greenBase, permiso, teleportX, teleportY, isTeleportRange, isBase }) => {
  const handleClick = () => {
    updateBoard(row, col)
  }

  let className = 'cell '

  if (!permiso && isTeleportRange(row, col, teleportX, teleportY)) {
    className += 'grey'
  } else {
    if (isBase(row, col, greenBase.x, greenBase.y, team.green)) {
      className += 'green'
    }
    if (isBase(row, col, blueBase.x, blueBase.y, team.blue)) {
      className += 'blue'
    }
  }

  return (
    <div onClick={handleClick} className={className} row={row} col={col}>
      {
        children.modifier && <Modifier type={children.modifier} />
      }

      {
        children.aliens.map((alien, index) => {
          return (
            <Alien key={index} team={alien.team} eyes={alien.eyes} />
          )
        })
      }

      {children.alterator && <Alterator tipo={children.alterator} />}
      {
          (row === 0 && col === 0) && <img src='../public/green_ovni.png' className='green_nave' />
        }
      {
          (row === 9 && col === 14) && <img src='../public/blue_ovni.png' className='blue_nave' />
        }
    </div>
  )
}

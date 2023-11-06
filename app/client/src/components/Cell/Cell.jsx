import { Alien } from '../Alien/Alien'
import { Modifier } from '../Modifier/Modifier'
import { Alterator } from '../Alterator/Alterator'
import { team } from '../../constants.js'
import './Cell.css'

export const Cell = ({ updateBoard, row, col, children, blueBase, greenBase, teleporterEnabled, teleportX, teleportY, outOfTeleportRange, isBase }) => {
  const handleClick = () => {
    updateBoard(row, col)
  }

  let className = 'cell '

  if (!teleporterEnabled && outOfTeleportRange(row, col, teleportX, teleportY)) {
    className += 'grey'
  } else {
    if (isBase(row, col, greenBase[0], greenBase[1], team.green)) {
      className += 'green'
    }
    if (isBase(row, col, blueBase[0], blueBase[1], team.blue)) {
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

import { Alien } from '../Alien/Alien'
import { Modifier } from '../Modifier/Modifier'
import { Alterator } from '../Alterator/Alterator'
import { team, alterator } from '../../constants.js'
import './Cell.css'

export const Cell = ({ aliensDirections, updateBoard, row, col, children, blueBase, greenBase, teleportX, teleportY, teleporterEnabled, teleportIn, teleportOut, outOfTeleportRange, isBase }) => {
  const isTeleportIn = (x, y) => {
    return (
      teleportIn.find(teleport => teleport.row === x && teleport.col === y) !== undefined
    )
  }

  const isTeleportOut = (x, y) => {
    return (

      teleportOut.find(teleport => teleport.row === x && teleport.col === y) !== undefined
    )
  }

  const handleClick = () => {
    updateBoard(row, col)
  }

  let className = 'cell '

  if (!teleporterEnabled && outOfTeleportRange(row, col, teleportX, teleportY)) {
    className += 'grey'
  } else {
    if (!teleporterEnabled && teleportX === row && teleportY === col) {
      className += 'in'
    }
    if (isBase(row, col, greenBase[0], greenBase[1], team.GREEN)) {
      className += 'green'
    }
    if (isBase(row, col, blueBase[0], blueBase[1], team.BLUE)) {
      className += 'blue'
    }
  }

  return (
    <div onClick={handleClick} className={className} row={row} col={col}>
      {
        children.modifier && <Modifier type={children.modifier} />
      }

      {
        children.aliens.map((alien) => {
          const alienDirection = aliensDirections[alien.id]
          return (
            <Alien key={alien.id} id={alien.id} team={alien.team} eyes={alien.eyes} direction={alienDirection} />
          )
        })
      }
      {
        children.alterator &&
        isTeleportIn(row, col) &&
          <Alterator tipo={alterator.TELEPORTER_IN} />
      }

      {
        children.alterator &&
        isTeleportOut(row, col) &&
          <Alterator tipo={alterator.TELEPORTER_OUT} />
      }

      {
        children.alterator && !isTeleportOut(row, col) && !isTeleportIn(row, col) &&
          <Alterator tipo={children.alterator} />
      }

      {
        (row === 0 && col === 0) && <img src='../green_ovni.png' className='green_nave' />
      }
      {
        (row === 9 && col === 14) && <img src='../blue_ovni.png' className='blue_nave' />
      }
    </div>
  )
}

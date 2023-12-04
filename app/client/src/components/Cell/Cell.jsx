import { Alien } from '../Alien/Alien'
import { Modifier } from '../Modifier/Modifier'
import { Alterator } from '../Alterator/Alterator'
import { team, alterator } from '../../constants.js'
import './Cell.css'

export const Cell = ({ updateBoard, row, col, children, blueBase, greenBase, teleportX, teleportY, teleporterEnabled, teleportIn, teleportOut, outOfTeleportRange, isBase }) => {
  // Funcion para ver si un par es entrada de un teleport
  const isTeleportIn = (x, y) => {
    return (
      teleportIn.find(teleport => teleport.row === x && teleport.col === y) !== undefined
    )
  }

  // Funcion para ver si un par es salida de un teleport
  const isTeleportOut = (x, y) => {
    return (
      teleportOut.find(teleport => teleport.row === x && teleport.col === y) !== undefined
    )
  }

  // Actualiza el tablero
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
          return (
            <Alien key={alien.id} team={alien.team} eyes={alien.eyes} />
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

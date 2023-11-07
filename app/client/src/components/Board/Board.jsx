import { Cell } from '../Cell/Cell'
import { alterator, team } from '../../constants.js'
import './Board.css'
import { useState } from 'react'

export const Board = ({ board, setBoard, teamPlayer, newAlterator, setAlter, setTeleporterEnabled, teleporterEnabled, gameId, blueOvniRange, greenOvniRange }) => {
  const FREE_POSITION = 'http://127.0.0.1:5000/games/is_free_position' // verificar
  const SEND_ALTERATOR = 'http://127.0.0.1:5000/games/set_alterator' // verificar
  const [teleportX, setTeleportX] = useState(null)
  const [teleportY, setTeleportY] = useState(null)
  const TELEPORT_RANGE = 4

  // Funcion para dar el rango de teleport
  const outOfTeleportRange = (row, col, x, y) => {
    return (Math.abs(row - x) >= TELEPORT_RANGE || Math.abs(col - y) >= TELEPORT_RANGE)
  }

  // Funcion para dar el rango de la base segun el team
  const isBase = (row, col, x, y, teamBase) => {
    if (teamBase === team.GREEN) {
      return (row <= x && col <= y)
    } else {
      return (row >= x && col >= y)
    }
  }

  const updateBoard = async (row, col) => {
    if (newAlterator === null) return
    if (!await isFreePosition(row, col)) return
    if (
      (outOfTeleportRange(row, col, teleportX, teleportY) &&
      (isBase(row, col, greenOvniRange[0], greenOvniRange[1], team.GREEN) ||
      isBase(row, col, blueOvniRange[0], blueOvniRange[1], team.BLUE)))
    ) return
    if (outOfTeleportRange(row, col, teleportX, teleportY) && (newAlterator === alterator.TELEPORTER_OUT)) return

    const newBoard = [...board]
    setAlteratorInCell(row, col, newAlterator, newBoard)
    setBoard(newBoard) // ACA NO IRIA SINO QUE ESTA CONTEMPLADO EN EL SSE.ONMESSAJE
  }

  const sendAlterator = async (newAlterator) => {
    try {
      const response = await fetch(`${SEND_ALTERATOR}/${gameId}`, {
        method: 'PUT',
        body: JSON.stringify({ alterator: newAlterator })
      })
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
    } catch (error) {
      console.error('Error set alterator', error)
    }
  }

  const isFreePosition = async (row, col) => {
    try {
      const response = await fetch(`${FREE_POSITION}/${gameId}?x=${row}&y=${col}`)
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()
      return (data.success)
    } catch (error) {
      console.error('Error is valid position', error)
    }
  }

  const setAlteratorInCell = async (row, col, newAlterator, newBoard) => {
    console.log('Entre al setAlterator')
    if (await isFreePosition(row, col)) {
      console.log('entre a una posicion free')
      if (newAlterator === alterator.TRAP) {
        console.log('entre a una trampa')
        const newTrap = {
          name: newAlterator,
          positionInit: { x: row, y: col },
          positionEnd: null,
          direction: null,
          team: teamPlayer
        }
        await sendAlterator(row, col, newTrap)
      } else {
        const alteratorSplit = newAlterator.split('_')
        const alteratorName = alteratorSplit[0]
        const alteratorDirection = alteratorSplit[1]

        if (alteratorName === 'DIRECTIONER') {
          console.log('entre a un directioner')
          const newDirectioner = {
            name: alteratorName,
            positionInit: { x: row, y: col },
            positionEnd: null,
            direction: alteratorDirection,
            team: teamPlayer
          }
          await sendAlterator(row, col, newDirectioner)
        } else if (alteratorName === 'TELEPORTER') {
          console.log('entre a un teleporter')
          const newTeleport = {
            name: alteratorName,
            positionInit: { x: row, y: col },
            positionEnd: null,
            direction: alteratorDirection,
            team: teamPlayer
          }
          if (alteratorDirection === 'IN') {
            newBoard[row][col].alterator = newAlterator
            // cambia estado a teleport out
            setAlter(alterator.TELEPORTER_OUT)
            setTeleporterEnabled(false)
            setTeleportX(row)
            setTeleportY(col)
          } else {
            newTeleport.positionEnd.x = row
            newTeleport.positionEnd.y = col
            await sendAlterator(row, col, newTeleport)
            setAlter(null)
            setTeleporterEnabled(true)
          }
        }
      }
    }
  }
  return (
    <section className='board'>
      {
        board.map((row, i) => {
          return (
            row.map((cell, j) => {
              return (
                <Cell
                  key={j}
                  col={j}
                  row={i}
                  updateBoard={updateBoard}
                  greenBase={greenOvniRange}
                  blueBase={blueOvniRange}
                  teleporterEnabled={teleporterEnabled}
                  teleportX={teleportX}
                  teleportY={teleportY}
                  isBase={isBase}
                  outOfTeleportRange={outOfTeleportRange}
                >
                  {cell}
                </Cell>
              )
            })
          )
        })
      }
    </section>
  )
}

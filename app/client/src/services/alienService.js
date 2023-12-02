/*
* Esta función toma el hash de celdas, y el board del comienzo
* de la partida.
* Actualiza el board con la informacion del hash.
*/

export const handleHash = (cells, newBoard, setTeleportIn, setTeleportOut) => {
  const copyBoard = structuredClone(newBoard)
  const teleportInList = []
  const teleportOutList = []

  Object.entries(cells).forEach(([position, cell]) => {
    const [row, col] = position.slice(1, -1).split(', ').map(Number)
    if (cell.alterator !== null && cell.alterator.name === 'TELEPORTER') {
      const [x, y] = cell.alterator.door_pos
      const [a, b] = cell.alterator.exit_pos
      teleportInList.push({ row: x, col: y })
      teleportOutList.push({ row: a, col: b })
    }

    copyBoard[row][col] = cell
  })

  if (teleportInList.length > 0 && teleportOutList.length > 0) {
    setTeleportIn(teleportInList)
    setTeleportOut(teleportOutList)
  }

  return copyBoard
}

export const handleAliens = (aliens, cells) => {
  const newAliens = [...aliens]
  if (newAliens.length === 0) {
    return initAliens(newAliens, cells)
  } else {
    return updateAliensPositions(newAliens, cells)
  }
}

/*
 * Inicia la lista de aliens con la informacion del hash.
*/
export const initAliens = (aliens, cells) => {
  Object.entries(cells).forEach(([position, cell]) => {
    const [row, col] = position.slice(1, -1).split(', ').map(Number)
    cell.aliens.forEach((alien) => {
      aliens.push({ id: alien.id, oldPosition: { row, col }, newPosition: { row, col } })
    })
  })
  return aliens
}

/*
 * Actualiza la lista de aliens con la informacion del hash.
*/
const updateAliensPositions = (aliens, cells) => {
  Object.entries(cells).forEach(([position, cell]) => {
    const [row, col] = position.slice(1, -1).split(', ').map(Number)
    cell.aliens.forEach((cellAlien) => {
      const alien = aliens.find(alien => alien.id === cellAlien.id)

      if (alien) {
        alien.oldPosition = { row: alien.newPosition.row, col: alien.newPosition.col }
        alien.newPosition = { row, col }
        aliens.filter(alien => alien.id !== cellAlien.id)
      }
    })
  })
  return aliens
}

/*
* Toma el arreglo de aliens, con posiciones antiguas y nuevas, y devuelve un
* arreglo de id con la direccion.
*/

export const getAliensDirections = (aliens) => {
  return aliens.map(alien => {
    let direction

    if (alien.oldPosition.row < alien.newPosition.row) {
      direction = 'down'
    } else if (alien.oldPosition.row > alien.newPosition.row) {
      direction = 'up'
    } else if (alien.oldPosition.col < alien.newPosition.col) {
      direction = 'right'
    } else if (alien.oldPosition.col > alien.newPosition.col) {
      direction = 'left'
    } else {
      direction = 'none'
    }
    return { id: alien.id, direction }
  })
}

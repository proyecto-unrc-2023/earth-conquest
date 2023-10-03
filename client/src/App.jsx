import { useState } from "react"

//enums
const alterator = {
  teleport: 'teleport',
  trap: 'trap',
  directioner: 'directioner'
}
const modifier = {
  killer: 'killer',
  multiplier: 'multiplier',
  mountain: 'mountain'
}

const team = {
  blue: 'blue',
  green: 'green'
}

const gameStatus = {
  started: 'started',
  notStarted: 'notStarted'
}

//Json posible de board
const boardJson = [
  [
    {
      aliens: [
        {
          id: null,
          eyes: 1,
          team: team.blue,
        }
      ],
      alterator: alterator.trap,
      modifier: modifier.mountain,
    },
    {
      aliens: [
        {
          id: null,
          eyes: 1,
          team: team.blue,
        }
      ],
      alterator: alterator.trap,
      modifier: modifier.mountain,
    },
    {
      aliens: [
        {
          id: null,
          eyes: 1,
          team: team.blue,
        }
      ],
      alterator: alterator.trap,
      modifier: modifier.mountain,
    },
    {
      aliens: [
        {
          id: null,
          eyes: 1,
          team: team.blue,
        }
      ],
      alterator: alterator.trap,
      modifier: modifier.mountain,
    },
    {
      aliens: [
        {
          id: null,
          eyes: 1,
          team: team.blue,
        }
      ],
      alterator: alterator.trap,
      modifier: modifier.mountain,
    }
  ]
]
console.log(boardJson)

//futuro componente celda
const Cell = ({ updateBoard, alien, row, col, elem }) => {
  const handleClick = () => {
    updateBoard(row, col, elem);
  }

  return (
    <div onClick={handleClick} className="cell" row={row} col={col}>
      {elem && 
        <Alien/>
      }
    </div>
  )
}

const Alien = () => {
  //const className = `${hayAlien ? 'alien' : ''}`
  return (
    <div className="alien"/>
  )
}

function App() {

  const [winner, setWinner] = useState(null)
  const [alien, setAlien] = useState(false)
  
  const grid = [Array(3).fill(false),
                Array(3).fill(false),
                Array(3).fill(false)]
  
  const [board, setBoard] = useState(grid)
  console.log(board)
  
  const updateBoard = (row, col, elem) => {
    const newBoard = [...board]
    newBoard[row][col] = !elem
    setBoard(newBoard)
  }

  return (
    <>
      <h1>Earth conquest</h1>
      <section className="board">
        {
          board.map((row, i) => {
            return (
                row.map((cell, j) => {
                  return (
                  <Cell 
                    key={j}
                    col={j}
                    row={i}
                    elem={board[i][j]}
                    updateBoard={updateBoard}>
                      {cell}
                  </Cell>
                  )
                })
            )
          })
        }
      </section>
      <section className="modifiers">
        
      </section>
    </>
  )
}

export default App

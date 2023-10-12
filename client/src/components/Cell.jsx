import { Alien } from './Alien'
import { Modifier } from './Modifier'
import { Alterator } from './Alterator'

export const Cell = ({ updateBoard, row, col, children, blueBase, greenBase }) => {
  const handleClick = () => {
    updateBoard(row, col)
  }

  let className = 'cell '

  if (row <= greenBase.x && col <= greenBase.y) {
    className += 'green'
  }

  if (row >= blueBase.x && col >= blueBase.y) {
    className += 'blue'
  }

  return (
    <div onClick={handleClick} className={className} row={row} col={col}>
      <>
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

        <div />

        {
            ((row === 0 && col === 0) && <img src='../public/green_ovni.png' className='green_nave' />)
          }
        {
            ((row === 9 && col === 14) && <img src='../public/blue_ovni.png' className='blue_nave' />)
          }
      </>
    </div>
  )
}

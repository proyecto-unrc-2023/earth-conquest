import {Alien} from "./Alien"
import { Modifier } from "./Modifier";
import { Alterator } from "./Alterator";


export const Cell = ({ updateBoard, row, col, children, blue_base, green_base }) => {
  const handleClick = () => {
    updateBoard(row, col);
  }

  let className = "cell "

  if(row <= green_base.x && col <= green_base.y ){
    className += "green"
  }

  if (row >= blue_base.x && col >= blue_base.y) {
    className += "blue"
  }

  return(
   <div onClick={handleClick} className={className} row={row} col={col}>
      {
        <>
          {
            children.modifier && <Modifier type={children.modifier}/>   
          }
          
          {          
            children.aliens.map((alien, index) => {
            return(
              <Alien key={index} team={alien.team} eyes={alien.eyes}></Alien>
            )
          })
          }

          { children.alterator && <Alterator tipo={children.alterator}/> }

          {
            <div />  
          }

          {
            ((row === 0 && col === 0) && <img src={"../public/green_ovni.png"} className="green_nave" />)
          }
          {
            ((row === 9 && col === 14) && <img src={"../public/blue_ovni.png"} className="blue_nave" />)
          }
        </>
      }
    </div>
  )
}
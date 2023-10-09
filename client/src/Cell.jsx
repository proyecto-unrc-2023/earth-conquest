import {Alien} from "./Alien"
import { Modifier } from "./Modifier";
import { Alterator } from "./Alterator";


export const Cell = ({ updateBoard, row, col, children, blue_base, green_base }) => {
  const handleClick = () => {
    updateBoard(row, col);
  }

  return(
   <div onClick={handleClick} className="cell" row={row} col={col}>
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
            (row <= blue_base.x && col <= blue_base.y ) && <div className="base"> Base</div>   
          }
          {
            (row >= green_base.x && col >= green_base.y) && <div className="base"> Base</div>  
          }
        </>
      }
    </div>
  )
}
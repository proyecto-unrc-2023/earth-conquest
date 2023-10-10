
export const Alien = ({team, eyes}) => {
    return (      
      <div className="alien">
        {((team === "blue") && (eyes === 1)) && <img src={"../public/blue_alien_1.png"} className="img_blue_alien" alt="" />}
        {((team === "blue") && (eyes === 2)) && <img src={"../public/blue_alien_2.png"} className="img_blue_alien" alt="" />}
        {((team === "blue") && (eyes === 3)) && <img src={"../public/blue_alien_3.png"} className="img_blue_alien" alt="" />}
        {((team === "blue") && (eyes === 4)) && <img src={"../public/blue_alien_4.png"} className="img_blue_alien" alt="" />}
        {((team === "blue") && (eyes === 5)) && <img src={"../public/blue_alien_5.png"} className="img_blue_alien" alt="" />}

        {((team === "green") && (eyes === 1)) && <img src={"../public/green_alien_1.png"} className="img_blue_alien" alt="" />}
        {((team === "green") && (eyes === 2)) && <img src={"../public/green_alien_2.png"} className="img_blue_alien" alt="" />}
        {((team === "green") && (eyes === 3)) && <img src={"../public/green_alien_3.png"} className="img_blue_alien" alt="" />}
        {((team === "green") && (eyes === 4)) && <img src={"../public/green_alien_4.png"} className="img_blue_alien" alt="" />}
        {((team === "green") && (eyes === 5)) && <img src={"../public/green_alien_5.png"} className="img_blue_alien" alt="" />}
      </div>
    )
}
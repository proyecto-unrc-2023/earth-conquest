import { alterator } from '../../constants.js'
import { useState } from 'react'
import './Panel.css'

export const Panel = ({ setAlter, teleporterEnabled, team }) => {
  const [showDirections, setShowDirections] = useState(false)
  const [showAlterators, setshowAlterators] = useState(true)
  const teamLower = team.toLowerCase()

  // Setea el alterador para colocar en el tablero
  const handleAlterator = (newAlterator) => {
    if (!teleporterEnabled) return
    setAlter(newAlterator) // setea el objeto
  }

  // Muestra las direcciones del Directioner
  const handleShowDirections = () => {
    setShowDirections(true)
    setshowAlterators(false)
  }

  // Setea las direcciones del Directioner
  const handleDirectionClick = (direction) => {
    setShowDirections(false)
    setshowAlterators(true)
    handleAlterator(direction)
  }

  return (
    <section className='alterators-panel'>
      <h1 className='tittle'>ALTERADORES</h1>
      <section className='buttons'>
        {showAlterators && (
          <>
            <button onClick={() => handleAlterator(alterator.TRAP)}>
              <img className='button_img_trap' src='/../trap.png' alt='Trap' />
              <section className='box-value'>
                <img src={`../${teamLower}_alien.png`} className='alien-value' />
                <p className='value'>4</p>
              </section>
            </button>
            <button onClick={() => handleAlterator(alterator.TELEPORTER_IN)}>
              <section>
                <img className='button_img_teleport1' src='/../teleport_in.gif' alt='Teleporter' />
                <img className='button_img_teleport1' src='/../teleport_out.gif' alt='Teleporter' />
              </section>
              <section className='box-value'>
                <img src={`../${teamLower}_alien.png`} className='alien-value' />
                <p className='value'>6</p>
              </section>
            </button>
            <button onClick={handleShowDirections}>
              <section>
                <img className='button_img_dir1' src='/../directioner_up.png' alt='Directioner' />
                <img className='button_img_dir1' src='/../directioner_right.png' alt='Directioner' />
                <img className='button_img_dir1' src='/../directioner_down.png' alt='Directioner' />
                <img className='button_img_dir1' src='/../directioner_left.png' alt='Directioner' />
              </section>
              <section className='box-value'>
                <img src={`../${teamLower}_alien.png`} className='alien-value' />
                <p className='value'>4</p>
              </section>
            </button>
          </>
        )}
        {showDirections && (
          <div className='type_dir'>
            <button onClick={() => handleDirectionClick(alterator.DIRECTIONER_UPWARDS)}>
              <img className='button_img_dir' src='/../directioner_up.png' alt='Directioner' />
            </button>
            <button onClick={() => handleDirectionClick(alterator.DIRECTIONER_DOWNWARDS)}>
              <img className='button_img_dir' src='/../directioner_down.png' alt='Directioner' />
            </button>
            <button onClick={() => handleDirectionClick(alterator.DIRECTIONER_RIGHT)}>
              <img className='button_img_dir' src='/../directioner_right.png' alt='Directioner' />
            </button>
            <button onClick={() => handleDirectionClick(alterator.DIRECTIONER_LEFT)}>
              <img className='button_img_dir' src='/../directioner_left.png' alt='Directioner' />
            </button>
          </div>
        )}
      </section>
    </section>
  )
}

import './Alien.css'

export const Alien = ({ team, eyes }) => {
  const imagen = `../${team}_alien_${eyes}.png`
  const className = `img_${team}_alien`

  return (
    <div className='alien'>
      <img src={imagen} className={className} alt={className} />
    </div>
  )
}

import './Alien.css'

export const Alien = ({ team, eyes }) => {
  const teamToLower = team.toLowerCase()
  const imagen = `../${teamToLower}_alien_${eyes}.png`
  const className = `img_${teamToLower}_alien`

  return (
    <div className='alien'>
      <img src={imagen} className={className} alt={className} />
    </div>
  )
}

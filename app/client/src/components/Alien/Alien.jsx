import './Alien.css'

export const Alien = ({ team, eyes }) => {
  const teamLower = team.toLowerCase()
  const imagen = `./${teamLower}_alien_${eyes}.png`
  const className = `img_${teamLower}_alien`
  const direction = 'none'

  return (
    <div className={`alien ${direction}`}>
      <img src={imagen} className={className} alt={className} />
    </div>
  )
}

import './Alien.css'

export const Alien = ({ team, eyes, direction, id }) => {
  const teamLower = team.toLowerCase()
  const imagen = `./${teamLower}_alien_${eyes}.png`
  const className = `${id} alien ${direction}`

  return (
    <div className={className}>
      <img src={imagen} className={`img_${teamLower}_alien`} alt={className} />
    </div>
  )
}

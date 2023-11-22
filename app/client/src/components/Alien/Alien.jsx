import './Alien.css'

export const Alien = ({ team, eyes, direction, id }) => {
  const teamLower = team.toLowerCase()
  const imagen = `./${teamLower}_alien_${eyes}.png`
  const className = `${id} alien ${direction}`

  return (
    <div data-testid='alien-container' className={className}>
      <img src={imagen} className={`img_${teamLower}_alien`} alt={className} data-testid='alien-image' />
    </div>
  )
}

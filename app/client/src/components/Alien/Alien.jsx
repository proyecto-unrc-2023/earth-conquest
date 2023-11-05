import './Alien.css'

export const Alien = ({ team, eyes }) => {
  const t = team.toLowerCase()
  const imagen = `../${t}_alien_${eyes}.png`
  const className = `img_${t}_alien`

  return (
    <div className='alien'>
      <img src={imagen} className={className} alt={className} />
    </div>
  )
}

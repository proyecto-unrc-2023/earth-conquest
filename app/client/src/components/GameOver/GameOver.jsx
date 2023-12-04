import './GameOver.css'

export function GameOver ({ game }) {
  const { 0: name, 1: team } = game.winner
  const containerClassName = `game-over container ${team.toLowerCase()}`

  return (
    <div className={containerClassName}>
      <h1>Game Over</h1>
      <p>¡ {name} From The {team} Team Wins !</p>

    </div>
  )
}

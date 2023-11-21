import React from 'react'

export function GameOver ({ game }) {
  console.log('ESTO VIENE EN GAME DE GAME OVER', game.winner)
  const { 0: name, 1: team } = game.winner
  return (
    <div>
      <h1>Game Over</h1>
      <p>¡El ganador es {name} del equipo {team}</p>
    </div>
  )
}

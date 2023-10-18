export const StatsGame = ({ team, lifeOvni, liveAliens }) => {
  return (
    <>
      <section className={`health-bar-${team}`}>
        <div className={`bar-${team}`} style={{ width: `${lifeOvni / 2}%` }} />
        <strong className='text'>{lifeOvni}/200</strong>
      </section>

      <section className={`live_alien_${team}`}>
        <p>Aliens {team} vivos: {liveAliens} </p>
      </section>
    </>
  )
}

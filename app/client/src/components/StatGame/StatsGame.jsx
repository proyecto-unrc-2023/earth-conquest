import './StatsGame.css'

export const StatsGame = ({ team, lifeOvni, liveAliens, playerName }) => {
  return (
    <>
      <section className={`health-bar-${team}`}>
        <div className={`bar-${team}`} style={{ width: `${lifeOvni * 10}%` }} />
        <strong className='text'>{lifeOvni}/10</strong>
      </section>

      <section className={`${team}_user_info`}>

        <section className={`live_alien_${team}`}>
          <img src={`../${team}_alien.png`} className={`${team}_alien`} alt='alien' />
          <p> {liveAliens} </p>
        </section>

        <section className={`${team}_name`}>
          <p>{`${playerName}`}</p>
        </section>

      </section>

    </>
  )
}

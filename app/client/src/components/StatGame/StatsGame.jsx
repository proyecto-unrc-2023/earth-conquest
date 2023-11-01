import './StatsGame.css'

export const StatsGame = ({ team, lifeOvni, liveAliens, playerName }) => {
  return (
    <>
      <section className={`health-bar-${team}`}>
        <div className={`bar-${team}`} style={{ width: `${lifeOvni / 2}%` }} />
        <strong className='text'>{lifeOvni}/200</strong>
      </section>

      <section className={`${team}_user_info`}>

        <section className={`live_alien_${team}`}>
          <img src={`../public/${team}_alien.png`} className={`${team}_alien`} alt='' />
          <p> {liveAliens} </p>
        </section>

        <section className={`${team}_name`}>
          <p style={{ fontFamily: 'PressStart2P' }}>{playerName}</p>
        </section>

      </section>

    </>
  )
}

import './Login.css'

export function Login ({ game, setNameGreen, cuandoSeJoinea, nameGreen, message, playHoverSound }) {
  return (
    <section className='box-login'>
      <label>
        <input
          type='text'
          placeholder='Insert name'
          value={nameGreen}
          onChange={(e) => {
            setNameGreen(e.target.value)
          }}
          className='input'
        />
        <button
          onClick={() => cuandoSeJoinea('GREEN', nameGreen, game.gameId)}
          disabled={!nameGreen}
          onMouseEnter={playHoverSound}
          className='btn'
        >
          Join
        </button>
      </label>
      {
        message.joinMessage.length > 0 && <p className='message'>{message.joinMessage}</p>
      }
    </section>
  )
}

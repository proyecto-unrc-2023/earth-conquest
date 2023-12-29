import './Login.css'
import buttonSound from '../../sound/select.mp3'

export function Login ({ game, setNameGreen, cuandoSeJoinea, nameGreen, playSound }) {
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
          onMouseEnter={() => playSound(buttonSound)}
          className='btn-login'
        >
          Join
        </button>
      </label>
    </section>
  )
}

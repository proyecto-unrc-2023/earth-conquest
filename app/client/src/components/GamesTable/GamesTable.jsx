import './GamesTable.css'
export const GamesTable = ({ allGames }) => {
  return (
    <table>
      <thead>
        <tr>
          <th>Game Id</th>
          <th>Blue Player</th>
          <th>Green Player</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        {
      allGames.map((game, index) => {
        return (

          <tr key={index}>
            <td>{game.game_id}</td>
            <td>{game.blue_player}</td>
            <td>{game.green_player}</td>
            <td>{game.status}</td>
            <td><button>Join</button></td>
          </tr>

        )
      })
      }
      </tbody>
    </table>
  )
}

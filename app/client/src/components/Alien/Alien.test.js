import React from 'react'
import '@testing-library/jest-dom'
import { render } from '@testing-library/react'
import { prettyDOM } from '@testing-library/react'
import { Alien } from './Alien'
import { team } from '../../constants'

test('renderiza el componente Alien ', () => {
  const teams = team.blue
  const eyes = 1

  const { getByAltText } = render(<Alien team={teams} eyes={eyes} />)

  const alienElement = getByAltText(`img_${teams}_alien`)
  console.log(prettyDOM(alienElement))
  expect(alienElement).toBeInTheDocument()
})

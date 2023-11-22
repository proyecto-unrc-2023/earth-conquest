/* eslint-disable no-undef */
import React from 'react'
import '@testing-library/jest-dom'
import { render, prettyDOM } from '@testing-library/react'
import { Alien } from './Alien'
import { team } from '../../constants'
import { handleAliens, getAliensDirections } from '../../services/alienService'

test('renderiza el componente Alien ', () => {
  const teams = team.BLUE
  const eyes = 1

  const { getByTestId } = render(<Alien team={teams} eyes={eyes} id={1} direction='none' />)

  const alienElement = getByTestId('alien-image')
  console.log(prettyDOM(alienElement))
  expect(alienElement.classList.contains('img_blue_alien')).toBeTruthy()
})

test('primer posicion de aliens', () => {
  const aliens = []
  const hash1 = {
    '(0, 0)': {
      aliens: [
        {
          id: 1,
          eyes: 1,
          team: 'BLUE'
        }
      ],
      modifier: null,
      alterator: null
    },
    '(0, 1)': {
      aliens: [],
      modifier: null,
      alterator: null
    }
  }
  const result = [{ id: 1, direction: 'none' }]
  const newAliens = handleAliens(aliens, hash1)
  const aliensDirections = getAliensDirections(newAliens)
  expect(aliensDirections).toEqual(result)
})

test('actualizar posicion de aliens', () => {
  const aliens = []
  const hash1 = {
    '(0, 0)': {
      aliens: [],
      modifier: null,
      alterator: null
    },
    '(0, 1)': {
      aliens: [
        {
          id: 1,
          eyes: 1,
          team: 'BLUE'
        }
      ],
      modifier: null,
      alterator: null
    },
    '(0, 2)': {
      aliens: [
        {
          id: 2,
          eyes: 1,
          team: 'BLUE'
        }
      ],
      modifier: null,
      alterator: null
    }
  }
  const hash2 = {
    '(0, 0)': {
      aliens: [],
      modifier: null,
      alterator: null
    },
    '(0, 1)': {
      aliens: [
        {
          id: 2,
          eyes: 1,
          team: 'BLUE'
        }
      ],
      modifier: null,
      alterator: null
    },
    '(0, 2)': {
      aliens: [
        {
          id: 1,
          eyes: 1,
          team: 'BLUE'
        }
      ],
      modifier: null,
      alterator: null
    }
  }
  const result = [{ id: 1, direction: 'right' }, { id: 2, direction: 'left' }]
  const newAliens1 = handleAliens(aliens, hash1)
  const newAliens2 = handleAliens(newAliens1, hash2)
  console.log(newAliens2)
  const aliensDirections = getAliensDirections(newAliens2)
  expect(aliensDirections).toEqual(result)
})

import React from 'react'
import '@testing-library/jest-dom'
import { render } from '@testing-library/react'
import { Modifier } from './Modifier'
import { modifier } from '../../constants'

test('renderiza el componente Moidifier con mountain', () => {
  const { container } = render(<Modifier type={modifier.mountain} />)

  expect(container.querySelector('.img_mountain')).toBeInTheDocument()
})

test('renderiza el componente Moidifier con killer', () => {
  const { container } = render(<Modifier type={modifier.killer} />)

  expect(container.querySelector('.img_killer')).toBeInTheDocument()
})

test('renderiza el componente Moidifier con multiplier', () => {
  const { container } = render(<Modifier type={modifier.multiplier} />)

  expect(container.querySelector('.img_multiplier')).toBeInTheDocument()
})

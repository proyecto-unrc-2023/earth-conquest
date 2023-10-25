import React from 'react'
import { render, fireEvent } from '@testing-library/react'
import '@testing-library/jest-dom'
import { Alterator } from './Alterator'
import { alterator } from '../../constants'

test('Renderiza el componente Alterator con trap', () => {
  const setAlterMock = jest.fn() // mock
  const { container } = render(<Alterator setAlter={setAlterMock} tipo={alterator.trap} />)

  // Verifica que el componente renderice la imagen de trap
  expect(container.querySelector('.img_trap')).toBeInTheDocument()

  // Simula hacer clic en el componente
  fireEvent.click(container.querySelector('.alterator'))

  // Verifica que la función setAlter se haya llamado con el tipo correcto
  expect(setAlterMock).toHaveBeenCalledWith(alterator.trap)
})

test('Renderiza el componente Alterator con directioner_down', () => {
  const setAlterMock = jest.fn()
  const { container } = render(<Alterator setAlter={setAlterMock} tipo={alterator.directioner_down} />)

  expect(container.querySelector('.img_directioner')).toBeInTheDocument()

  fireEvent.click(container.querySelector('.alterator'))

  expect(setAlterMock).toHaveBeenCalledWith(alterator.directioner_down)
})

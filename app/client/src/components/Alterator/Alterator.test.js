/* eslint-disable no-undef */
import React from 'react'
import { render, fireEvent, prettyDOM } from '@testing-library/react'
// import { prettyDOM } from '@testing-library/react'
import '@testing-library/jest-dom'
import { Alterator } from './Alterator'
import { alterator } from '../../constants'

test('Renderiza el componente Alterator con trap', () => {
  const { container } = render(<Alterator tipo={alterator.TRAP} />)
  console.log(prettyDOM(container.querySelector('.img_trap')))
  const img = container.querySelector('.img_trap')
  const src = img.getAttribute('src')
  // Verifica que el componente renderice la imagen de trap
  expect(src).toBe('../trap.png')
})

/*
test('Renderiza el componente Alterator con trap', () => {
  const setAlterMock = jest.fn() // mock
  const { container } = render(<Alterator setAlter={setAlterMock} tipo={alterator.TRAP} />)

  // Verifica que el componente renderice la imagen de trap
  expect(container.querySelector('.img_trap')).toBeInTheDocument()

  // Simula hacer clic en el componente
  fireEvent.click(container.querySelector('.alterator'))

  // Verifica que la función setAlter se haya llamado con el tipo correcto
  expect(setAlterMock).toHaveBeenCalledWith(alterator.TRAP)
})

test('Renderiza el componente Alterator con directioner_down', () => {
  const setAlterMock = jest.fn()
  const { container } = render(<Alterator setAlter={setAlterMock} tipo={alterator.DIRECTIONER_DOWNWARDS} />)

  expect(container.querySelector('.img_directioner')).toBeInTheDocument()

  fireEvent.click(container.querySelector('.alterator'))

  expect(setAlterMock).toHaveBeenCalledWith(alterator.DIRECTIONER_DOWNWARDS)
})

test('Renderiza el componente Alterator con directioner_up', () => {
  const setAlterMock = jest.fn()
  const { container } = render(<Alterator setAlter={setAlterMock} tipo={alterator.DIRECTIONER_UPWARDS} />)

  expect(container.querySelector('.img_directioner')).toBeInTheDocument()

  fireEvent.click(container.querySelector('.alterator'))

  expect(setAlterMock).toHaveBeenCalledWith(alterator.DIRECTIONER_UPWARDS)
})

test('Renderiza el componente Alterator con directioner_right', () => {
  const setAlterMock = jest.fn()
  const { container } = render(<Alterator setAlter={setAlterMock} tipo={alterator.DIRECTIONER_RIGHT} />)

  expect(container.querySelector('.img_directioner')).toBeInTheDocument()

  fireEvent.click(container.querySelector('.alterator'))

  expect(setAlterMock).toHaveBeenCalledWith(alterator.DIRECTIONER_RIGHT)
})

test('Renderiza el componente Alterator con directioner_left', () => {
  const setAlterMock = jest.fn()
  const { container } = render(<Alterator setAlter={setAlterMock} tipo={alterator.DIRECTIONER_LEFT} />)

  expect(container.querySelector('.img_directioner')).toBeInTheDocument()

  fireEvent.click(container.querySelector('.alterator'))

  expect(setAlterMock).toHaveBeenCalledWith(alterator.DIRECTIONER_LEFT)
})

test('Renderiza el componente Alterator con teleport_in', () => {
  const setAlterMock = jest.fn()
  const { container } = render(<Alterator setAlter={setAlterMock} tipo={alterator.TELEPORTER_IN} />)

  expect(container.querySelector('.img_teleporter')).toBeInTheDocument()

  fireEvent.click(container.querySelector('.alterator'))

  expect(setAlterMock).toHaveBeenCalledWith(alterator.TELEPORTER_IN)
})

test('Renderiza el componente Alterator con teleport_out', () => {
  const setAlterMock = jest.fn()
  const { container } = render(<Alterator setAlter={setAlterMock} tipo={alterator.TELEPORTER_OUT} />)

  expect(container.querySelector('.img_teleporter')).toBeInTheDocument()

  fireEvent.click(container.querySelector('.alterator'))

  expect(setAlterMock).toHaveBeenCalledWith(alterator.TELEPORTER_OUT)
})
*/

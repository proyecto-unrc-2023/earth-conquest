import React from 'react'
import { render, fireEvent } from '@testing-library/react'
//import { prettyDOM } from '@testing-library/react'
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

test('Renderiza el componente Alterator con directioner_up', () => {
  const setAlterMock = jest.fn()
  const { container } = render(<Alterator setAlter={setAlterMock} tipo={alterator.directioner_up} />)

  expect(container.querySelector('.img_directioner')).toBeInTheDocument()

  fireEvent.click(container.querySelector('.alterator'))

  expect(setAlterMock).toHaveBeenCalledWith(alterator.directioner_up)
})

test('Renderiza el componente Alterator con directioner_right', () => {
  const setAlterMock = jest.fn()
  const { container } = render(<Alterator setAlter={setAlterMock} tipo={alterator.directioner_right} />)

  expect(container.querySelector('.img_directioner')).toBeInTheDocument()

  fireEvent.click(container.querySelector('.alterator'))

  expect(setAlterMock).toHaveBeenCalledWith(alterator.directioner_right)
})

test('Renderiza el componente Alterator con directioner_left', () => {
  const setAlterMock = jest.fn()
  const { container } = render(<Alterator setAlter={setAlterMock} tipo={alterator.directioner_left} />)

  expect(container.querySelector('.img_directioner')).toBeInTheDocument()

  fireEvent.click(container.querySelector('.alterator'))

  expect(setAlterMock).toHaveBeenCalledWith(alterator.directioner_left)
})

test('Renderiza el componente Alterator con teleport_in', () => {
  const setAlterMock = jest.fn()
  const { container } = render(<Alterator setAlter={setAlterMock} tipo={alterator.teleport_in} />)

  expect(container.querySelector('.img_teleporter')).toBeInTheDocument()

  fireEvent.click(container.querySelector('.alterator'))

  expect(setAlterMock).toHaveBeenCalledWith(alterator.teleport_in)
})

test('Renderiza el componente Alterator con teleport_out', () => {
  const setAlterMock = jest.fn()
  const { container } = render(<Alterator setAlter={setAlterMock} tipo={alterator.teleport_out} />)

  expect(container.querySelector('.img_teleporter')).toBeInTheDocument()

  fireEvent.click(container.querySelector('.alterator'))

  expect(setAlterMock).toHaveBeenCalledWith(alterator.teleport_out)
})

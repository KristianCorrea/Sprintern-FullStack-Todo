import React from 'react'
import { Routes, Route } from 'react-router-dom'
import Login from './pages/Login'

function App() {
  return (
    // <NavBar/>
    <Routes>
      <Route path='/login' element={<Login/>}/>
    </Routes>
  )
}

export default App

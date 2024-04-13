import './App.css'
import Button from '@mui/material/Button';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Home from './pages/Home';
import Register from './pages/Register';
import Login from './pages/Login';
import Navbar from './components/Navbar'

function App() {


  return (
    <>
    <Navbar/>
    <BrowserRouter>
    <Routes>
      <Route path='/' element={<Home/>} />
      <Route  path='/register' element={<Register/>} />
      <Route path="/login" element={<Login/>} />

    </Routes>
    
    </BrowserRouter>
      
      <Button variant="contained">Hello world</Button>
    </>
  )
}

export default App

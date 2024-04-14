import './App.css'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Home from './pages/Home';
import Register from './pages/Register';
import Login from './pages/Login';
import Navbar from './components/Navbar';
import { Button } from '@material-tailwind/react';
function App() {


  return (
    <>
    <Button className='text-xl'>Button</Button>
    <BrowserRouter>
    <Navbar/>
    <Routes>
      <Route path='/' element={<Home/>} />
      <Route  path='/register' element={<Register/>} />
      <Route path="/login" element={<Login/>} />

    </Routes>
    
    </BrowserRouter>
    
    </>
  )
}

export default App

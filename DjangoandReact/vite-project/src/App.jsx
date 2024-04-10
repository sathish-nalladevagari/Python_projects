
import './App.css'
import { BrowserRouter, Routes , Route , Navigate} from 'react-router-dom'
import Home from './components/Home'
import ProtectedRoute from './components/ProtectedRoute'
import Login from './components/Login'
import Register from './components/Register'


function Logout() {
  localStorage.clear()
  return <Navigate to="/login" />
}

function RegisterAndLogout() {
  localStorage.clear()
  return <Register />
}

function App() {

  return (
    <>
    <BrowserRouter>
      <Routes>
        <Route element={<ProtectedRoute/>}>
          <Route path='/' element={<Home/>}/>
        </Route>
        <Route path='login' element={<Login/>} exact />
        <Route path='logout' element={<Logout/>} exact />
        <Route path='register' element={<RegisterAndLogout/>}  />
      </Routes>
    </BrowserRouter>
    </>
  )
}

export default App

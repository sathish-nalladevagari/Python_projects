import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from 'axios'
import { ACCESS_TOKEN , REFRESH_TOKEN } from "../constants";
import api from "../api";


function Form({route , method}) {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const navigate = useNavigate()

    const name = method === 'login' ? "Login" : "Register"
    const handleSubmit = async(e) =>{
        e.preventDefault();
        try {
            const res = await api.post(route, {username : username , password : password})
            if (method === 'login'){

              localStorage.setItem(ACCESS_TOKEN, res.data.access)
              localStorage.setItem(REFRESH_TOKEN, res.data.refresh)
              navigate("/")
            } 
            else{
              navigate("/login")
            }
        } catch (error) {
            alert(error)
        }
      
    }

  return (
    <>
    <form onSubmit={handleSubmit}>
  <div className="mb-3">
    <label  className="form-label">Username</label>
    <input type="text" className="form-control" value={username} onChange={(e)=> setUsername(e.target.value)} />

  </div>
  <div className="mb-3">
    <label  className="form-label">Password</label>
    <input type="password" className="form-control" value={password} onChange={(e) => setPassword(e.target.value)} />
  </div>
  <button type="submit" className="btn btn-primary">{name}</button>
</form>
    </>
  )
}

export default Form
import { Children, useState ,useEffect } from "react"
import {useNavigate, Outlet } from "react-router-dom"
import api from "../api"
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants"
import { jwtDecode} from "jwt-decode"

function ProtectedRoute() {

    useEffect(()=>{
        auth().catch(()=>{
            setIsAuthorized(false)
        },[])
    })
    const [isAuthorized, setIsAuthorized] = useState(null)
    const navigate  = useNavigate()

    const refreshToken = async() =>{
        const refreshToken = localStorage.getItem(REFRESH_TOKEN)
        try {
            const res = await api.post("/api/token/refresh/", {
                refresh : refreshToken
            })
            if (res.status === 200) {
                localStorage.setItem(ACCESS_TOKEN, res.data.access)
                setIsAuthorized(true)
            } else {
                setIsAuthorized(false)
            }
        } catch (error) {
            setIsAuthorized(false)
            alert(error)
        }
            
    }

    const auth = async () =>{
        const token = localStorage.getItem(ACCESS_TOKEN)
        if (!token){
            setIsAuthorized(false);
            return;
        }
        const decoded = jwtDecode(token)
        const tokenExpiration = decoded.exp;
        const now = Date.now()

        if (tokenExpiration < now){
            await refreshToken()

        }else{
            setIsAuthorized(true)
        }
    }
    if (isAuthorized === null){
        return <div>Loading...</div>
    }


  return isAuthorized ? <Outlet/> : navigate("/login")
}

export default ProtectedRoute
import axios from 'axios'

 const api = axios.create({
    withCredentials: true,
    baseURL : "http://127.0.0.1:8000/",
    headers: {'Content-Type': 'application/json'},
    credentials: 'include',
});
export default api;
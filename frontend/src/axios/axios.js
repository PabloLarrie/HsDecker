import axios from "axios"

const API = axios.create({ baseURL: "http://localhost:8000" })

API.defaults.headers.post["Content-Type"] = "application/json"
API.defaults.headers.patch["Content-Type"] = "application/json"
API.defaults.headers.put["Content-Type"] = "application/json"

export const api = {
    install(Vue) {
        Vue.prototype.$api = API
    }
}
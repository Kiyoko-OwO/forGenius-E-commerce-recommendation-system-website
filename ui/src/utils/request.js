import axios from 'axios'

const request = axios.create({
    baseURL: 'http://127.0.0.1:8888/api/private/v1/' // base path to API
})

export default request
import axios from 'axios'

let instance = axios.create({
    baseURL : '/'
});

export const AXIOS = instance;
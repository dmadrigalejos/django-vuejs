import { AXIOS } from '@/helpers/interceptor.js'

export default {
    getUsers() {
        return AXIOS.get('/myapp/user/');
    },
    addUser(user) {
        return AXIOS.post('/myapp/user/', user)
    },
    editUser(user, id) {
        return AXIOS.put('/myapp/user/' + id + '/', user)
    }
}
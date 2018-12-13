import { AXIOS } from '@/helpers/interceptor.js'

export default {
    loginUser(user) {
        return AXIOS.post('/myapp/login/', user);
    },
    logoutUser() {
        return AXIOS.get('/myapp/login/invalidate');
    }
}
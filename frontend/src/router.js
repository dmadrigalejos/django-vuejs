import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

import { AXIOS } from '@/helpers/interceptor'
import store from './store';

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta : {
        fullscreen : false
      }
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('./views/Login.vue'),
      meta : {
        fullscreen : true
      }      
    },
    {
      path: '/users',
      name: 'users',
      component: () => import('./views/Users.vue'),
      meta : {
        fullscreen : false
      }
    }
  ]
})

router.beforeEach((to, from, next) => {
  AXIOS.get('/myapp/login/authenticate')
  .then(response => {
    console.log(response.data);
    store.commit('setUser', response.data)

    if (to.path === '/login') {
      next('/')
    } else {
      next();
    }
  })
  .catch(e => {
    console.log(e);

    if (to.path != '/login') {
      next('/login')
    } else {
      next();
    }
  })
});


export default router
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    drawer : true,
    user : {}
  },
  mutations: {
    toggleDrawer : function(state) {
      state.drawer = !state.drawer
    },
    setUser : function(state, user) {
      state.user = user;
    }
  },
  actions: {

  }
})

<template>
    <div class="toolbar">
        <v-toolbar
      :clipped-left="$vuetify.breakpoint.lgAndUp"
      color="blue darken-3"
      dark
      app
      fixed
    >
      <v-toolbar-title style="width: 300px" class="ml-0 pl-3">
        <v-toolbar-side-icon @click.stop="toggle"></v-toolbar-side-icon>
        <span class="hidden-sm-and-down">Project X</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      {{ $store.state.user.userFirstname }}
      <v-btn icon large @click="logout">
        <v-avatar size="32px" tile>
          <img
            src="https://cdn.vuetifyjs.com/images/logos/logo.svg"
            alt="Vuetify"
          >
        </v-avatar>
      </v-btn>
    </v-toolbar>
    </div>
</template>

<script>
import LoginService from '@/api/loginservice.js'
export default {
    name : 'ToolBar',
    methods: {
      logout : function() {
        LoginService.logoutUser()
        .then(response => {
          this.$router.push('/login')          
        })
        .catch(e => {
          console.log(e);
        })
      },
      toggle : function() {
          this.$store.commit('toggleDrawer')
      }
    }
}
</script>

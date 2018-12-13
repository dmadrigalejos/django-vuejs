<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Login</v-toolbar-title>
                <v-spacer></v-spacer>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field v-model="user.userName" prepend-icon="person" name="login" label="Login" type="text"></v-text-field>
                  <v-text-field v-model="user.userPassword" id="password" prepend-icon="lock" name="password" label="Password" type="password"></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="login" color="primary">Login</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import LoginService from '@/api/loginservice.js'
  export default {
    data: () => ({
      drawer: null,
      user : {
        userName : '',
        userPassword : ''
      }
    }),
    methods : {
      login() {
        LoginService.loginUser(this.user)
        .then(response => {
          console.log(response);          
          this.$router.push('/')
        })
        .catch(e => {
          console.log(e);
        })
      }
    }
  }
</script>

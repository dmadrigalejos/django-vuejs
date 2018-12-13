<template>
  <div>
    <v-toolbar flat color="white">
      <v-toolbar-title>Users</v-toolbar-title>
      <v-divider
        class="mx-2"
        inset
        vertical
      ></v-divider>
      <v-spacer></v-spacer>
      <v-dialog v-model="dialog" max-width="500px">
        <v-btn slot="activator" color="primary" dark class="mb-2">New User</v-btn>
        <v-card>
          <v-card-title>
            <span class="headline">{{ formTitle }}</span>
          </v-card-title>

          <v-card-text>
            <v-container grid-list-md>
              <v-layout wrap>
                <v-flex xs12>
                  <v-text-field v-model="editedItem.userId" label="User Id"></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-text-field v-model="editedItem.username" label="Username"></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-text-field v-model="editedItem.userFirstname" label="Firstname"></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-text-field v-model="editedItem.userLastname" label="Lastname"></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-text-field v-model="editedItem.userPassword" label="Password"></v-text-field>
                </v-flex>
              </v-layout>
            </v-container>
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" flat @click="close">Cancel</v-btn>
            <v-btn color="blue darken-1" flat @click="save">Save</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-toolbar>
    <v-data-table
      :headers="headers"
      :items="users"
      class="elevation-1"
    >
      <template slot="items" slot-scope="props">
        <td>{{ props.item.userId }}</td>
        <td>{{ props.item.username }}</td>
        <td>{{ props.item.userFirstname }}</td>
        <td>{{ props.item.userLastname }}</td>
        <td>
          <v-icon
            small
            class="mr-2"
            @click="editItem(props.item)"
          >
            edit
          </v-icon>
          <v-icon
            small
            @click="deleteItem(props.item)"
          >
            delete
          </v-icon>
        </td>
      </template>
      <template slot="no-data">
        <v-btn color="primary" @click="initialize">Reset</v-btn>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import UserService from '@/api/userservice.js'

  export default {
    data: () => ({
      dialog: false,
      headers: [
        { text: 'Id', value: 'userId' },
        { text: 'Username', value: 'username' },
        { text: 'Firstname', value: 'userFirstname' },
        { text: 'Lastname', value: 'userLastname' },
        { text: 'Actions', value: 'name', sortable: false }
      ],
      users: [],
      editedIndex: -1,
      editedItem: {
        userId: '',
        username: '',
        userFirstname: '',
        userLastname: '',
        userPassword: ''
      },
      defaultItem: {
        userId: '',
        username: '',
        userFirstname: '',
        userLastname: '',
        userPassword: ''
      }
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New User' : 'Edit User'
      }
    },

    watch: {
      dialog (val) {
        val || this.close()
      }
    },

    created () {
      this.initialize()
    },

    methods: {
      initialize () {
        UserService.getUsers()
        .then(response => {
          this.users = response.data;
        })
        .catch(e => {
          console.log(e);
        })
      },

      editItem (item) {
        this.editedIndex = this.users.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        const index = this.users.indexOf(item)
        confirm('Are you sure you want to delete this item?') && this.users.splice(index, 1)
      },

      close () {
        this.dialog = false
        setTimeout(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        }, 300)
      },

      save () {
        if (this.editedIndex > -1) {
          // update
          // Object.assign(this.users[this.editedIndex], this.editedItem)
          UserService.editUser(this.editedItem, this.editedItem.userId)
          .then(response => {
            console.log(response);
            this.initialize();
          })
          .catch(e => {
            console.log(e);
          })
        } else {
          // new
          // this.users.push(this.editedItem)
          UserService.addUser(this.editedItem)
          .then(response => {
            console.log(response);
            this.initialize();
          })
          .catch(e => {
            console.log(e);
          })
        }
        this.close()
      }
    }
  }
</script>
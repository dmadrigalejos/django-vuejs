<template>
  <v-app id="inspire">
    <NavDrawer v-if="!$route.meta.fullscreen"></NavDrawer>
    <ToolBar v-if="!$route.meta.fullscreen"></ToolBar>
    <v-content>
      <router-view></router-view>
    </v-content>    
  </v-app>
</template>

<script>
import NavDrawer from '@/components/NavDrawer'
import ToolBar from '@/components/ToolBar'

  export default {
    components : {
      NavDrawer,
      ToolBar
    }
  }
</script>

<template>
  <v-app id="app">
    <Header />
    <div class="main-board">
      <nuxt/>
    </div>
  </v-app>
</template>

<script lang="ts">
import Header from "~/components/Header.vue";

import {defineComponent} from "@nuxtjs/composition-api";

export default defineComponent({
  components: { Header }
})
</script>

<style scoped>
body {
  max-width: 1200px;
}

.v-application {
  background: #e8ebeb;
}

.main-board{
  margin: 20px;
  margin-top: 26px;
  margin-bottom: 26px;
  padding: 20px;
  background: white;
  height: 100%;
  box-shadow: 0 10px 20px 0 rgba(0, 0, 0, .2);
}
</style>

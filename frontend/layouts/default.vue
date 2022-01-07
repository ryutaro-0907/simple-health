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
  background: #d5fafa;
}

.main-board{
  margin: 20px;
  margin-top: 26px;
  margin-bottom: 26px;
  padding: 20px;
  background: rgb(226, 224, 224);
  height: 100%;
  box-shadow: 0 10px 20px 0 rgba(2, 2, 2, 0.2);
}
</style>
